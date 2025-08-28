import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
data = pd.read_csv('CORPUS-Final.csv')

target = data["Dynamicity"]

# Comptage des occurrences ONLINE / OFFLINE
nbOffline = sum("OFF" in str(t).upper() for t in target)
NbOnline = sum("ON" in str(t).upper() for t in target)

# Calcul des pourcentages
TotalPub = nbOffline + NbOnline
rateOffline = nbOffline / TotalPub * 100
rateOnline = NbOnline / TotalPub * 100

# Préparation des données pour le graphique
Tasks = [rateOffline, rateOnline]
my_labels = ['Offline', 'Online']
my_colors = ['silver', 'lightblue']
my_explode = (0, 0)

# Création du graphique
plt.figure(figsize=(6, 6))  # Ajuste la taille si nécessaire
plt.pie(
    Tasks,
    labels=my_labels,
    autopct='%1.1f%%',
    textprops={'fontsize': 20},
    startangle=180,
    colors=my_colors,
    explode=my_explode,
    wedgeprops={"edgecolor": "black", 'linewidth': 1.7}
)

# Supprimer le titre et assurer une bonne mise en page
plt.title('')
plt.axis('equal')

# Sauvegarde du PDF sans marges blanches
plt.savefig(
    "Animation Features-Dynamicity.pdf",
    dpi=600,
    bbox_inches='tight',
    pad_inches=0
)

plt.show()
