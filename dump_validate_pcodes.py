import pluscodes as pcodes
from shapely.geometry import Point, Polygon
import json

import matplotlib.pyplot as plt


def check_pcode(pcode):
    point = pcodes.decode(pcode)
    return point.lnglat()


coords = json.load(open('nepaldistricts_acesmndr.json'))
coords = coords['features'][24]['geometry']['coordinates'][0]
#BHAKTAPUR 22, KATHMANDU 24, LALITPUR 26
poly = Polygon(coords)


with open('KATHMANDU', 'r') as f: # <- Original DUMP file
    lines = f.read().splitlines()

fw = open('KATHMANDU_True.csv', 'w') # <- Clipped DUMP file
for pcode in lines:
    x = check_pcode(pcode)
    x = Point(x)

    if x.within(poly) == True:
        fw.write(pcode+","+str(x.x)+","+str(x.y))
        fw.write('\n')

fw.close()
