from model.databasetemp import get_temps, get_timestamps
from bokeh.plotting import figure, output_file, show
from bokeh.io import export_png

yget = get_temps()
xget = get_timestamps()

x = []
y = []

for i in xget:
    x.append(i[0])

for i in yget:
    y.append(float(i[0]))

output_file('templates/lines.html')

p = figure(title='line example', x_axis_type='datetime', y_axis_label='y')

# print(x)
print(type(y[0]))
# print(xget)

p.line(x, y, legend_label="Temp.", line_width=2)

show(p)
