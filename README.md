# 🪐 Simulation N-Corps du Système Solaire (Comparatif Algorithmique)

> **Comparatif d'algorithmes d'intégration numérique pour la mécanique céleste.**

Ce projet implémente et compare différentes méthodes d'intégration numérique pour simuler les interactions gravitationnelles du système solaire. Il met en évidence l'importance du choix de l'algorithme sur la stabilité des orbites.
---
### Méthodes Implémentées & Comparaison
Le projet explore trois approches pour résoudre les équations du mouvement :

1.  **Méthode d'Euler (Standard) :** Approche intuitive du premier ordre. *Limite observée : Dérive rapide de l'énergie et instabilité des orbites sur le long terme.*
2.  **Méthode d'Euler Asymétrique (Symplectique) :** Variante semi-implicite. *Avantage : Meilleure conservation de l'énergie orbitale.*
3.  **Runge-Kutta :** Implémenté en tant que module avancé (bonus). *Résultat : Précision maximale et stabilité robuste pour les simulations longues durées.*
---
### Stack Technique
* **Langage :** Python 3
* **Calcul :** NumPy (Optimisation vectorielle)
* **Visualisation :** Matplotlib

---
### Installation & Utilisation

Vous pouvez lancer la simulation de deux manières.
#### Option A : Installation Classique (Python)

1. Cloner le repository :
   ```bash
   git clone [https://github.com/nolan-nedelec/solar-system-simulation.git](https://github.com/nolan-nedelec/solar-system-simulation.git)
2. Installer les dépendances :
   ```bash
   pip install numpy matplotlib
3. Lancer les programmes

#### Option B : Lancer via Docker 🐳 (Recommandé)
Cette méthode garantit que la simulation tourne dans un environnement isolé, sans avoir à gérer les versions de Python ou les bibliothèques.

1.  **Construire l'image :**
    ```bash
    docker build -t solar-system .
    ```

2.  **Lancer la simulation :**
    ```bash
    docker run --rm -v ${PWD}:/app solar-system
    ```
---
Projet réalisé pour analyser la stabilité numérique des systèmes dynamiques.
