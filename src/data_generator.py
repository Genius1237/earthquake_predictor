import numpy as np
import pandas as pd
from tqdm import tqdm

path = '../data/database.csv'
df = pd.read_csv(path)

print(df.shape)
equakes = []
for i in range(df.shape[0]):
    if df['Type'][i] == 'Earthquake':
        equakes.append((df['Latitude'][i],df['Longitude'][i],df['Magnitude'][i]))

lat_up = 90
lat_low = -90
long_up = 180
long_low = -180
scale = 10

k = 1
# Scaling factor
n_examples = 10000

d = np.zeros(((lat_up-lat_low)*scale,(long_up-long_low)*scale))

# (0,0) in the array is (90,-180) in terms of coordinates

print("No. of earthquakes: {}".format(len(equakes)))

ii = np.array([[i for j in range((long_up-long_low)*scale)] for i in range((lat_up-lat_low)*scale)])
ij = np.array([[j for j in range((long_up-long_low)*scale)] for i in range((lat_up-lat_low)*scale)])

for e in tqdm(equakes[:n_examples]):
    index_i = lat_up*scale - int(e[1]*scale)
    index_j = long_up*scale - int(e[2]*scale)

    r_sq = (ii-index_i)**2 + (ij-index_j)**2

    d += k*e[0]/r_sq
    
    '''
    for i in range(18000):
        for j in range(36000):
            r_square = (i-index_i)**2 + (j-index_j)**2 
            d[i][j] += k*e[0]/r_square
    '''

d = np.nan_to_num(d)
d[d>10000] = 0
'''
t = d.reshape(-1)
t.sort()
t = t[::-1]
print(t[:100])
'''
np.save('lat_long',d)