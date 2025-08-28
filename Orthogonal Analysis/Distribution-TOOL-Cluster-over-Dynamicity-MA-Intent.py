import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

print("=========================*********************===================************================")

# Load data
data = pd.read_csv('CORPUS-Final.csv')

# Categorical arrays
tech = ['ONLINE', 'OFFLINE']
level = ['Debugging', 'Understanding', 'Educational']
category = ['TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER','AltaRica']  # Added AltaRica

# Initialize counts (length = 11 now)
ONLINEMLLang = [0]*len(category)
OFFLINEMLLang = [0]*len(category)
DebuggingMLLang = [0]*len(category)
UnderstandingMLLang = [0]*len(category)
EducationalMLLang = [0]*len(category)

# Targets from CSV
target1 = data["Unnamed: 12"]
target2 = data["Unnamed: 15"]
target3 = data["Dynamicity"]
target4 = data["Unnamed: 14"]
target5 = data["Unnamed: 16"]

# Count tech occurrences
for i in range(len(target3)):
    if target3[i]=="ONLINE": 
        for j in range(len(category)):
            if category[j]==target1[i]: 
                ONLINEMLLang[j] += 1 
    if target3[i]=="OFFLINE": 
        for j in range(len(category)):
            if category[j]==target1[i]: 
                OFFLINEMLLang[j] += 1 

# Count levels
for i in range(len(target2)):
    if target2[i]=="DEBUG" or target4[i]=="DEBUG" or target5[i]=="DEBUG": 
        for j in range(len(category)):
            if category[j]==target1[i]: 
                DebuggingMLLang[j] += 1 
    if target2[i]=="UNDERSTAND" or target4[i]=="UNDERSTAND" or target5[i]=="UNDERSTAND": 
        for j in range(len(category)):
            if category[j]==target1[i]: 
                UnderstandingMLLang[j] += 1 
    if target2[i]=="EDUCATE" or target4[i]=="EDUCATE" or target5[i]=="EDUCATE": 
        for j in range(len(category)):
            if category[j]==target1[i]: 
                EducationalMLLang[j] += 1 

# Prepare dataframes
tech_count = [ONLINEMLLang, OFFLINEMLLang]
level_count = [DebuggingMLLang, UnderstandingMLLang, EducationalMLLang]
df1 = pd.DataFrame(tech_count, columns=category, index=tech)
df2 = pd.DataFrame(level_count, columns=category, index=level)

# Create figure and subplots
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, constrained_layout=True, sharex=True, figsize=(11,6.5))

# Plot first scatter
dfu1 = df1.unstack().reset_index()
dfu1.columns = list("XYS")
dfu1["S"] *= 380
a1.scatter(x="X", y="Y", s="S", data=dfu1, color='w', edgecolors='black', linewidth=2)
a1.margins(.3)

# Plot second scatter
dfu2 = df2.unstack().reset_index()
dfu2.columns = list("XYS")
dfu2["S"] *= 380
a2.scatter(x="X", y="Y", s="S", data=dfu2, color='w', edgecolors='black', linewidth=2)
a2.margins(.3)

# Annotate first plot
for i in range(len(tech)):
    for j in range(len(category)):
        s = int(tech_count[i][j]) if tech_count[i][j] != 0 else " "
        a1.annotate(str(s), xy=(category[j], tech[i]), ha='center', va='center', color='black', size=18)

# Annotate second plot
for i in range(len(level)):
    for j in range(len(category)):
        s = int(level_count[i][j]) if level_count[i][j] != 0 else " "
        a2.annotate(str(s), xy=(category[j], level[i]), ha='center', va='center', color='black', size=18)

# Labels and styling
a1.set_ylabel('Dynamicity', size=16, labelpad=20, weight="bold")
a2.set_ylabel('Animation Intent', size=16, labelpad=20, weight="bold")
a1.tick_params(labelsize=18.0)
a2.tick_params(labelsize=14.0, rotation=30)
a1.set_xlabel('')
a2.set_xlabel('TOOLS', size=16, labelpad=20, weight="bold")
a1.set_axisbelow(True)
a2.set_axisbelow(True)
a1.grid(ls='dotted', color='black')
a2.grid(ls='dotted', color='black')

# Show and save figure
plt.tight_layout()
plt.show()
fig.savefig('TOOL+DYN+MAIntent.pdf', dpi=200)
