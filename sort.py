import csv
from operator import itemgetter

with open('data.csv', 'r') as f:
    data = [line for line in csv.reader(f)]

# new data here

data = sorted(data, key=lambda x:int(x[2])) 

with open('data.csv', 'w', newline='') as f:
    csv.writer(f).writerows(data)