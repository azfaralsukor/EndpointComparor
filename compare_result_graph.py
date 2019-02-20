import matplotlib.pyplot as plt

X = []
Y = []
Z = []
A = []

graph_data = open('compare_data.csv', 'r').read()
lines = graph_data.split('\n')
for line in lines:
	if len(line) > 1:
		x, y, z, a, i = line.split(',')
		X.append(int(x))
		Y.append(int(y))
		Z.append(int(z))
		A.append(int(a))
plt.plot(X, Y, label="v1")
plt.plot(X, Z, label="v2")
plt.plot(X, A, label="v3")
plt.xlabel('Response Size (10 MB)')
plt.ylabel('Time Taken (ms)')
plt.legend()
plt.show()