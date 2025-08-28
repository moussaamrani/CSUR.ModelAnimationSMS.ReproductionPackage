import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
data = pd.read_csv('CORPUS-Final.csv')

# Récupération de la colonne "Venue Type"
target = data["Venue Type"]

# Comptage des types de publication selon la première lettre
NbConf = sum(str(t).upper().startswith("C") for t in target)
NbWSHOP = sum(str(t).upper().startswith("W") for t in target)
NbJOUR = sum(str(t).upper().startswith("J") for t in target)

# Vérification des valeurs
print(f"Conférences : {NbConf}")
print(f"Workshops : {NbWSHOP}")
print(f"Journaux : {NbJOUR}")

# Calcul des pourcentages avec deux décimales
TotalPub = NbConf + NbWSHOP + NbJOUR
rateCONF = round(NbConf / TotalPub * 100, 2)
rateWSHOP = round(NbWSHOP / TotalPub * 100, 2)
# Pour s'assurer que la somme = 100%, on calcule le dernier comme reste
rateJOUR = round(100 - rateCONF - rateWSHOP, 2)

# Vérification des taux
print(f"Conférences : {rateCONF}%")
print(f"Workshops : {rateWSHOP}%")
print(f"Journaux : {rateJOUR}%")
print("Somme des pourcentages :", rateCONF + rateWSHOP + rateJOUR)

# Préparation des données pour le graphique
Tasks = [rateCONF, rateWSHOP, rateJOUR]
my_labels = ['Conference', 'Workshop', 'Journal']
my_colors = ['#ea8b3e', '#8b3eea', '#ffcc00']
my_explode = (0, 0, 0)

# Création du graphique
plt.figure(figsize=(6, 6))  # Taille uniforme
plt.pie(
    Tasks,
    labels=my_labels,
    textprops={'fontsize': 18},
    autopct=lambda p: f'{p:.2f}%',  # Affiche deux décimales
    startangle=180,
    colors=my_colors,
    explode=my_explode,
    wedgeprops={"edgecolor": "black", 'linewidth': 1.7}
)

# Supprimer le titre et rendre les proportions égales
plt.title('')
plt.axis('equal')

# Sauvegarde du PDF sans marges blanches
plt.savefig(
    "distribution-venu.pdf",
    dpi=600,
    bbox_inches='tight',  # Supprime les marges blanches
    pad_inches=0          # Élimine les espaces résiduels
)

plt.show()
