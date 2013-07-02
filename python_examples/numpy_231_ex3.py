import numpy as np
# example.txt file looks like the following
#
# XR21 32.789 1
# XR22 33.091 2

table = np.loadtxt('example.txt',
		dtype={'names': ('ID', 'Result', 'Type'),
		'formats': ('S4', 'f4', 'i2')})

# array([('XR21', 32.78900146484375, 1),
#        ('XR22', 33.090999603271484, 2)],
#  dtype=[('ID', '|S4'), ('Result', '<f4'), ('Type', '<i2')])
