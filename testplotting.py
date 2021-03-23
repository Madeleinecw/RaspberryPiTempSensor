from model.databasetemp import get_temps, get_timestamps
import matplotlib as mpl 
mpl.use('Agg')
from matplotlib import pyplot as plt
from mpld3 import fig_to_html

def make_plot():
    fig = plt.figure()
    dev_x = get_temps()

    dev_y = get_timestamps()
    plt.rcParams['axes.facecolor'] = '#621708'
    plt.rcParams['axes.titlesize'] = 24
    plt.rcParams['xtick.color'] = '#F6AA1C'


    plt.plot(dev_y, dev_x, color= '#F6AA1C')

    plt.title('Temperatures by Time of Day', color= '#F6AA1C')
    plt.ylabel('Temperatures', color= '#F6AA1C')
    plt.xlabel('Time of Day', color= '#F6AA1C')

    plt.show()

    fig.savefig('static/temp.png')
    plt_html = fig_to_html(fig)
    return plt_html