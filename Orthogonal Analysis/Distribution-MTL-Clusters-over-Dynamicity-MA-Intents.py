import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lecture du CSV
data = pd.read_csv('CORPUS-Final.csv')

# Variables catégorielles
Dynamicity = ['ONLINE', 'OFFLINE']
AnimIntent = ['Debugging', 'Understanding', 'Educational']

# Nouvel ensemble d'outils sans répétition
TOOLS = ['MEEDUSE', 'OTHER', 'GEMOC', 'TOPCASED', 'ATOMPM', 'GenGED', 'VMTS', 'RMT', 'AltaRica', 'TROPIC', 'DiaMeta']

# Tableaux de comptage initialisés à 0
ONLINEMLLang = [0]*len(TOOLS)
OFFLINEMLLang = [0]*len(TOOLS)

DebuggingMLLang = [0]*len(TOOLS)
UnderstandingMLLang = [0]*len(TOOLS)
EducationalMLLang = [0]*len(TOOLS)

# Colonnes cibles dans le CSV
target1 = data["Unnamed: 12"]  # outils
target2 = data["Unnamed: 15"]  # animation intent
target3 = data["Dynamicity"]   # online/offline
target4 = data["Unnamed: 14"]  # animation intent secondaire
target5 = data["Unnamed: 16"]  # animation intent secondaire

# Comptage pour Dynamicity
for i in range(len(target3)):
    if "ONLINE" in str(target3[i]).upper():
        for j in range(len(TOOLS)):
            if TOOLS[j].upper() in str(target1[i]).upper():
                ONLINEMLLang[j] += 1
    if "OFFLINE" in str(target3[i]).upper():
        for j in range(len(TOOLS)):
            if TOOLS[j].upper() in str(target1[i]).upper():
                OFFLINEMLLang[j] += 1

# Comptage pour Animation Intent
for i in range(len(target2)):
    if "DEBUG" in str(target2[i]).upper() or "DEBUG" in str(target4[i]).upper() or "DEBUG" in str(target5[i]).upper():
        for j in range(len(TOOLS)):
            if TOOLS[j].upper() in str(target1[i]).upper():
                DebuggingMLLang[j] += 1
    if "UNDERSTAND" in str(target2[i]).upper() or "UNDERSTAND" in str(target4[i]).upper() or "UNDERSTAND" in str(target5[i]).upper():
        for j in range(len(TOOLS)):
            if TOOLS[j].upper() in str(target1[i]).upper():
                UnderstandingMLLang[j] += 1
    if "EDUCATE" in str(target2[i]).upper() or "EDUCATE" in str(target4[i]).upper() or "EDUCATE" in str(target5[i]).upper():
        for j in range(len(TOOLS)):
            if TOOLS[j].upper() in str(target1[i]).upper():
                EducationalMLLang[j] += 1

# Création des DataFrames
Dynamicity_count = [ONLINEMLLang, OFFLINEMLLang]
AnimIntent_count = [DebuggingMLLang, UnderstandingMLLang, EducationalMLLang]

df1 = pd.DataFrame(Dynamicity_count, columns=TOOLS, index=Dynamicity)
df2 = pd.DataFrame(AnimIntent_count, columns=TOOLS, index=AnimIntent)

# Création de la figure
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, constrained_layout=True, sharex=True, figsize=(11,6.5))

# Paramètres figure
plt.rcParams["figure.figsize"] = [11,6.5]
plt.rcParams["figure.autolayout"] = True
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 3

# Préparation des données pour le scatter plot
dfu = df1.unstack().reset_index()
dfu.columns = list("XYS")
dfu["S"] *= 380
a1.scatter(x="X", y="Y", s="S", data=dfu, color='w', edgecolors='black', linewidth=2)
a1.margins(.3)

dfu = df2.unstack().reset_index()
dfu.columns = list("XYS")
dfu["S"] *= 380
a2.scatter(x="X", y="Y", s="S", data=dfu, color='w', edgecolors='#000000', linewidth=2)
a2.margins(.3)

# Ajout des annotations pour Dynamicity
for i in range(len(Dynamicity)):
    for j in range(len(TOOLS)):
        s = int(Dynamicity_count[i][j]) if Dynamicity_count[i][j] != 0 else " "
        a1.annotate(text=s, xy=(TOOLS[j], Dynamicity[i]), ha='center', va='center', color='black', size=18)

# Ajout des annotations pour Animation Intent
for i in range(len(AnimIntent)):
    for j in range(len(TOOLS)):
        s = int(AnimIntent_count[i][j]) if AnimIntent_count[i][j] != 0 else " "
        a2.annotate(text=s, xy=(TOOLS[j], AnimIntent[i]), ha='center', va='center', color='black', size=18)

# Paramètres axes
a1.set_ylabel('Dynamicity', size=16, labelpad=20, weight="bold")
a2.set_ylabel('Animation Intent', size=16, labelpad=20, weight="bold")
a1.tick_params(labelsize=18.0)
a2.tick_params(labelsize=12.0, rotation=30)
a1.set_xlabel('', size=10, labelpad=20)
a2.set_xlabel('TOOLS', size=16, labelpad=20, weight="bold")
a1.set_axisbelow(True)
a2.set_axisbelow(True)
a1.grid(ls='dotted', color='black')
a2.grid(ls='dotted', color='black')

# Affichage et sauvegarde
plt.tight_layout()
plt.show()
#fig.savefig('MTL-Clusters-over-Dynamicity-MA-Intents.pdf', dpi=200)
fig.savefig('TOOL+DYN+MAIntent.pdf', dpi=200)

