# Mini-SOC — Détection de connexions SSH suspectes

## 1. Présentation du projet

Mini-SOC est un projet personnel de cybersécurité visant à développer un outil de détection simple d'événements de sécurité à partir de journaux d'authentification SSH sous Linux.

L'outil analyse les logs, identifie les tentatives d'authentification échouées, regroupe les événements par adresse IP source et détecte les comportements potentiellement suspects.

Il permet de comprendre les bases du fonctionnement d'un SOC (Security Operations Center), notamment la collecte, l'analyse, la détection et la génération d'alertes de sécurité.

## 2. Objectifs

- Comprendre le fonctionnement des journaux d'authentification Linux.
- Analyser des événements de sécurité SSH.
- Identifier les tentatives d'authentification échouées.
- Extraire et compter les adresses IP sources.
- Détecter les tentatives répétées à partir d'un seuil défini.
- Générer des alertes de sécurité.
- Produire un rapport de synthèse.
- Développer un outil de détection en Python.

## 3. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Ubuntu Server | Environnement Linux |
| Python 3 | Développement du script de détection |
| SSH | Analyse des événements d'authentification |
| Regex | Extraction des adresses IP |
| Git | Gestion des versions |
| GitHub | Hébergement du projet |
| VMware | Virtualisation de l'environnement |

## 4. Fonctionnalités

Le script `src/detect.py` permet de :

- Lire un fichier de logs SSH (`logs/auth.log`).
- Identifier les tentatives de connexion échouées.
- Extraire les adresses IP sources.
- Compter les tentatives par adresse IP.
- Déclencher une alerte lorsqu'une IP atteint le seuil de 5 tentatives échouées.
- Enregistrer les alertes dans `logs/alerts.log`.
- Afficher des statistiques dans le terminal.
- Générer un rapport de synthèse dans `logs/rapport_soc.txt`.

### Statistiques générées

Le programme affiche notamment :

- Le nombre total de tentatives échouées.
- Le nombre d'adresses IP distinctes.
- Le nombre d'adresses IP ayant déclenché une alerte.
- L'adresse IP la plus active.

## 5. Architecture du projet

```text
Mini-SOC/
├── logs/
│   ├── auth.log
│   ├── alerts.log
│   └── rapport_soc.txt
├── src/
│   └── detect.py
├── .gitignore
└── README.md
```

| Fichier | Description |
|---|---|
| `logs/auth.log` | Journal d'authentification SSH analysé |
| `logs/alerts.log` | Historique des alertes générées |
| `logs/rapport_soc.txt` | Rapport de synthèse des événements |
| `src/detect.py` | Script Python de détection |
| `.gitignore` | Fichiers exclus du suivi Git |

## 6. Environnement de travail

Le projet est réalisé dans un environnement virtualisé :

- Système : Ubuntu Server
- Hyperviseur : VMware
- Accès à la machine : SSH depuis Windows PowerShell
- Langage : Python 3

## 7. Installation et utilisation

### Prérequis

- Une machine Linux disposant de Python 3.
- Un fichier de logs d'authentification SSH.
- Git pour récupérer le projet.

### Récupération du projet

```bash
git clone https://github.com/LEOPOLDINE16/Mini-SOC.git
cd Mini-SOC
```

### Exécution

```bash
python3 src/detect.py
```

Le programme analyse les logs disponibles, affiche les statistiques et génère les fichiers de sortie.

## 8. Validation et tests

Plusieurs scénarios ont été réalisés afin de vérifier le comportement du système.

| Scénario | Résultat attendu | Résultat obtenu |
|---|---|---|
| Tentatives échouées sous le seuil | Aucune alerte | Conforme |
| 5 tentatives échouées depuis une IP | Déclenchement d'une alerte | Conforme |
| Plusieurs IP avec des nombres de tentatives différents | Identification de l'IP la plus active | Conforme |

### Exemple de détection

Une adresse IP effectuant 5 tentatives d'authentification échouées déclenche une alerte SSH.

Exemple de message :

```text
ALERTE SSH : 192.168.1.50 - 5 tentatives échouées
```

## 9. Cadre et limites du projet

Ce projet est réalisé à des fins pédagogiques.

Les analyses sont effectuées à partir de journaux de test. L'outil constitue une première approche de la détection d'événements de sécurité.

À ce stade, le Mini-SOC :

- analyse un fichier de logs statique ;
- ne réalise pas de surveillance en temps réel ;
- ne bloque pas automatiquement les adresses IP ;
- utilise un seuil fixe de détection.

## 10. Évolutions possibles

- Ajouter une surveillance des logs en temps réel.
- Développer une interface graphique ou un tableau de bord.
- Ajouter des visualisations statistiques.
- Mettre en place une détection de comportements plus complexes.
- Intégrer un système de notification.
- Améliorer la gestion et la classification des alertes.
- Enrichir les événements avec des informations complémentaires sur les IP.

## 11. Compétences développées

- Analyse de journaux Linux.
- Détection d'événements de sécurité.
- Programmation Python.
- Manipulation de fichiers.
- Extraction de données avec des expressions régulières.
- Gestion de seuils et génération d'alertes.
- Utilisation de Git et GitHub.
- Mise en place d'un environnement Linux virtualisé.

## 12. Auteur

Projet personnel réalisé dans le cadre de mon parcours en cybersécurité — ERIS1, 3iL Ingénieurs.

GitHub : [LEOPOLDINE16](https://github.com/LEOPOLDINE16)
