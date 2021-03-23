from model.databasetemp import get_temps, get_timestamps
import matplotlib as mpl 
mpl.use('Agg')
from matplotlib import pyplot as plt
from mpld3 import fig_to_html

def make_plot():
    fig = plt.figure()
    dev_x = get_temps()

    dev_y = get_timestamps()

    plt.plot(dev_y, dev_x)

    plt.title('Temperatures by Time of Day')
    plt.ylabel('Temperatures')
    plt.xlabel('Time of Day')

    plt.show()

    fig.savefig('static/temp.png')
    plt_html = fig_to_html(fig)
    return plt_html