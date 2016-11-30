from matplotlib import pyplot as plt


def bargraph(xList, yList):
	colors = ['r', 'g', 'b', 'k']
	for i in range(len(xList)):
		plt.bar(xList[i], yList[i], color=colors[i], align='center')

	plt.title('Epic Info')
	plt.ylabel('Y axis')
	plt.xlabel('X axis')

	plt.show()

x = [[5,8,10],[6,7,4]]
y = [[12,16,6],[12,16,6]]

bargraph(x,y)