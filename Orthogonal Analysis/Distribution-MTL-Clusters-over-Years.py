import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import gridspec
from matplotlib.pyplot import figure

print("========================================================================================================")

# Lecture du fichier CSV
data = pd.read_csv('CORPUS-Final.csv')

# Vecteurs mis à jour
Dynamicity = ['ONLINE', 'OFFLINE']
AnimIntent = ['Debugging', 'Understanding', 'Educational']
TOOLS = ['MEEDUSE', 'OTHER', 'GEMOC', 'TOPCASED', 'ATOMPM', 'GenGED', 'VMTS', 'RMT', 'AltaRica', 'TROPIC', 'DiaMeta']

# Mise à jour des années
Years = [str(y) for y in range(2000, 2026)]
Years2 = [
    '2000-2001', '2002-2003', '2004-2005', '2006-2007', '2008-2009',
    '2010-2011', '2012-2013', '2014-2015', '2016-2017', '2018-2019',
    '2020-2021', '2022-2023', '2024-2025'
]

level = ['', '']

# Suppression des doublons dans la liste MTLCluster
MTLCluster = list(dict.fromkeys(['FSM','PN','B','REWRITE','KERMETA','XTEND/JAVA','VARIOUS','OTHER']))

# Variables cibles
target1 = data["CLUSTER"]
target2 = data["Year"]
target3 = data["Dynamicity"]

# Initialisation des compteurs d'années
Years_count = [[0]*len(MTLCluster) for _ in range(len(Years2))]

# Remplissage des compteurs par année
for i in range(len(target2)):
    for k, (start, end) in enumerate([(2000,2001),(2002,2003),(2004,2005),(2006,2007),
                                      (2008,2009),(2010,2011),(2012,2013),(2014,2015),
                                      (2016,2017),(2018,2019),(2020,2021),(2022,2023),(2024,2025)]):
        if start <= target2[i] <= end:
            for j, cluster in enumerate(MTLCluster):
                if cluster == target1[i]:
                    Years_count[k][j] += 1

# Création du DataFrame
df1 = pd.DataFrame(Years_count, columns=MTLCluster, index=Years2)

# DataFrame secondaire (vide)
df2_data = [[0]*len(MTLCluster), [0]*len(MTLCluster)]
df2 = pd.DataFrame(df2_data, columns=MTLCluster, index=level)

# Création des graphiques avec largeur réduite et hauteur augmentée
fig, (a1, a2) = plt.subplots(ncols=1, nrows=2, constrained_layout=True, sharex=True, figsize=(8,12))
plt.rcParams["axes.linewidth"] = 2.5

# Premier graphique
dfu = df1.unstack().reset_index()
dfu.columns = list("XYS")
dfu["S"] *= 900
a1.scatter(x="X", y="Y", s="S", data=dfu, color='w', edgecolors='black', linewidth=2)
a1.margins(.1)

# Second graphique
df2_plot_data = []
for i, col in enumerate(df2.columns):
    for j, idx in enumerate(df2.index):
        df2_plot_data.append({'X': col, 'Y': idx, 'S': df2.iloc[j, i] * 900})
dfu2 = pd.DataFrame(df2_plot_data)
a2.scatter(x="X", y="Y", s="S", data=dfu2, color='w', edgecolors='black', linewidth=2)
a2.margins(.1)

# Ajout des annotations sur le graphique principal
for i in range(len(Years2)):
    for j in range(len(MTLCluster)):
        text = str(int(Years_count[i][j])) if Years_count[i][j] != 0 else " "
        a1.annotate(text=text, xy=(MTLCluster[j], Years2[i]), ha='center', va='center', color='black', size=12)

# Ajout des annotations sur le graphique secondaire
for i in range(len(level)):
    for j in range(len(MTLCluster)):
        text = str(df2.iloc[i, j]) if df2.iloc[i, j] != 0 else " "
        a2.annotate(text=text, xy=(MTLCluster[j], level[i]), ha='center', va='center', color='black', size=12)

# Mise en forme des graphiques
a1.set_ylabel('Year', size=14, labelpad=15, weight="bold")
a2.set_xlabel('MTL Cluster', size=14, labelpad=15, weight="bold")
a1.tick_params(labelsize=10)
a2.tick_params(labelsize=10, rotation=45)
a1.grid(ls='dotted', color='black')
a2.grid(ls='dotted', color='black')

# Sauvegarde et affichage
plt.tight_layout()
fig.savefig('MTL-Clusters-Years.pdf', dpi=200)
plt.show()

# Total global
total = sum(map(sum, Years_count))
print("Total :", total)
