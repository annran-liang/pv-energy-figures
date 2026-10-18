"""Print portable color/style recipes or create a palette preview (stdlib only)."""
import argparse
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]

def load_palettes():
    return json.loads((ROOT / 'assets' / 'palettes.json').read_text(encoding='utf-8'))

def rcparams():
    # Starting values at final physical size; adapt to the journal and language.
    return {'font.family':'sans-serif','font.sans-serif':['Arial','DejaVu Sans'],
            'font.size':8,'axes.labelsize':8,'xtick.labelsize':7,'ytick.labelsize':7,
            'legend.fontsize':7,'axes.linewidth':0.6,'lines.linewidth':1.2,
            'axes.spines.top':False,'axes.spines.right':False,'legend.frameon':False,
            'pdf.fonttype':42,'ps.fonttype':42,'svg.fonttype':'none',
            'savefig.facecolor':'white'}

def preview(out, data):
    width, height = 1000, 100 + 100 * len(data['palettes'])
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
             '<rect width="100%" height="100%" fill="white"/>',
             '<g font-family="Arial, sans-serif" fill="#252A30">',
             '<text x="28" y="32" font-size="21">PV &amp; Energy Research - Palette Library</text>',
             '<text x="28" y="58" font-size="13">Recommended colors; not exact paper extraction. Check the final figure for accessibility.</text>']
    for i, (name, item) in enumerate(data['palettes'].items()):
        y = 88 + 100*i
        parts.append(f'<text x="28" y="{y+20}" font-size="16">{escape(name)}</text>')
        parts.append(f'<text x="28" y="{y+42}" font-size="12">{item["type"]}</text>')
        for j, color in enumerate(item['colors']):
            x = 245 + j*101
            parts.append(f'<rect x="{x}" y="{y}" width="94" height="44" fill="{color}" stroke="#CCD1D6" stroke-width="0.5"/>')
            parts.append(f'<text x="{x+3}" y="{y+63}" font-size="12">{color}</text>')
    parts.append('</g></svg>')
    Path(out).write_text('\n'.join(parts),encoding='utf-8')

def main():
    data = load_palettes()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--palette', choices=list(data['palettes']), default='scenario')
    parser.add_argument('--format', choices=['json','python','r'], default='json')
    parser.add_argument('--preview', type=Path)
    args = parser.parse_args()
    if args.preview:
        preview(args.preview,data)
        print(str(args.preview))
        return
    selected = data['palettes'][args.palette]
    colors = selected['colors']
    if args.format == 'json':
        print(json.dumps({'id':args.palette,**selected,'neutral':data['neutral'],'rcParams':rcparams()},ensure_ascii=False,indent=2))
    elif args.format == 'python':
        print('import matplotlib as mpl\nfrom cycler import cycler\nfrom matplotlib.colors import LinearSegmentedColormap')
        print(f'COLORS = {colors!r}\nmpl.rcParams.update({rcparams()!r})')
        if selected['type'] == 'categorical':
            print('mpl.rcParams["axes.prop_cycle"] = cycler(color=COLORS)\n# Bind scientific labels to COLORS explicitly for stable mapping.')
        else:
            print(f'CMAP = LinearSegmentedColormap.from_list({args.palette!r}, COLORS)')
            if selected['type'] == 'diverging':
                print('# Set TwoSlopeNorm(vcenter=0, vmin=..., vmax=...) from the actual data.')
    else:
        print('library(ggplot2)\ncolors <- c('+', '.join(json.dumps(c) for c in colors)+')')
        print('theme_set(theme_classic(base_size = 8) + theme(legend.key = element_blank()))')
        if selected['type'] == 'categorical':
            print('# Name colors with actual scientific labels, then add:\n# + scale_color_manual(values = colors)\n# + scale_fill_manual(values = colors)')
        elif selected['type'] == 'sequential':
            print('# + scale_fill_gradientn(colours = colors)')
        else:
            print('# For a symmetric signed range, use gradientn with symmetric limits, or\n# scale_fill_gradient2(low=colors[1], mid=colors[4], high=colors[7], midpoint=0).')

if __name__ == '__main__':
    main()
