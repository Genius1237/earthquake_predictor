import argparse
import numpy as np

lat_up = 90
lat_low = -90
long_up = 180
long_low = -180
scale = 10

parser = argparse.ArgumentParser(description='Return badness value for a point on a map')
parser.add_argument('--lat', dest='lat', type=float)
parser.add_argument('--long', dest='long', type=float)

args = parser.parse_args()
lat = args.lat
long = args.long

d = np.load('lat_long.npy')

index_i = lat_up*scale - int(lat*scale)
index_j = long_up*scale - int(long*scale)

print(d[index_i][index_j])