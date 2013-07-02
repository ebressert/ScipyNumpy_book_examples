import numpy as np
from scipy.cluster import vq
import matplotlib.pyplot as plt

# Creating data
c1 = np.random.randn(100, 2) + 5
c2 = np.random.randn(30, 2) - 5
c3 = np.random.randn(50, 2)

# Pooling all the data into one 150 x 2 array
data = np.vstack([c1, c2, c3])

# Calculating the cluster centriods and variance
# from kmeans
centroids, variance = vq.kmeans(data, 3)

# The identified variable contains the information
# we need to separate the points in clusters
# based on the vq function.
identified, distance = vq.vq(data, centroids)

# Retrieving coordinates for points in each vq
# identified core
vqc1 = data[identified == 0]
vqc2 = data[identified == 1]
vqc3 = data[identified == 2]

#Setting up plot details
x1, x2 = -10, 10
y1, y2 = -10, 10

fig = plt.figure()
fig.subplots_adjust(hspace=0.1, wspace=0.1)

ax1 = fig.add_subplot(121, aspect='equal')
ax1.scatter(c1[:, 0], c1[:, 1], lw=0.5, color='#00CC00')
ax1.scatter(c2[:, 0], c2[:, 1], lw=0.5, color='#028E9B')
ax1.scatter(c3[:, 0], c3[:, 1], lw=0.5, color='#FF7800')
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
ax1.set_xlim(x1, x2)
ax1.set_ylim(y1, y2)
ax1.text(-9, 8, 'Original')

ax2 = fig.add_subplot(122, aspect='equal')
ax2.scatter(vqc1[:, 0], vqc1[:, 1], lw=0.5, color='#00CC00')
ax2.scatter(vqc2[:, 0], vqc2[:, 1], lw=0.5, color='#028E9B')
ax2.scatter(vqc3[:, 0], vqc3[:, 1], lw=0.5, color='#FF7800')
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
ax2.set_xlim(x1, x2)
ax2.set_ylim(y1, y2)
ax2.text(-9, 8, 'VQ identified')

fig.savefig('scipy_351_ex1.pdf', bbox_inches='tight')
