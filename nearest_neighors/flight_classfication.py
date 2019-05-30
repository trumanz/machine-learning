import sys
import struct
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np


def aiportsCodeToInt(airports):
    rc = []
    for airport in airports:
        x = 'aa' + airport + 'aaa'
        y = struct.unpack('Q', x.encode())[0]
        print(y)
        rc.append(y)
    return rc

def flightDistance(a,b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    z = abs(a[2] - b[2])
    if z > 12*60:
        z = abs(24*60 - z)
    d = x + y + z
    print("cal distance with " + str(a) + "--" + str(b) + ":" + str(d))
    return x

def getSamePatternFlights(flights, minutes_delta_max):
    t1 = flights['departureTime'].min()
    t2 = flights['departureTime'].max()
    print(str(t1) + "==>" + str(t2))
    print(type(t1))
    x = (t2.date() - t1.date()).days + 1
    print(x)
    fs = flights[['departureAirport', 'arrivalAirport','dTime']]
    fs = fs.assign(da = lambda x: aiportsCodeToInt(x.departureAirport))
    fs = fs.assign(aa = lambda x: aiportsCodeToInt(x.arrivalAirport))
    fs = fs[['da', 'aa','dTime']]
    print(fs)
    nbrs = NearestNeighbors(x,metric=flightDistance)
    nbrs.fit(fs)

    distances,indices = nbrs.kneighbors(fs)
    print("distacnes")
    print(distances)
    print("indices")
    print(indices)




flights = pd.read_csv("small_flight.csv", parse_dates=['departureTime', 'arrivalTime'])
#print(flights)
header = list(flights.head(0))
care_columns = ['departureAirport', 'arrivalAirport','departureTime', 'arrivalTime']
for c in care_columns:
    header.remove(c)
care_columns.reverse()
for c in care_columns:
    header.insert(2, c)

flights = flights[header]
print(type(flights['departureTime']))
t1 = flights['departureTime'].min()
t2 = flights['departureTime'].max()
print(t1)
print(t2)
#2 weeks
flights = flights.query('departureTime> "2017-11-13 00:00:00" and departureTime <  "2017-11-20 00:00:00"')
flights = flights.sort_values(by=["departureAirport", "arrivalAirport", "departureTime"])

def timeOfDay(x):
    print(x)
    return x

flights = flights.assign(dTime = lambda x : pd.to_datetime(x['departureTime'], format='%Y-%m-%d %H:%M:%S').values.astype('datetime64[m]').astype('uint64')%(24*60))

getSamePatternFlights(flights, 1)

sys.exit(1)