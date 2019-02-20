import requests
import re
import time
from subprocess import Popen
import csv

start_time = time.time()
server = 'http://127.0.0.1'
userkey = ''
headers = {'apikey': '', 'UserKey': userkey}

startid = 1
projectids = []
print("Starting test...")
print("Testing on address " + server, end="")

Popen('python compare_live_graph.py')
print(" with iteration of " + str(len(projectids)) + " times...")
for x in range(0, len(projectids)):
    print("ProjectId: " + str(projectids[x]))
    with requests.get(server + '/svc/api/project/getallv1/' + str(projectids[x]), headers=headers, stream=True) as v1:
        v1_time = re.search("'Elapsed': '(.*) ms'", str(v1.json())).group(1)
        resoponse = str(v1.json())

    with requests.get(server + '/svc/api/project/getallv2/' + str(projectids[x]), headers=headers, stream=True) as v2:
        v2_time = re.search("'Elapsed': '(.*) ms'", str(v2.json())).group(1)

    with requests.get(server + '/svc/api/project/getall/' + str(projectids[x]), headers=headers, stream=True) as v3:
        v3_time = re.search("'Elapsed': '(.*) ms'", str(v3.json())).group(1)

    file=open("compare_data.csv", "a+")
    file=file.write(str(len(resoponse)) + "," + v1_time + "," + v2_time + "," + v3_time + "," + str(projectids[x]) + "\n")

    with open('compare_data.csv', 'r') as f:
        data = [line for line in csv.reader(f)]
    data = sorted(data, key=lambda x: int(x[0]))
    with open('compare_data.csv', 'w', newline='') as f:
        csv.writer(f).writerows(data)

print("Done. Exiting...")
print("Elapsed time: " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
