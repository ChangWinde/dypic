import matplotlib.pyplot as plt
import numpy as np

# =========================================================== 
# 线形：  -实线，--双划线，:虚线，:.点划线                        
# 标记符：+叉号，o圆，*星状，.实心圆，s正方形，^v<>上下左右三角 
# 颜色：  r蓝色，g绿色，b蓝色，y黄色，k黑色，c青绿色            
# ===========================================================
# 在figure上画出函数图像
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

fig = plt.figure()
plt.show()
