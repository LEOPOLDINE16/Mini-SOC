from pathlib import Path
import re
from collections import Counter
from datetime import datetime

# Déterminer le chemin du projet
projet = Path(__file__).resolve().parent.parent
fichier_logs = projet / "logs" / "auth.log"
fichier_alertes = projet / "logs" / "alerts.log"

# Seuil de détection
SEUIL = 5

# Compteur des tentatives échouées
tentatives_par_ip = Counter()

# Lire les logs SSH
with open(fichier_logs, "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()

print("=== Analyse des logs SSH ===")

for ligne in lignes:
    if "Failed password" in ligne:
        resultat = re.search(r"Failed password .* from (\S+)", ligne)

        if resultat:
            ip = resultat.group(1)
            tentatives_par_ip[ip] += 1
            print(f"[ECHEC SSH] IP : {ip}")

# Afficher le bilan
print("\n=== Bilan des tentatives échouées ===")

for ip, nombre in tentatives_par_ip.items():
    print(f"{ip} : {nombre} tentative(s) échouée(s)")

# Détecter et enregistrer les alertes
print("\n=== Alertes de sécurité ===")

alerte_detectee = False

with open(fichier_alertes, "a", encoding="utf-8") as fichier:
    for ip, nombre in tentatives_par_ip.items():
        if nombre >= SEUIL:
            date_alerte = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = (
                f"[{date_alerte}] ALERTE SSH : "
                f"{ip} - {nombre} tentatives échouées"
            )

            print(message)
            fichier.write(message + "\n")
            alerte_detectee = True

if not alerte_detectee:
    print("Aucune activité suspecte détectée.")

print("\n=== Fin de l'analyse ===")

# Générer un rapport statistique
print("\n=== Rapport statistique SOC ===")

total_echecs = sum(tentatives_par_ip.values())
nombre_ip_distinctes = len(tentatives_par_ip)
nombre_ip_en_alerte = sum(
    1 for nombre in tentatives_par_ip.values()
    if nombre >= SEUIL
)

print(f"Total des échecs SSH : {total_echecs}")
print(f"Nombre d'IP distinctes : {nombre_ip_distinctes}")
print(f"Nombre d'IP en alerte : {nombre_ip_en_alerte}")

ip_plus_active = tentatives_par_ip.most_common(1)

if ip_plus_active:
    ip, nombre = ip_plus_active[0]
    print(f"IP la plus active : {ip} ({nombre} échecs)")
else:
    print("Aucune tentative échouée enregistrée.")
