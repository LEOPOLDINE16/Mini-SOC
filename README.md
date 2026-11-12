# Mini-SOC - Détection de connexions SSH suspectes

## 1. Présentation du projet

Ce projet personnel consiste à développer un outil simple de
détection d'événements de sécurité sur un système Linux.

L'objectif est d'analyser des journaux de connexions SSH afin
d'identifier des tentatives d'authentification échouées et de
détecter des comportements potentiellement suspects.

## 2. Objectifs

- Comprendre le fonctionnement des logs Linux.
- Lire et analyser des événements SSH.
- Identifier les tentatives de connexion échouées.
- Extraire et compter les adresses IP sources.
- Générer des alertes en cas de tentatives répétées.
- Développer un outil de détection en Python.

## 3. Technologies utilisées

- Ubuntu Server
- Python 3
- SSH
- Linux
- Git et GitHub

## 4. Fonctionnalités prévues

- Lecture d'un fichier de logs SSH.
- Détection des échecs d'authentification.
- Comptage des tentatives par adresse IP.
- Détection d'un seuil de tentatives suspectes.
- Affichage d'alertes dans le terminal.

## 5. Environnement de travail

Le projet est réalisé sur une machine virtuelle Ubuntu Server
hébergée avec VMware.

## 6. Cadre du projet

Les analyses seront effectuées sur des journaux de test.
Ce projet est réalisé à des fins pédagogiques.

## 7. Évolutions possibles

- Ajouter une interface graphique.
- Enregistrer les alertes dans un fichier.
- Ajouter des statistiques sur les événements détectés.
