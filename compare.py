import requests
import re
import time
from subprocess import Popen
import csv

start_time = time.time()
server = 'http://127.0.0.1'
userkey = '1.ef5b2625-705d-4c0a-99a3-bb521746c4d3'
headers = {'apikey': 'SuFH7x5V2v', 'UserKey': userkey}

startid = 1
projectids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 229, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 283, 291, 292, 294, 295, 309, 312, 313, 314, 317, 336, 338, 339, 340, 341, 343, 344, 345, 346, 347, 349, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385]
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
