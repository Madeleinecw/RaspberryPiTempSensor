from model.databasetemp import get_temps, get_timestamps
from datetime import datetime, timedelta
import matplotlib as mpl 
mpl.use('Agg')
from matplotlib import pyplot as plt
from mpld3 import fig_to_html, plugins

def make_plot():
 
    fig, ax = plt.subplots()
    dev_x = get_temps()
    dev_y = get_timestamps()

    now = datetime.now()
    yesterday = datetime.now() - timedelta(1)
    
   
    plt.rcParams['axes.facecolor'] = '#621708'
    plt.rcParams['axes.titlesize'] = 24
    plt.rcParams['xtick.color'] = '#F6AA1C'
    plt.rcParams['ytick.color'] = '#F6AA1C'
    plt.grid(b=True, color="#AA280E")

    plt.plot(dev_y, dev_x, 'o', color= '#F6AA1C')
    plt.ylim(16, 20)
    plt.xlim(yesterday, now)

    plt.title('Temperatures by Time of Day', color= '#F6AA1C')
    plt.ylabel('Temperatures', color= '#F6AA1C')
    plt.xlabel('Time of Day', color= '#F6AA1C')

    plt.show()

    

    fig.savefig('static/temp.png')
   
    lines = ax.plot(dev_y, dev_x, color= '#F6AA1C')
    labelTooltip = plugins.LineLabelTooltip(lines[0], label='ylabel')
    plugins.connect(fig, labelTooltip)
    plt_html = fig_to_html(fig)


    return plt_html