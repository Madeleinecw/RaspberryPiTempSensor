# from model.databasetemp import get_temps, get_timestamps
import matplotlib as mpl 
mpl.use('Agg')
from matplotlib import pyplot as plt
from mpld3 import fig_to_html

def make_plot_from_range(temperatureHistory: list):

    x = []
    y = []

    for item in temperatureHistory:
        x.append(item[0])
        y.append(item[1])

    fig = plt.figure()
   
    
    plt.rcParams['axes.facecolor'] = '#621708'
    plt.rcParams['xtick.color'] = '#F6AA1C'
    plt.rcParams['axes.titlesize'] = 24


    plt.plot(y, x, color= '#F6AA1C')

    plt.title('The Times YOU selected:', color= '#F6AA1C')
    plt.ylabel('Temperatures', color= '#F6AA1C')
    plt.xlabel('Time of Day', color= '#F6AA1C')

    plt.show()

    fig.savefig('static/rangetemp.png')
    plt_html = fig_to_html(fig)
    return plt_html

