import json

df = json.load(open('nepaldistricts_acesmndr.json'))


def districtname(i):
    name = df['features'][i]['properties']['DISTRICT']
    return name

def nebound(i):
    coords = df['features'][i]['geometry']['coordinates'][0]
    return (max(coord[1] for coord in coords), max(coord[0] for coord in coords))

def swbound(i):
    coords = df['features'][i]['geometry']['coordinates'][0]
    return (min(coord[1] for coord in coords), min(coord[0] for coord in coords))


# Generate northeast and southwest coordinates for each district 
for i in range(len(df['features'])):
    print(districtname(i), nebound(i), swbound(i))
