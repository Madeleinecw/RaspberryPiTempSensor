from utils.database_service import get_temps, get_timestamps
from datetime import datetime, timedelta
import matplotlib as mpl 
mpl.use('Agg')
from matplotlib import pyplot as plt
from mpld3 import fig_to_html, plugins
from matplotlib.lines import Line2D

def make_plot():
    
    css = """
    .mpld3-tooltip {
    background-color: white; 
    color: #AA280E }
    """ 

    fig, ax = plt.subplots()
    dev_x = get_temps()
    dev_y = get_timestamps()

    now = datetime.now()
    yesterday = datetime.now() - timedelta(0.5)
    
   
    plt.rcParams['axes.facecolor'] = '#621708'
    plt.grid(b=True, color='#AA280E')

    plt.ylim(16, 20)
    plt.xlim(yesterday, now)

    plt.title('Temperatures by Time of Day', color= '#F6AA1C')
    plt.ylabel('Temperatures', color= '#F6AA1C')
    plt.xlabel('Time of Day', color= '#F6AA1C')

    plt.show()

    

    fig.savefig('static/temp.png')

    lines = Line2D(dev_y, dev_x, color= '#F6AA1C', lw=1, marker='.')
    ax.add_line(lines)

    new_x = []
    for i in dev_x:
        new_x.append(i[0])

    label = [str(i) for i in new_x]

    labelTooltip = plugins.PointHTMLTooltip(lines, label, css=css)
    plugins.connect(fig, labelTooltip)

    plt_html = fig_to_html(fig, figid='graph-log-generated')
    return plt_html