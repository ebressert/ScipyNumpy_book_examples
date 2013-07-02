import numpy as np

def temp_and_rain(lat ,min_temp=10, max_temp=10, points=1000):
    # Extremely over simplified temperature dependence
    # latitude.

    lat = np.abs(lat)
    temp = np.random.normal(scale=5, size=lat.shape) + lat / 2
    temp = np.abs(temp)

    # Randomizer, we'll never know if the rain is
    # correlated with 
    tobe_ornot = np.random.randint(0, high=2)

    if tobe_ornot:
        rain = np.random.normal(scale=3, size=lat.shape) + temp * 2

    else:
        rain = np.random.uniform(high=100, size=lat.shape)

    return temp, rain

lat = np.random.uniform(low=-90, high=90, size=100)

temp, rain = temp_and_rain(lat)

result = np.corrcoef(temp, y=rain)

# Showing evidence of correlation
# array([[ 1.        ,  0.99547777],
#        [ 0.99547777,  1.        ]])

# Showing no evidence of correlation
# array([[ 1.        ,  0.13876381],
#        [ 0.13876381,  1.        ]])










