# This is a simple example of a line plot using matplotlib
import matplotlib.pyplot as plt

# Define data points
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a basic line plot
plt.scatter(x, y, color='blue')

# Label the axes
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title to the plot
plt.title('Basic line plot')

# Display the plot
plt.show()