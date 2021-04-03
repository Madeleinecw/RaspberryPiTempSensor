from utils.temperatures_database_service import get_all_temperatures, get_all_outside_temps, get_all_feels_like_temps, get_all_timestamps
import numpy as np
from bokeh.plotting import figure, output_notebook, show, output_file
from bokeh.io import export_png, curdoc
from bokeh.themes import Theme
from bokeh.models.tools import HoverTool
from bokeh.models import Legend, LegendItem
from bokeh.embed import json_item
curdoc().theme = Theme(filename="themes/redTheme.yml")

def get_bokeh_graph_from_range(temperaturesHistory: list):

    temperature = []
    outsideTemperature = []
    feelsLikeTemperature = []
    timestamp = []

    for entry in temperaturesHistory:
        temperature.append(float(entry[0]))
        outsideTemperature.append(float(entry[1]))
        feelsLikeTemperature.append(float(entry[2]))
        timestamp.append(entry[3])

    output_notebook()

    p = figure(title='Temperatures', x_axis_type='datetime', y_axis_label='degrees celsius')

    p.add_tools(HoverTool(tooltips = [('Time', '$x{%F %T}'), ('Temp', '$y''°C')],
                        formatters = {'$x' : 'datetime'} ))

    p.xaxis.major_tick_line_color = '#878E88'
    p.xaxis.major_tick_line_width = 3
    p.xaxis.minor_tick_line_color = 'white'
    p.yaxis.major_tick_line_color = '#878E88'
    p.yaxis.major_tick_line_width = 3
    p.yaxis.minor_tick_line_color = 'white'
    p.xaxis.major_label_text_color = '#F6AA1C'
    p.yaxis.major_label_text_color = '#F6AA1C'

    r = p.multi_line(xs=[time, time, time], ys=[feels, outside, alltemp], color=['blue', '#878E88', '#F6AA1C'],  line_width=2)

    legend = Legend(items=[
        LegendItem(label='Feels Like', renderers=[r], index=0),
        LegendItem(label='Outside', renderers=[r], index=1),
        LegendItem(label='Inside', renderers=[r], index=2)
    ])

    p.add_layout(legend)
    p.legend.background_fill_color = '#2F2F2F'
    p.legend.label_text_color = '#F6AA1C'

    return json_item(p, 'myplot')