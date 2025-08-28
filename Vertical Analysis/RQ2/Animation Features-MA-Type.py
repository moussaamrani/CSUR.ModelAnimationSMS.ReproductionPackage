import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
data = pd.read_csv('CORPUS-Final.csv')

target = data["Animation Type"]

# Comptage des types d'animation
NbOffline = sum("PREDEF" in str(t).upper() for t in target)
NbOnline = sum("CUSTOM" in str(t).upper() for t in target)

TotalPub = NbOffline + NbOnline

# Calcul des pourcentages
rateOffline = NbOffline / TotalPub
rateOnline = NbOnline / TotalPub

Tasks = [rateOnline, rateOffline]
my_labels = ['CUSTOM', 'PREDEF']
my_colors = ['silver', 'lightblue']
my_explode = (0, 0)

# Création du graphique
plt.figure(figsize=(6, 6))  # Ajuste la taille globale si besoin
plt.pie(
    Tasks,
    labels=my_labels,
    autopct='%1.1f%%',
    startangle=180,
    textprops={'fontsize': 20},
    colors=my_colors,
    explode=my_explode,
    wedgeprops={"edgecolor": "black", 'linewidth': 1.7}
)

plt.title('')
plt.axis('equal')

# Sauvegarde du PDF sans marges blanches
plt.savefig(
    "Animation Features-MA-Type.pdf",
    dpi=600,
    bbox_inches='tight',
    pad_inches=0
)

plt.show()
