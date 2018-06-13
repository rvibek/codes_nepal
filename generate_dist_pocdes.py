import pluscodes as pcode
import numpy as np
import json

#ultimate loop

districts = json.load(open('nepaldistrictbound_acesmndr.json'))

for i,x in enumerate(districts):

    district = (x['district'])
    seldistrict = districts[i]

    nelat = seldistrict['bounds']['northeast']['lat']
    nelng = seldistrict['bounds']['northeast']['lng']
    swlat = seldistrict['bounds']['southwest']['lat']
    swlng = seldistrict['bounds']['southwest']['lng']

    print(swlat, nelat, swlng, nelng)




    dist = seldistrict['district']




    c10 = 0.000125  # 14*14 s
    # c11 = 0.000024  # 3*3
    c = c10

    f = open(dist, "w")
    for i in np.arange(swlat, nelat, c):
        for j in np.arange(swlng, nelng, c):
            # print(i,k)
            f.write(pcode.encode(i, j, 10))
            # print(i, j)
            f.write('\n')

    f.close()
