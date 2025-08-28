import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
data = pd.read_csv('CORPUS-Final.csv')

# Récupération de la colonne "Orientation"
target = data["Orientation"]

# Comptage des catégories
Nboffline = sum("INDUS" in str(t).upper() for t in target)
Nbonline = sum("ACA" in str(t).upper() for t in target)

# Calcul des pourcentages
TotalPub = Nboffline + Nbonline
rateoffline = Nboffline / TotalPub * 100
rateonline = Nbonline / TotalPub * 100

# Préparer les données pour le graphique
ratioDist = [rateonline, rateoffline]
my_labels = ['Academic', 'Industrial']
my_colors = ['lightblue', 'silver']
my_explode = (0, 0)

# Création de la figure au format A4 portrait
fig = plt.figure(figsize=(8.27, 11.69))  # Format A4 en pouces
ax = fig.add_subplot(111)

# Création du graphique circulaire
wedges, texts, autotexts = ax.pie(
    ratioDist,
    labels=my_labels,
    textprops={'fontsize': 25},
    autopct='%1.1f%%',
    startangle=180,
    colors=my_colors,
    explode=my_explode,
    wedgeprops={"edgecolor": "black", 'linewidth': 1.7}
)

# Supprimer le titre et forcer un cercle parfait
ax.set_title('')
ax.axis('equal')

# Supprimer toutes les marges internes
fig.subplots_adjust(0, 0, 1, 1)
ax.set_position([0, 0, 1, 1])

# Sauvegarde du PDF sans AUCUNE marge
plt.savefig(
    "Distribution-over-Orientation.pdf",
    format="pdf",
    dpi=600,
    bbox_inches='tight',
    pad_inches=0
)

plt.close(fig)
