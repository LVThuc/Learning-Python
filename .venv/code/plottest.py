# This is a simple example of a line plot using matplotlib
import matplotlib.pyplot as plt
import os  # Import the os module

# Define data points
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot with blue color for the scatter points
plt.scatter(x, y, color='blue')

# Label the axes
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title to the plot
plt.title('Basic line plot')

# Define the directory and filename
output_dir = 'output'
output_file = 'scatter_plot.png'

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

# Save the plot as a PNG file in the specified directory
output_path = os.path.join(output_dir, output_file)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved plot to: {output_path}")

# Display the plot
plt.show()