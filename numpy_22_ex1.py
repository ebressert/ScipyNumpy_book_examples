import numpy as np
import matplotlib.pyplot as plt

# First let us create an image
img1 = np.zeros((20, 20)) + 3
img1[4:-4, 4:-4] = 6
img1[7:-7, 7:-7] = 9
# See subplot A

# Let's filter out all values larger than 2 and less than 6
index1 = img1 > 2
index2 = img1 < 6
compound_index = index1 & index2

# The compound statement can alternatively be written as
compound_index = (img1 > 3) & (img1 < 7)
img2 = np.copy(img1)
img2[compound_index] = 0
# See plot B

# Making the boolean arrays even more complex we can do
index3 = img1 == 9
index4 = (index1 & index2) | index3
img3 = np.copy(img1)
img3[index4] = 0
# See subplot C

fig = plt.figure(313, figsize=(6, 6))
fig.subplots_adjust(hspace=None, wspace=None)
ax1 = fig.add_subplot(131)
ax1.imshow(img1, origin='lower left', interpolation='nearest',
           vmin=0, vmax=10, cmap=plt.cm.Greens)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
ax1.set_title('Plot A')

ax2 = fig.add_subplot(132)
ax2.imshow(img2, origin='lower left', interpolation='nearest',
           vmin=0, vmax=10, cmap=plt.cm.Greens)
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
ax2.set_title('Plot B')

ax3 = fig.add_subplot(133)
ax3.imshow(img3, origin='lower left', interpolation='nearest',
           vmin=0, vmax=10, cmap=plt.cm.Greens)
ax3.xaxis.set_visible(False)
ax3.yaxis.set_visible(False)
ax3.set_title('Plot C')
fig.savefig('ch212_f01.pdf', bbox_inches='tight')
plt.close(fig)
