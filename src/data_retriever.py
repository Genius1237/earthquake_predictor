import argparse
import numpy as np
import sys

lat_up = 90
lat_low = -90
long_up = 180
long_low = -180
scale = 10

parser = argparse.ArgumentParser(description='Return badness value for a point on a map')
parser.add_argument('--lat', dest='lat', type=float)
parser.add_argument('--long', dest='long', type=float)
parser.add_argument('--input', dest='input')

args = parser.parse_args()
lat = args.lat
long = args.long

d = np.load(args.input)

index_i = lat_up*scale - int(lat*scale)
index_j = long_up*scale - int(long*scale)
result = d[index_i][index_j]
print(abs(result) * 100)
sys.stdout.flush()