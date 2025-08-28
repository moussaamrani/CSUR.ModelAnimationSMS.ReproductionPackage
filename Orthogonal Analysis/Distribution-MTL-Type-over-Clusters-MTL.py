import pandas as pd 
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('CORPUS-Final.csv')

# ✅ Merge META into MP
data["MTL Type"] = data["MTL Type"].replace("MP", "META")

# Arrays with categorical variables
MTLtype = ['GBT','META','GPPL','GPML','LOGIC','ALGEBRAIC']  # MP now includes META
TOOLCluster = ['TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER'] 
MTLCluster = ['FSM','REWRITE','KERMETA','PN','XTEND/JAVA','B','VARIOUS','OTHER']

# Initialize counters for MTL types
MTLtype_count_dict = {mt: [0]*len(MTLCluster) for mt in MTLtype}

# Initialize counters for TOOL clusters
TOOLCluster_count = [[0]*len(MTLCluster) for _ in range(len(TOOLCluster))]

# Targets
target1 = data["MTL Type"]
target2 = data["CLUSTER"]

# Count occurrences for MTL types over MTL clusters
for i in range(len(target1)):
    mt_type = target1[i]
    cluster = target2[i]
    if mt_type in MTLtype and cluster in MTLCluster:
        MTLtype_count_dict[mt_type][MTLCluster.index(cluster)] += 1

# Convert dictionary to list of lists
MTLtype_count = [MTLtype_count_dict[mt] for mt in MTLtype]

# Create DataFrames
df1 = pd.DataFrame(MTLtype_count, columns=MTLCluster, index=MTLtype)
df2 = pd.DataFrame(TOOLCluster_count, columns=MTLCluster, index=TOOLCluster)

# ============================
# Plotting
# ============================
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, constrained_layout=True, sharex=True, figsize=(11,6.5))

# First scatter plot (MTL types)
dfu1 = df1.unstack().reset_index()
dfu1.columns = list("XYS")
dfu1["S"] *= 400
a1.scatter(x="X", y="Y", s="S", data=dfu1, color='w', linestyle='solid', edgecolors='black', linewidth=2)
a1.margins(.1)

# Second scatter plot (TOOL clusters)
dfu2 = df2.unstack().reset_index()
dfu2.columns = list("XYS")
dfu2["S"] *= 400
a2.scatter(x="X", y="Y", s="S", data=dfu2, color='w', linestyle='solid', edgecolors='black', linewidth=2)
a2.margins(.1)

# ============================
# Annotate first plot
# ============================
for i, mt in enumerate(MTLtype):
    for j, cluster in enumerate(MTLCluster):
        count = MTLtype_count[i][j]
        text = str(count) if count != 0 else " "
        a1.annotate(text, xy=(cluster, mt), ha='center', va='center', color='black', size=14)

# Annotate second plot
for i, tool in enumerate(TOOLCluster):
    for j, cluster in enumerate(MTLCluster):
        count = TOOLCluster_count[i][j]
        text = str(count) if count != 0 else " "
        a2.annotate(text, xy=(cluster, tool), ha='center', va='center', color='black', size=14)

# ============================
# Labels and styling
# ============================
a1.set_ylabel('MTL Type', size=16, weight="bold", color="black")
a2.set_ylabel('TOOL Cluster', size=16, weight="bold", color="black")
a1.set_xlabel('')
a2.set_xlabel('MTL Cluster', size=16, weight="bold", color='black')
a1.tick_params(labelsize=12)
a2.tick_params(labelsize=12, rotation=30)
a1.grid(ls='dotted', color='black')
a2.grid(ls='dotted', color='black')

# Show and save figure
plt.tight_layout()
fig.set_size_inches(6.5, 7.5)
plt.show()
fig.savefig('MTL-Type-over-Clusters-MTL.pdf', dpi=200)

# ============================
# Print total counts including META
# ============================
print("Total MTL counts:", sum([sum(MTLtype_count_dict[mt]) for mt in MTLtype]))
