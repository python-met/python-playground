## making a simple graph with matplotlib

# matplotlib.pyplot always aliased as plt
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# define x and y with lists
# x = hours
# y = mb
ne_time = [1,2,3,4,5,6,7,8,9]
ne_press = [908, 860, 1083, 1041, 1000, 999, 880, 897, 978]

ks_time = [1,2,3,4,5,6,7,8,9]
ks_press = [910, 968, 1099, 1051, 1041, 1000, 890, 894, 977]

# plot x, x2, y, y2
plt.plot(ks_time, ks_press, label='Kansas')
plt.plot(ne_time, ne_press, label='Nebraska')

# label axis, title
# plt.xlabel('hours')
# format x axis as hours
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%d hr'))
# plt.ylabel('mb')
plt.title('Nebraska & Kansas Pressure')
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d mb'))

#display graph and legend
plt.legend()
plt.show()
