## making a simple graph with matplotlib

# matplotlib.pyplot always aliased as plt
import matplotlib.pyplot as plt

# define x and y with lists
x = [1,2,3,4,5,6,7,8,9]
y = [1,4,9,9,5,4,3,4,6]

x2 = [1,5,6]
y2 = [2,4,4]

# plot x, x2, y, y2
plt.plot(x, y, label='1st series')
plt.plot(x2, y2, label='2nd series')

# set labels
plt.xlabel('time')
plt.ylabel('pressure')

#label axis, title
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('title \nSub-title')

#display graph and legend
plt.legend()
plt.show()
