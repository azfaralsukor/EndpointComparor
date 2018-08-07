import requests
import re
import time

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
        print('Result: Identical')
    else:
        print('Result: NOT IDENTICAL')

else:
    d_a=[]
    if not failed:
        print(" with iteration of "+str(totalprojectcount-startid)+" times...")
        for x in range(startid,totalprojectcount):
            print("ProjectId: "+str(x), end="")
            with requests.get(server+'/svc/api/project/getallv1/'+str(x), headers=headers, stream=True) as o:
                f = re.sub('Elapsed.*? ms','',str(o.json()), flags=re.DOTALL)
                
            with requests.get(server+'/svc/api/project/getall/'+str(x), headers=headers, stream=True) as n:
                s = re.sub('Elapsed.*? ms','',str(n.json()), flags=re.DOTALL)

            if f == s:
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
                    f = re.sub('Elapsed.*? ms','',str(o.json()), flags=re.DOTALL)
                    
                with requests.get(server+'/svc/api/project/getall/'+str(failed[x]), headers=headers, stream=True) as n:
                    s = re.sub('Elapsed.*? ms','',str(n.json()), flags=re.DOTALL)

                if f == s:
                    print(' --- Identical')
                else:
                    d_a.append(failed[x])
                    print(' --- NOT IDENTICAL')

        print("Failed ProjectIds: ", end="")
        for x in d_a:
          print(x, end=" ")
        print("\n"+str(len(d_a))+" out of "+str(len(failed))+" projects failed. Your new endpoint is "+str((len(failed)-len(d_a))/(len(failed))*100)+"% accurate")
print("Done. Exiting...")
print("Elapsed time: "+time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))