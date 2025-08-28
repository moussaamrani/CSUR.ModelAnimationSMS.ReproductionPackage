import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("**=========================*********************===================************================")

# Load data
data = pd.read_csv('CORPUS-Final.csv')

# Categories including AltaRica
category = ['TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER','AltaRica'] 

# Years grouped in 2-year intervals up to 2025
tech = ['2000-2001', '2002-2003', '2004-2005', '2006-2007', '2008-2009',
        '2010-2011', '2012-2013', '2014-2015', '2016-2017', '2018-2019',
        '2020-2021', '2022-2023', '2024-2025']

# Initialize counts
tech_count = [[0]*len(category) for _ in range(len(tech))]

# Count occurrences per 2-year interval
for i, row in data.iterrows():
    year = row['Year']
    cat = row['Unnamed: 12']
    for idx, interval in enumerate(tech):
        start, end = map(int, interval.split('-'))
        if start <= year <= end and cat in category:
            tech_count[idx][category.index(cat)] += 1

# Dummy second plot
level = ['Level1', 'Level2']
level_count = [[0]*len(category) for _ in range(len(level))]

# Create DataFrames
df1 = pd.DataFrame(tech_count, columns=category, index=tech)
df2 = pd.DataFrame(level_count, columns=category, index=level)

# Create figure with reduced width and increased height
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, constrained_layout=True, sharex=True, figsize=(9,12.2))

# First scatter plot
dfu1 = df1.unstack().reset_index()
dfu1.columns = list("XYS")
dfu1["S"] = dfu1["S"] * 700
a1.scatter(x="X", y="Y", s="S", data=dfu1, color='w', edgecolors='black', linewidth=2)
a1.margins(0.1)

# Second scatter plot
dfu2 = df2.unstack().reset_index()
dfu2.columns = list("XYS")
dfu2["S"] = dfu2["S"] * 600
a2.scatter(x="X", y="Y", s="S", data=dfu2, color='w', edgecolors='black', linewidth=2)
a2.margins(0.1)

# Annotate first plot
for i, year_interval in enumerate(tech):
    for j, cat in enumerate(category):
        s = tech_count[i][j]
        if s != 0:
            a1.annotate(str(s), xy=(cat, year_interval), ha='center', va='center', color='black', size=14)

# Annotate second plot
for i, lvl in enumerate(level):
    for j, cat in enumerate(category):
        s = level_count[i][j]
        if s != 0:
            a2.annotate(str(s), xy=(cat, lvl), ha='center', va='center', color='black', size=22)

# Labels and styling
a1.set_ylabel('Year Interval', size=14, weight="bold")
a2.set_ylabel('Level', size=14, weight="bold")
a1.set_xlabel('')
a2.set_xlabel('TOOL Cluster', size=14, weight="bold")
a1.tick_params(labelrotation=45, labelsize=12)
a2.tick_params(labelrotation=45, labelsize=12)
a1.grid(ls='dotted', color='black')
a2.grid(ls='dotted', color='black')

# Show and save figure
plt.tight_layout()
fig.savefig('TOOL-Clusters-Years-2025.pdf', dpi=200)
plt.show()


