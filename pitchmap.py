import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axis
fig, ax = plt.subplots(figsize=(22, 10))

# Define the lengths of each region (in meters)
lengths = [2, 2, 2, 2]
colors = ['#FFFF99', '#FFFF66', '#99FF99', '#FF6666']
labels = ['YORKER', 'FULL', 'GOOD', 'SHORT']

# Starting point for the regions
start = 0

# Draw the pitch
for i, (length, color, label) in enumerate(zip(lengths, colors, labels)):
    rect = patches.Rectangle((start, 0), length, 10, linewidth=1, edgecolor='white', facecolor=color)
    ax.add_patch(rect)
    ax.text(start + length / 2, 5, label, color='white', fontsize=12, ha='center', va='center')
    start += length

# Add lines for the meter markings
for meter in range(0, 9, 2):
    ax.axvline(meter, color='white', linewidth=1)
    ax.text(meter, 11, f'{meter}M', color='white', fontsize=12, ha='center')

# Add the stumps at the end
ax.axhline(0, color='white', linewidth=3)
ax.axhline(10, color='white', linewidth=3)

# Set limits and remove axes
ax.set_xlim(0, 8)
ax.set_ylim(0, 12)
ax.axis('off')

# Show the plot
plt.show()
