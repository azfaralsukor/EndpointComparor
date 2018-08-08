import requests
import re
import time
import os
from subprocess import Popen
import csv
from operator import itemgetter

start_time = time.time()
server = 'http://127.0.0.1'
userkey = '203.28d40838-f51f-4a78-9dbe-26ff07f74cb9'
headers = {'apikey': 'SuFH7x5V2v', 'UserKey': userkey}
totalprojectcount = 365 # SELECT MAX(ProjectId) FROM ProjectTbl; +1
id = 0
startid = 1
failed = []

print("Starting test...")
print("Testing on address "+server, end="")

if id != 0:
    x = id
    print(" for ProjectId: "+str(x))
    with requests.get(server+'/svc/api/project/getallv1/'+str(x), headers=headers, stream=True) as o:
        f = re.sub('Elapsed.*? ms','',str(o.json()), flags=re.DOTALL)
        
    with requests.get(server+'/svc/api/project/getall/'+str(x), headers=headers, stream=True) as n:
        s = re.sub('Elapsed.*? ms','',str(n.json()), flags=re.DOTALL)

    print(f)
    print(s)

    if f == s:
        print(o.json())
        print('Result: Identical')
    else:
        print('Result: NOT IDENTICAL')

else:
    d_a=[]
    Popen('python live_graph.py')
    if not failed:
        print(" with iteration of "+str(totalprojectcount-startid)+" times...")
        for x in range(startid,totalprojectcount):
            print("ProjectId: "+str(x), end="")
            with requests.get(server+'/svc/api/project/getallv1/'+str(x), headers=headers, stream=True) as o:
                f_time = re.search("'Elapsed': '(.*) ms'", str(o.json())).group(1)
                f = re.sub('Elapsed.*? ms','',str(o.json()), flags=re.DOTALL)
                
            with requests.get(server+'/svc/api/project/getall/'+str(x), headers=headers, stream=True) as n:
                s_time = re.search("'Elapsed': '(.*) ms'", str(n.json())).group(1)
                s = re.sub('Elapsed.*? ms','',str(n.json()), flags=re.DOTALL)

            if f == s:
                file=open("data.csv", "a+")
                file=file.write(str(len(f))+","+f_time+","+s_time+"\n")
                with open('data.csv', 'r') as f:
                    data = [line for line in csv.reader(f)]
                data = sorted(data, key=lambda x:int(x[0])) 
                with open('data.csv', 'w', newline='') as f:
                    csv.writer(f).writerows(data)
                print(' --- Identical')
            else:
                d_a.append(x)
                print(' --- NOT IDENTICAL')

        print("Failed ProjectIds: ", end="")
        for x in d_a:
          print(x, end=" ")
        print("\n"+str(len(d_a))+" out of "+str(totalprojectcount-startid)+" projects failed. Your new endpoint is "+str((totalprojectcount-startid-len(d_a))/(totalprojectcount-startid)*100)+"% accurate")
    else:
        print(" with iteration of "+str(len(failed))+" times...")
        for x in range(0,len(failed)):
                print("ProjectId: "+str(failed[x]), end="")
                with requests.get(server+'/svc/api/project/getallv1/'+str(failed[x]), headers=headers, stream=True) as o:
                    f_time = re.search("'Elapsed': '(.*) ms'", str(o.json())).group(1)
                    f = re.sub('Elapsed.*? ms','',str(o.json()), flags=re.DOTALL)
                    
                with requests.get(server+'/svc/api/project/getall/'+str(failed[x]), headers=headers, stream=True) as n:
                    s_time = re.search("'Elapsed': '(.*) ms'", str(n.json())).group(1)
                    s = re.sub('Elapsed.*? ms','',str(n.json()), flags=re.DOTALL)

                if f == s:
                    file=open("data.csv", "a+")
                    file=file.write(str(len(f))+","+f_time+","+s_time+"\n")
                    with open('data.csv', 'r') as f:
                        data = [line for line in csv.reader(f)]
                    data = sorted(data, key=lambda x:int(x[0])) 
                    with open('data.csv', 'w', newline='') as f:
                        csv.writer(f).writerows(data)
                    print(' --- Identical')
                else:
                    d_a.append(failed[x])
                    print(' --- NOT IDENTICAL')

        print("Failed ProjectIds: ", end="")
        for x in d_a:
          print(x, end=" ")
        print("\n"+str(len(d_a))+" out of "+str(len(failed))+" projects failed. Your new endpoint is "+str((len(failed)-len(d_a))/(len(failed))*100)+"% accurate")

Popen('python result_graph.py')
print("Done. Exiting...")
print("Elapsed time: "+time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
