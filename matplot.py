import matplotlib.pyplot as plt

# print(matplotlib.__version__) Checking Matplotlib Version

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.ylabel("y number")
plt.xlabel("x number")

# x label
plt.xlabel("x-axis")

#y label
plt.ylabel("y axis")

# chart title
plt.title("Practice chart")

# To plot the marker oon point
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "o", label="marker")

# to plot the star on point
plt.plot([3, 4, 5, 6], [3, 4, 5, 9], "*" , label="star points")

# lineStyle of the graph
plt.plot([2,3,6,7,8,9],[9,8,7,6,5,4], linestyle="dotted" , label="linestyle dotted")

# linestyle of  the graph 
plt.plot([9,8,7,6,5,4],[2,3,6,7,8,9], linestyle="dashed" , label="linestyle dashed")

# colour of line

plt.plot([2,3,4,5,6,7],[2,3,4,5,6,7], color = "r", linewidth = "5",  label="color and width is 5")


# add grid lines to the plot
plt.grid()

# one one window multiple graphes
#plt.subplot(1, 2, 1)

#Scatter plots
plt.scatter([50, 60, 70, 80, 90, 100, 101], [50, 60, 70, 80, 90, 100, 101], color="black")

#colormap in the drawing by including the plt.colorbar() statement:
plt.colorbar()

plt.legend(loc="upper right", shadow= True)
plt.show()