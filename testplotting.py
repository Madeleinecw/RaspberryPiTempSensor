from testdb import get_temps, get_timestamps
import matplotlib as mpl 
mpl.use('Agg')
from matplotlib import pyplot as plt

fig = plt.figure()
dev_x = get_temps()

dev_y = get_timestamps()

plt.plot(dev_y, dev_x)

plt.title('Temperatures by Time of Day')
plt.ylabel('Temperatures')
plt.xlabel('Time of Day')

plt.show()

fig.savefig('temp.png')

