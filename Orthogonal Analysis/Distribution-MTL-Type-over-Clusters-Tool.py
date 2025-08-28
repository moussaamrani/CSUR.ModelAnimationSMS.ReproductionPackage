import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('CORPUS-Final.csv')

# ✅ Merge META into MP
data["MTL Type"] = data["MTL Type"].replace("MP", "META")

# Targets
target1 = data["MTL Type"]
target2 = data["Unnamed: 12"]

# Arrays with categorical variables
MTLtype = ['GBT','META','GPPL','GPML','LOGIC','ALGEBRAIC']
level = ['','','','','','','','']  # Placeholder for second plot
MTLCluster = ['TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER','AltaRica']

# Initialize counters for MTL types
MTLtype_count_dict = {mt: [0]*len(MTLCluster) for mt in MTLtype}

# Initialize second plot counts (level_count)
level_count = [[0]*len(MTLCluster) for _ in range(len(level))]

# Count occurrences
for i in range(len(target1)):
    mt_type = target1[i]
    cluster = target2[i]
    if mt_type in MTLtype and cluster in MTLCluster:
        MTLtype_count_dict[mt_type][MTLCluster.index(cluster)] += 1

# Convert dictionary to list of lists
MTLtype_count = [MTLtype_count_dict[mt] for mt in MTLtype]

# Create DataFrames
df1 = pd.DataFrame(MTLtype_count, columns=MTLCluster, index=MTLtype)
df2 = pd.DataFrame(level_count, columns=MTLCluster, index=level)

# ============================
# Create figure with two subplots
# ============================
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, constrained_layout=True, sharex=True, figsize=(11,6.5))

# First scatter plot - MTL types
dfu1 = df1.unstack().reset_index()
dfu1.columns = list("XYS")
dfu1["S"] *= 400
a1.scatter(x="X", y="Y", s="S", data=dfu1, color='w', linestyle='solid', edgecolors='black', linewidth=2)
a1.margins(.1)

# Second scatter plot - TOOL clusters (level_count)
df2_plot_data = []
for i, col in enumerate(df2.columns):
    for j, idx in enumerate(df2.index):
        df2_plot_data.append({'X': col, 'Y': idx, 'S': df2.iloc[j, i] * 400})
dfu2 = pd.DataFrame(df2_plot_data)
a2.scatter(x="X", y="Y", s="S", data=dfu2, color='w', linestyle='solid', edgecolors='#000000', linewidth=2)
a2.margins(.1)

# ============================
# Annotate first plot
# ============================
for i, mt in enumerate(MTLtype):
    for j, cluster in enumerate(MTLCluster):
        text = str(MTLtype_count[i][j]) if MTLtype_count[i][j] != 0 else " "
        a1.annotate(text=text, xy=(cluster, mt), ha='center', va='center', color='black', size=14)

# Annotate second plot
for i, lvl in enumerate(level):
    for j, cluster in enumerate(MTLCluster):
        text = str(level_count[i][j]) if level_count[i][j] != 0 else " "
        a2.annotate(text=text, xy=(cluster, lvl), ha='center', va='center', color='black', size=14)

# Labels and styling
a1.set_ylabel('MTL Type', size=16, weight="bold", color="black")
a2.set_ylabel('', size=16, weight="bold", color="black")
a1.set_xlabel('')
a2.set_xlabel('TOOL Cluster', size=18, weight="bold", color='black')
a1.tick_params(labelsize=12)
a2.tick_params(labelsize=12, rotation=30)
a1.grid(ls='dotted', color='black')
a2.grid(ls='dotted', color='black')

# Show and save figure
plt.tight_layout()
fig.set_size_inches(6.5, 7.5)
plt.show()
fig.savefig('MTL-Type-Clusters-Tool-AltaRica.pdf', dpi=200, transparent=True)

# Print total counts including META as MP
print("Total MTL counts:", sum([sum(MTLtype_count_dict[mt]) for mt in MTLtype]))
