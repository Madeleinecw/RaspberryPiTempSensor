# from model.databasetemp import get_temps, get_timestamps
import matplotlib as mpl 
mpl.use('Agg')
from matplotlib import pyplot as plt
from mpld3 import fig_to_html, plugins
from matplotlib.lines import Line2D

def make_plot_from_range(temperatureHistory: list):

    css = """
    .mpld3-tooltip {
    background-color: white; 
    color: #AA280E }
    """ 
    fig, ax = plt.subplots()

    x = []
    y = []

    for item in temperatureHistory:
        x.append(item[0])
        y.append(item[1])

   
    
    plt.rcParams['axes.facecolor'] = '#621708'
    plt.rcParams['axes.titlesize'] = 24


    plt.plot(y, x, color= '#F6AA1C')

    plt.title('The Times YOU selected:', color= '#F6AA1C')
    plt.ylabel('Temperatures', color= '#F6AA1C')
    plt.xlabel('Time of Day', color= '#F6AA1C')
    plt.grid(b=True, color='#AA280E')


    plt.show()

    lines = Line2D(y, x, color= '#F6AA1C', lw=1, marker='.')
    ax.add_line(lines)



    label = [str(i) for i in x]

    labelTooltip = plugins.PointHTMLTooltip(lines, label, css=css)
    plugins.connect(fig, labelTooltip)

    fig.savefig('static/rangetemp.png')
    plt_html = fig_to_html(fig, figid='selected-graph-generated')
    return plt_html

