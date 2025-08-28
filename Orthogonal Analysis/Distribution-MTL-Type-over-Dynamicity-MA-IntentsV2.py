import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

print("===============-------------------===============")
# Load data
data = pd.read_csv('CORPUS-Final.csv')

# Merge META into MP
data["MTL Type"] = data["MTL Type"].replace("MP", "META")

# Define categories
Dynamicity = ['ONLINE', 'OFFLINE']
animIntent = ['DEBUG', 'UNDERSTAND', 'EDUCATE']
MTLtype = ['GBT', 'META', 'GPPL', 'GPML', 'LOGIC', 'ALGEBRAIC']

# Initialize counters
ONLINEIntent = [0] * len(MTLtype)
OFFLINEIntent = [0] * len(MTLtype)
DebuggingMTL = [0] * len(MTLtype)
UnderstandingMTL = [0] * len(MTLtype)
EducationalMTL = [0] * len(MTLtype)

# Extract targets
target1 = data["MTL Type"]
target2 = data["Unnamed: 15"]
target3 = data["Dynamicity"]
target4 = data["Unnamed: 14"]
target5 = data["Unnamed: 16"]

# Count ONLINE / OFFLINE for each MTL type
for i in range(len(target3)):
    for j in range(len(MTLtype)):
        if MTLtype[j] == target1[i]:
            if target3[i] == "ONLINE":
                ONLINEIntent[j] += 1
            elif target3[i] == "OFFLINE":
                OFFLINEIntent[j] += 1

# Count Animation Intent per MTL type
for i in range(len(target2)):
    for j in range(len(MTLtype)):
        if MTLtype[j] == target1[i]:
            if target2[i] == "DEBUG" or target4[i] == "DEBUG" or target5[i] == "DEBUG":
                DebuggingMTL[j] += 1
            if target2[i] == "UNDERSTAND" or target4[i] == "UNDERSTAND" or target5[i] == "UNDERSTAND":
                UnderstandingMTL[j] += 1
            if target2[i] == "EDUCATE" or target4[i] == "EDUCATE" or target5[i] == "EDUCATE":
                EducationalMTL[j] += 1

# Build DataFrames
Dynamicity_count = [ONLINEIntent, OFFLINEIntent]
animIntent_count = [DebuggingMTL, UnderstandingMTL, EducationalMTL]

df1 = pd.DataFrame(Dynamicity_count, columns=MTLtype, index=Dynamicity)
df2 = pd.DataFrame(animIntent_count, columns=MTLtype, index=animIntent)

# Create figure and subplots with larger width
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, sharex=True, figsize=(16,7), constrained_layout=False)
fig.subplots_adjust(top=0.95, bottom=0.12, left=0.10, right=0.97, hspace=0.3)  # margins outside figure

# ============================
# PLOT 1: Dynamicity Bubble Chart
# ============================
dfu = df1.unstack().reset_index()
dfu.columns = list("XYS")
dfu["S"] *= 400
a1.scatter(x="X", y="Y", s="S", data=dfu, color='w', edgecolors='black', linewidth=2)

# ============================
# PLOT 2: Animation Intent Bubble Chart
# ============================
dfu = df2.unstack().reset_index()
dfu.columns = list("XYS")
dfu["S"] *= 400
a2.scatter(x="X", y="Y", s="S", data=dfu, color='w', edgecolors='black', linewidth=2)

# ============================
# Annotations for Dynamicity
# ============================
for i in range(len(Dynamicity)):
    for j in range(len(MTLtype)):
        text = str(int(Dynamicity_count[i][j])) if Dynamicity_count[i][j] != 0 else " "
        a1.annotate(text=text, xy=(MTLtype[j], Dynamicity[i]), ha='center', va='center', color='black', size=20)

# ============================
# Annotations for Animation Intent
# ============================
for i in range(len(animIntent)):
    for j in range(len(MTLtype)):
        text = str(int(animIntent_count[i][j])) if animIntent_count[i][j] != 0 else " "
        a2.annotate(text=text, xy=(MTLtype[j], animIntent[i]), ha='center', va='center', color='black', size=22)

# ============================
# Labels, Titles, and Grid
# ============================
a1.set_ylabel('Dynamicity', size=18, labelpad=30, weight="bold")
a2.set_ylabel('Animation Intent', size=18, labelpad=30, weight="bold")
a1.set_xlabel('')
a2.set_xlabel('MTL Type', size=18, labelpad=30, weight="bold")

a1.tick_params(labelsize=16)
a2.tick_params(labelsize=16, rotation=30)

a1.set_axisbelow(True)
a2.set_axisbelow(True)
a1.grid(ls='dotted', color='black')
a2.grid(ls='dotted', color='black')

# ============================
# Reduce internal whitespace (inside figure)
# ============================
a1.margins(0.05)
a2.margins(0.05)

# Set axis limits to collate points with borders
a1.set_xlim(-0.5, len(MTLtype)-0.5)
a1.set_ylim(-0.5, len(Dynamicity)-0.5)
a2.set_xlim(-0.5, len(MTLtype)-0.5)
a2.set_ylim(-0.5, len(animIntent)-0.5)

# ============================
# Show and Save Figure
# ============================
plt.show()
fig.savefig('MTL+DYN+MAIntent.pdf', dpi=200, bbox_inches='tight')

# ============================
# Print Total Counts
# ============================
print("Total counts:", sum(ONLINEIntent) + sum(OFFLINEIntent))
