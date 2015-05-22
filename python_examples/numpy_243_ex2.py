import numpy as np
import matplotlib.pyplot as plt

# Generating data
x, y = np.random.randn(2, 1000000)

# Computing the 2D histogram
img, xedges, yedges = np.histogram2d(x, y, bins=(20, 20))

# Preparing the axis mapping for 2D histogram in Matplotlib
extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]

fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Plotting the 2D data in hexagonal and rectangular
# format. 

# Getting desired color map
yarg = plt.cm.gist_yarg

# Plotting rectangular 2D histogram
ax1.imshow(img, extent=extent, interpolation='nearest', cmap=yarg, 
           origin='lower left')

# Plotting hexagonal 2D histrogram
ax2.hexbin(x, y, gridsize=20, cmap=yarg)

# Setting titles
ax1.set_title('Rectangular binning')
ax2.set_title('Hexagonal binning')

# Setting extent of plot area
ax1.set_xlim(-4,4)
ax1.set_ylim(-4,4)
ax2.set_xlim(-4,4)
ax2.set_ylim(-4,4)

# Setting aspect ratio to equal --> 1:1
ax1.set_aspect('equal')
ax2.set_aspect('equal')

# Saving figure
fig.savefig('binning.png')
