import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Step 1: Read the Excel file into a DataFrame
df = pd.read_excel('sample.xlsx')

# Replace 'Unnamed' column names with an empty string
df.columns = df.columns.str.replace('Unnamed:.*', '', regex=True)

# Replace NaN values with an empty string
df = df.fillna('')

# Extract the first row's content and remove it from the DataFrame
# title = df.iloc[0, 0]
# df = df.iloc[1:]

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Add the title
# plt.title(title)

# Remove the box around the plot
ax.axis('off')

# Create a table from the DataFrame and add it to the subplots
table = plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)

# Auto set the column widths
table.auto_set_column_width(col=list(range(len(df.columns))))

# Save the figure as a PNG image
plt.savefig('output.jpg', bbox_inches='tight', dpi=300)

