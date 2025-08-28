import matplotlib.pyplot as plt
import pandas as pd

# Charger les données
data = pd.read_csv('CORPUS-Final.csv')

# Colonnes ciblées
target1 = data["Unnamed: 14"]
target2 = data["Unnamed: 15"]
target3 = data["Unnamed: 16"]

# Compteurs
NbUND, NbDEBUG, NbEDUCATE = 0, 0, 0

# Fonction pour compter les intentions
def count_labels(target):
    global NbUND, NbDEBUG, NbEDUCATE
    for val in target:
        if val == "DEBUG":
            NbDEBUG += 1
        elif val == "UNDERSTAND":
            NbUND += 1
        elif val == "EDUCATE":
            NbEDUCATE += 1

# Compter pour les trois colonnes
count_labels(target1)
count_labels(target2)
count_labels(target3)

# Total
TotalPub = NbUND + NbDEBUG + NbEDUCATE

# Calcul des pourcentages non arrondis
rateDEBUG = NbDEBUG / TotalPub * 100
rateUND = NbUND / TotalPub * 100
rateEDUCATE = NbEDUCATE / TotalPub * 100

# Arrondi intelligent pour garantir 100 %
rates = [rateDEBUG, rateUND, rateEDUCATE]
rounded_rates = [round(r, 1) for r in rates]  # 1 seul chiffre après la virgule
diff = round(100 - sum(rounded_rates), 1)
rounded_rates[-1] += diff  # Corrige le dernier pourcentage

# Labels et couleurs
my_labels = ['DEBUG', 'UNDERSTAND', 'EDUCATE']
my_colors = ['silver', 'lightblue', '#9f6dd1']

# Création du graphique
plt.figure(figsize=(8, 8))
plt.pie(
    rounded_rates,
    labels=my_labels,
    autopct='%1.1f%%',   # <-- 1 seule décimale dans le graphique
    startangle=180,
    textprops={'fontsize': 18},
    colors=my_colors,
    wedgeprops={"edgecolor": "black", 'linewidth': 1.7}
)

# Titre
plt.title('Répartition des intentions', fontsize=20)
plt.axis('equal')

# Sauvegarde du graphique
plt.savefig("Animation-intent-Total.pdf", dpi=600)
plt.show()

# Affichage des valeurs exactes dans la console
print(f"DEBUG     : {rounded_rates[0]}% ({NbDEBUG})")
print(f"UNDERSTAND: {rounded_rates[1]}% ({NbUND})")
print(f"EDUCATE   : {rounded_rates[2]}% ({NbEDUCATE})")
print(f"TOTAL     : {sum(rounded_rates)}%")
