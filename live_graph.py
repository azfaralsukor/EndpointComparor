import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
sp = fig.add_subplot(1,1,1)

def animate(i):
	graph_data = open('data.csv', 'r').read()
	lines = graph_data.split('\n')
	xs = []
	ys = []
	zs = []
	for line in lines:
		if len(line) > 1:
			x, y, z = line.split(',')
			xs.append(int(x))
			ys.append(int(y))
			zs.append(int(z))
	sp.clear()
	sp.plot(xs, ys, label="old")
	sp.plot(xs, zs, label="new")
	plt.xlabel('Response Size (10 MB)')
	plt.ylabel('Time Taken (ms)')
	sp.legend()

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
