"""Render original synthetic chart examples; requires numpy and matplotlib.

Run: python scripts/render_gallery.py --out figure-gallery.png
This is a chart-selection aid, not a real-data plotting pipeline.
"""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.ticker import MaxNLocator
from figure_style import load_palettes, rcparams

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    rng=np.random.default_rng(20261018)
    data=load_palettes(); colors=data['palettes']['scenario']['colors']
    plt.rcParams.update(rcparams())
    plt.rcParams.update({'font.size':10,'axes.labelsize':9,'xtick.labelsize':8,'ytick.labelsize':8})
    fig, axs=plt.subplots(3,3,figsize=(14,11),layout='constrained')
    fig.suptitle('PV & Energy Research | Chart Selection Examples\nSYNTHETIC DATA - DESIGN EXAMPLES ONLY',fontsize=18,fontweight='bold')
    titles=['a  Ranked potential + intervals','b  Scenario paths + uncertainty','c  Household outcome distributions',
            'd  Threshold coverage curves','e  Subgroup effects + intervals','f  Multi-benefit trade-offs',
            'g  Feasibility / sensitivity matrix','h  Additive contribution breakdown','i  Capacity-weighted priority curve']
    for ax,title in zip(axs.flat,titles):
        ax.set_title(title,loc='left',fontsize=11,fontweight='bold',pad=10)
        ax.grid(axis='y',color='#E7EAED',lw=.6,zorder=0)
    ax=axs[0,0]; y=np.arange(7); v=np.array([2.2,3.4,4.1,5.0,6.8,7.6,9.1])
    ax.errorbar(v,y,xerr=.35+np.arange(7)*.09,fmt='o',color=colors[0],capsize=2)
    ax.set_yticks(y,[f'City {i}' for i in range(1,8)]); ax.set_xlabel('Potential (mock units)'); ax.set_xlim(0,11)
    ax=axs[0,1]; x=np.arange(2020,2051,5)
    for k in range(3):
        v=1+(x-2020)*(.025+.015*k)
        band=(x-2020)*.004+.04
        ax.fill_between(x,v-band,v+band,color=colors[k],alpha=.17)
        ax.plot(x,v,color=colors[k],label=f'S{k+1}')
    ax.legend(); ax.set_xlabel('Year'); ax.set_ylabel('Index (mock units)')
    ax=axs[0,2]
    dist=[rng.lognormal(.4+.17*k,.35,160) for k in range(3)]
    bp=ax.boxplot(dist,patch_artist=True,showfliers=False,widths=.45)
    for box,c in zip(bp['boxes'],colors): box.set_facecolor(c); box.set_alpha(.4)
    for i,values in enumerate(dist,1): ax.scatter(rng.normal(i,.06,len(values)),values,s=4,alpha=.15,color=colors[i-1],rasterized=True)
    ax.set_xticks([1,2,3],['Low income','Middle','High']); ax.set_ylabel('Savings (mock units)')
    ax=axs[1,0]; x=np.linspace(0,24,120)
    for k in range(2): ax.plot(x,100*np.exp(-(x/(10+7*k))**1.6),color=colors[k],label=f'Plan {k+1}')
    ax.axvline(8,ls='--',color='#707780',lw=.8); ax.text(8.5,92,'8 h threshold',fontsize=9)
    ax.set(xlabel='Backup duration (h)',ylabel='Households meeting duration (%)',ylim=(0,105)); ax.legend()
    ax=axs[1,1]; v=np.array([-.9,-.5,-.7,.1]); err=np.array([.22,.15,.3,.2]); yy=np.arange(4)
    ax.axvline(0,color='#707780',ls='--',lw=.8); ax.errorbar(v,yy,xerr=err,fmt='o',capsize=2,color=colors[2])
    ax.set_yticks(yy,['Group A','Group B','Group C','Group D']); ax.set_xlabel('Effect (mock units)')
    ax=axs[1,2]
    for k in range(3):
        xx=rng.uniform(.1,1,50); vv=.3+.5*xx+rng.normal(0,.12,50)+k*.1
        ax.scatter(xx,vv,s=16,color=colors[k],alpha=.65,label=f'Region {k+1}',edgecolors='none')
    ax.set(xlabel='Carbon benefit (mock units)',ylabel='Water benefit (mock units)'); ax.legend()
    ax=axs[2,0]; xx,yy=np.meshgrid(np.arange(1,8),np.arange(1,7)); z=(xx-4)*.7+(yy-3)*.5
    mask=yy>xx+2; z=np.ma.array(z,mask=mask)
    cmap=LinearSegmentedColormap.from_list('tradeoff',data['palettes']['tradeoff-div']['colors']); cmap.set_bad('#E3E5E8')
    mesh=ax.pcolormesh(np.arange(.5,8),np.arange(.5,7),z,cmap=cmap,norm=TwoSlopeNorm(vcenter=0,vmin=-3.5,vmax=3.5),edgecolors='white',linewidth=.5)
    ax.contour(xx,yy,z,levels=[0],colors='#252A30',linewidths=1)
    ax.set(xlabel='Grid availability (mock units)',ylabel='Service target (mock units)')
    fig.colorbar(mesh,ax=ax,label='Cost difference (mock units)',shrink=.75)
    ax.text(1,5.3,'Infeasible',fontsize=9,color='#555B61')
    ax=axs[2,1]; changes=np.array([.8,-.3,-.5,.2]); start=1.2; totals=[start]
    ax.bar(0,start,color='#707780',width=.65)
    current=start
    for i,delta in enumerate(changes,1):
        ax.bar(i,abs(delta),bottom=min(current,current+delta),color=colors[1] if delta>0 else colors[2],width=.65)
        ax.plot([i-.65,i+.35],[current,current],color='#9AA1A8',lw=.5,ls=':')
        current+=delta; totals.append(current)
    ax.bar(5,current,color=colors[0],width=.65)
    ax.set_xticks(np.arange(6),['Start','A','B','C','D','End']); ax.set_ylabel('Additive outcome (mock units)'); ax.axhline(0,color='#707780',lw=.6)
    ax=axs[2,2]; widths=np.array([5,9,7,13,8,16,10,12,7,13]); heights=np.array([9.5,9,8.2,7.8,7.1,6.3,5.6,4.8,3.9,2.8])
    left=np.r_[0,np.cumsum(widths)[:-1]]
    ax.bar(left,heights,width=widths,align='edge',color=[colors[k%3] for k in range(10)],edgecolor='white',lw=.5)
    ax.axvline(60,color='#252A30',ls='--',lw=.8); ax.set(xlabel='Cumulative capacity (mock units)',ylabel='Marginal benefit (mock units)',xlim=(0,100))
    for ax in axs.flat: ax.xaxis.set_major_locator(MaxNLocator(nbins=5)) if ax not in [axs[0,2],axs[2,1]] else None
    fig.savefig(args.out,dpi=170)
    plt.close(fig)
    print(args.out)

if __name__=='__main__': main()
