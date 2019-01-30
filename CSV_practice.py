import pprint

with open('flight.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
            k, v = line.title().strip().split(',')
            flights[k] = v
    
pprint.pprint (flights)




