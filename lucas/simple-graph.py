# making a simple graph with matplotlib

import matplotlib.pyplot as plt
import numpy

figure = plt.figure()

# graph title
figure.suptitle('Axis Here')

# 2 x 2 grid of axis
figure, ax_list = plt.subplots(2, 2)

# print graph when invoked from CLI
plt.show(figure)
