import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 在figure上画出函数图像
# =========================================================== 
# 线形：  -实线，--双划线，:虚线，:.点划线                        
# 标记符：+叉号，o圆，*星状，.实心圆，s正方形，^v<>上下左右三角 
# 颜色：  r蓝色，g绿色，b蓝色，y黄色，k黑色，c青绿色            
# ===========================================================
def drawLine(fig,s1,s2,s3,x,y,style,isAnnotate=False,x0=0,y0=0,anText='None',s=None,anStyle='--k',isLegend=False,ll='None',title='None',isLim=False,lim=None,xl='None',yl='None',):
    # 设置子图
    ax = fig.add_subplot(s1,s2,s3)
    # 题目的设置
    plt.title(title)
    # xy轴的限制    
    if isLim:
        plt.xlim(lim[0],lim[1])
        plt.ylim(lim[2], lim[3])   
    # xy轴的描述文本
    plt.xlabel(xl)
    plt.ylabel(yl)
    
    # 设置xy轴的刻度
    # plt.xticks(np.linspace(-1, 1, 5))
    # 设置y坐标轴刻度及标签, $$是设置字体
    # plt.yticks([0, 0.5], ['$minimum$', 'normal'])

    # 绘制图像
    l1, = plt.plot(x,y,style,label='double')
   
    # 图像图例
    if isLegend:
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width*0.9, box.height])
        plt.legend(handles = [l1,], labels = [ll], bbox_to_anchor=(1, 0.5),ncol=1,loc = 'center left')
    
    # 加注释点
    if isAnnotate:
        plt.scatter(x0,y0,s=50,color='k')
        plt.plot([x0,x0],[y0,0],anStyle,lw=2.5)
        plt.annotate(s=anText,xy=(x0,y0),xytext=(s[0],s[1]),textcoords='offset points',
                    arrowprops=dict(arrowstyle='->',Connectionstyle='arc3,rad=.2'))
    # 设置坐标轴
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    # 设置网格
    plt.grid(axis="y")

# 在figure上画出柱状图
# =========================================================
# Macaron色谱
# 马卡龙玫瑰        #E27386
# 马卡龙玫瑰粉红    #f55066
# 巧克力马卡龙      #cb8e85
# 马卡龙抹茶奶霜    #b7d28d 
# 开心果杏仁杏仁饼  #dcff93
# 马卡龙粉         #f1b8e4
# 杏仁饼紫         #d9b8f1
# 杏仁饼海洋蓝     #b8f1ed
# 马卡龙芒果激情   #fecf45
# 巧克力樱桃色     #aa5b71
# 马卡龙巧克力，橙 #ff8240
# 马卡龙柚子覆盆子 #f9b747
# 马卡龙覆盆子     #fe9778
# =========================================================
def drawBar(fig,s1,s2,s3,x,y,facecolor,edgecolor,isUp=False,isBottom=False,title='None',isLim=False,lim=None,xl='None',yl='None'):
    # 设置子图
    ax = fig.add_subplot(s1,s2,s3)
    # 题目的设置
    plt.title(title)
    # xy轴的限制    
    if isLim:
        plt.xlim(lim[0],lim[1])
        plt.ylim(lim[2], lim[3])   
    # xy轴的描述文本
    plt.xlabel(xl)
    plt.ylabel(yl)
    # 绘图
    plt.bar(x,y,facecolor=facecolor,edgecolor=edgecolor)
    # 现实数值
    if isUp:
        for x,y in zip(x,y):
            plt.text(x+0.4,y+0.05,'%.2f'%y,ha='center',va='bottom')
    if isBottom:
        for x,y in zip(x,y):
            plt.text(x+0.4,y-0.05,'%.2f'%y,ha='center',va='top')

# 在figure上画出等高线图
# =========================================================
# cmap 的候选值 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 
# 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r',
#  'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 
# 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 
# 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 
# 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 
# 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 
# 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r',
#  'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3',
#  'Set3_r', 'Spectral', 'Spectral_r', 'Vega10', 'Vega10_r', 'Vega20',
# 'Vega20_r', 'Vega20b', 'Vega20b_r', 'Vega20c', 'Vega20c_r', 'Wistia', 
# 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r',
#  'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 
# 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 
# 'bwr_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 
# 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth',
#  'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r',
#  'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern',
#  'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r',
#  'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 
# 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r',
#  'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism',
#  'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spectral',
#  'spectral_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r',
#  'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 
# 'terrain_r', 'viridis', 'viridis_r', 'winter', 'winter_r'
#  num 表示被分成的段数
# =========================================================
def contour(fig,s1,s2,s3,x,y,z,num,cmap,title="None",isLim=False,lim=None):
    # 设置子图
    ax = fig.add_subplot(s1,s2,s3)
    # 题目的设置
    if title != "None":
        plt.title(title)
    # xy轴的限制    
    if isLim:
        plt.xlim(lim[0],lim[1])
        plt.ylim(lim[2], lim[3])
    # 绘图
    X,Y = np.meshgrid(x,y)
    plt.contourf(X,Y,z,num,alpha=0.75,cmap=cmap)
    C = plt.contour(X,Y,z,num,color='k',linewidth=0.5)
    plt.clabel(C,inline=True,fontsize=10)

# 在figure上画3d图
# =========================================================
# x,y,z都是2d-array
# cmap = plt.get_cmap('rainbow')|...
# =========================================================
def drawfor3D(fig,x,y,z,camp):
    ax = Axes3D(fig)
    ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=camp)

fig = plt.figure()
plt.show()
