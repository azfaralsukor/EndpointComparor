import matplotlib.pyplot as plt

X = []
Y = []
Z = []

graph_data = open('data.csv', 'r').read()
lines = graph_data.split('\n')
for line in lines:
	if len(line) > 1:
		x, y, z = line.split(',')
		X.append(int(x))
		Y.append(int(y))
		Z.append(int(z))
plt.plot(X, Y, label="old")
plt.plot(X, Z, label="new")
plt.legend()
plt.show()