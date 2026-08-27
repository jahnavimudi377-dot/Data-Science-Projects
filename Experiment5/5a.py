import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,25,30]
plt.plot(x,y)
plt.title("Line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.savefig("line-plot.png")
plt.savefig("line plot")
plt.show()