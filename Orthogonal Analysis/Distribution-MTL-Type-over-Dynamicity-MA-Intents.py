import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

print("===============-------------------===============")
# Load data
data = pd.read_csv('CORPUS-Final.csv')

# ✅ Merge META into MP
data["MTL Type"] = data["MTL Type"].replace("META", "MP")

# Define categories
Dynamicity = ['ONLINE', 'OFFLINE']
animIntent = ['DEBUG', 'UNDERSTAND', 'EDUCATE']
MTLtype = ['GBT', 'MP', 'GPPL', 'GPML', 'LOGIC', 'ALGEBRAIC']

# Initialize counters
ONLINEIntent = [0] * len(MTLtype)
OFFLINEIntent = [0] * len(MTLtype)
DebuggingMTL = [0] * len(MTLtype)
UnderstandingMTL = [0] * len(MTLtype)
EducationalMTL = [0] * len(MTLtype)

# Extract targets
target1 = data["MTL Type"]      # MTL Type
target2 = data["Unnamed: 15"]   # Animation Intent 1
target3 = data["Dynamicity"]    # ONLINE / OFFLINE
target4 = data["Unnamed: 14"]   # Animation Intent 2
target5 = data["Unnamed: 16"]   # Animation Intent 3

# ✅ Count ONLINE / OFFLINE for each MTL type
for i in range(len(target3)):
    for j in range(len(MTLtype)):
        if MTLtype[j] == target1[i]:
            if target3[i] == "ONLINE":
                ONLINEIntent[j] += 1
            elif target3[i] == "OFFLINE":
                OFFLINEIntent[j] += 1

# ✅ Count Animation Intent per MTL type
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

# Create figure and subplots
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, constrained_layout=True, sharex=True, figsize=(11, 6.5))

# ============================
# PLOT 1: Dynamicity Bubble Chart
# ============================
dfu = df1.unstack().reset_index()
dfu.columns = list("XYS")
dfu["S"] *= 400
a1.scatter(x="X", y="Y", s="S", data=dfu, color='w', linestyle='solid', edgecolors='black', linewidth=2)
a1.margins(.3)

# ============================
# PLOT 2: Animation Intent Bubble Chart
# ============================
dfu = df2.unstack().reset_index()
dfu.columns = list("XYS")
dfu["S"] *= 400
a2.scatter(x="X", y="Y", s="S", data=dfu, color='w', linestyle='solid', edgecolors='#000000', linewidth=2)
a2.margins(.3)

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
a1.set_ylabel('Dynamicity', size=16, labelpad=40, weight="bold", rotation=90, va='center')
a2.set_ylabel('Animation Intent', size=16, labelpad=20, weight="bold")
a1.tick_params(labelsize=18.0)
a2.tick_params(labelsize=18.0)

a1.set_xlabel('')
a2.set_xlabel('MTL Type', size=18, labelpad=20, weight="bold")
a1.set_axisbelow(True)
a2.set_axisbelow(True)
a1.grid(ls='dotted', color='black')
a2.grid(ls='dotted', color='black')

# ============================
# Show and Save Figure
# ============================
plt.tight_layout()
fig = plt.gcf()
plt.show()
# fig.savefig('MTL-Type-Dynamicity-MA-Intents.pdf', dpi=200)
fig.savefig('MTL+DYN+MAIntent.pdf', dpi=200)


# ============================
# Print Total Counts
# ============================
print("Total counts:", sum(ONLINEIntent) + sum(OFFLINEIntent))
