"""Render an original four-panel comparison using synthetic districts only."""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize, TwoSlopeNorm
from matplotlib.patches import Patch
import numpy as np

from figure_style import load_palettes, rcparams


def demo_values():
    """Rows and columns are a fictitious study region, without a CRS."""
    rng = np.random.default_rng(22)
    y, x = np.indices((7, 10))
    domain = ((x - 4.5 + (y - 3) * 0.35) / 5.1) ** 2 + ((y - 3) / 4.1) ** 2 < 1
    before = np.where(domain, 22 + x * 4 + y * 2 + rng.normal(0, 5, x.shape), np.nan)
    after = np.where(domain, before + (x - 4) * 3 - (y - 3) * 2 +
                     rng.normal(0, 5, x.shape), np.nan)
    before[2, 3] = np.nan
    after[4, 7] = np.nan
    return domain, before, after


def render(out, svg=None):
    p = load_palettes()
    n = p["neutral"]
    plt.rcParams.update(rcparams())
    plt.rcParams.update({"text.color": n["text"], "axes.labelcolor": n["text"],
                         "xtick.color": n["text"], "ytick.color": n["text"]})
    domain, before, after = demo_values()
    delta = after - before
    seq = LinearSegmentedColormap.from_list("level", p["palettes"]["urban-exposure-seq"]["colors"])
    div = LinearSegmentedColormap.from_list("change", p["palettes"]["urban-effect-div"]["colors"])
    for cmap in (seq, div):
        cmap.set_bad(n["missing"])
    vmax = 10 * np.ceil(np.nanmax(np.stack([before, after])) / 10)
    limit = 5 * np.ceil(np.nanmax(np.abs(delta)) / 5)
    level = Normalize(0, vmax)
    change = TwoSlopeNorm(0, -limit, limit)
    fig = plt.figure(figsize=(7.1, 5.9), layout="constrained")
    grid = fig.add_gridspec(5, 2, height_ratios=[0.45, 2.5, .12, 2.65, .57],
                           width_ratios=[1, 1])
    header = fig.add_subplot(grid[0, :])
    header.axis("off")
    header.text(0, .65, "Comparing exposure across two periods", size=14, weight="bold")
    header.text(0, .04, "SYNTHETIC DATA  /  FICTITIOUS REGION", size=8, color=n["baseline"])

    def grid_map(ax, values, cmap, norm, title):
        h, w = domain.shape
        yy, xx = np.indices((h, w))
        colors = cmap(norm(np.ma.masked_invalid(values[domain])))
        # Distinguish in-domain missing data (gray) from the white exterior.
        ax.bar(xx[domain], height=1, width=1, bottom=yy[domain] - .5,
               color=colors, edgecolor="white", linewidth=.55)
        missing = domain & ~np.isfinite(values)
        ax.bar(xx[missing], height=1, width=1, bottom=yy[missing] - .5,
               color="none", edgecolor=n["baseline"], linewidth=0, hatch="///")
        ax.set(xlim=(-.5, w-.5), ylim=(h-.5, -.5), aspect="equal")
        ax.axis("off")
        ax.set_title(title, loc="left", weight="bold", pad=5, fontsize=9)
        return matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)

    a, b = fig.add_subplot(grid[1, 0]), fig.add_subplot(grid[1, 1])
    level_key = grid_map(a, before, seq, level, "a   Baseline exposure")
    grid_map(b, after, seq, level, "b   Follow-up exposure")
    cax = fig.add_subplot(grid[2, :])
    fig.colorbar(level_key, cax=cax, orientation="horizontal", label="Exposure index",
                 ticks=np.arange(0, vmax + 1, 30))

    c, d = fig.add_subplot(grid[3, 0]), fig.add_subplot(grid[3, 1])
    delta_key = grid_map(c, delta, div, change, "c   Change in exposure")
    yy, xx = np.where(np.isfinite(delta))
    select = np.argsort(delta[yy, xx])
    select = np.concatenate([select[:3], select[-3:]])
    yy, xx = yy[select], xx[select]
    initial, final = before[yy, xx], after[yy, xx]
    rows = np.arange(len(select))
    d.set_title("d   Three largest decreases and increases", loc="left", weight="bold", pad=5,
                fontsize=9)
    d.set_axisbelow(True)
    d.grid(axis="x", color=n["grid"], linewidth=.45)
    d.hlines(rows, initial, final, color=n["baseline"], linewidth=1.0)
    d.scatter(initial, rows, label="Baseline", facecolors="white", edgecolors="#2A668A",
              s=25, linewidths=1, zorder=3)
    d.scatter(final, rows, label="Follow-up", color="#2A668A", marker="D",
              s=19, linewidths=0, zorder=3)
    d.set(yticks=rows, yticklabels=[f"R{i+1:02} C{j+1:02}" for i, j in zip(yy, xx)],
          xlim=(0, vmax), xlabel="Exposure index")
    d.invert_yaxis()
    d.tick_params(axis="y", length=0)
    d.spines["left"].set_visible(False)

    footer_a = grid[4, 0].subgridspec(2, 1, height_ratios=[1, 1])
    cb = fig.colorbar(delta_key, cax=fig.add_subplot(footer_a[0]), orientation="horizontal",
                      ticks=[-limit, 0, limit])
    cb.set_label("Index points (follow-up minus baseline)", labelpad=1)
    meta = fig.add_subplot(grid[4, 1])
    meta.axis("off")
    handles, labels = d.get_legend_handles_labels()
    meta.legend(handles + [Patch(facecolor=n["missing"], edgecolor=n["baseline"],
                                 linewidth=0, hatch="///")], labels + ["Missing data"],
                loc="upper left", ncol=3, borderaxespad=0, handletextpad=.4, columnspacing=1)
    meta.text(0, -.02, f"{np.isfinite(delta).sum()} matched synthetic districts",
              color=n["baseline"], fontsize=7, transform=meta.transAxes)
    fig.savefig(out, dpi=300)
    if svg:
        fig.savefig(svg)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=Path("china-spatial-demo.png"), type=Path)
    parser.add_argument("--svg", type=Path, help="Optional editable SVG output")
    args = parser.parse_args()
    render(args.out, args.svg)
