import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV data into a DataFrame
df = pd.read_csv('ex2_data.csv')

# Extract the data from the 'value' column
values = df['Value']

# Create a histogram
plt.hist(range(len(values)), bins=100, edgecolor='black', weights=values)

# Customize the plot
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Histogram of Values by Index')

# Display the histogram
plt.show()
