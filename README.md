# 🪐 Simulation N-Corps du Système Solaire (Comparatif Algorithmique)

Ce projet implémente et compare différentes méthodes d'intégration numérique pour simuler les interactions gravitationnelles du système solaire. Il met en évidence l'importance du choix de l'algorithme sur la stabilité des orbites.

### 🧪 Méthodes Implémentées & Comparaison
Le projet explore trois approches pour résoudre les équations du mouvement :

1.  **Méthode d'Euler (Standard) :** Approche intuitive du premier ordre. *Limite observée : Dérive rapide de l'énergie et instabilité des orbites sur le long terme.*
2.  **Méthode d'Euler Asymétrique (Symplectique) :** Variante semi-implicite. *Avantage : Meilleure conservation de l'énergie orbitale.*
3.  **Runge-Kutta :** Implémenté en tant que module avancé (bonus). *Résultat : Précision maximale et stabilité robuste pour les simulations longues durées.*

### 💻 Stack Technique
* **Langage :** Python 3
* **Calcul :** NumPy (Optimisation vectorielle)
* **Visualisation :** Matplotlib

### 🚀 Lancer la simulation
1. Cloner le repository :
   ```bash
   git clone [https://github.com/nolan-nedelec/solar-system-simulation.git](https://github.com/nolan-nedelec/solar-system-simulation.git)
2. Installer les dépendances :
   ```bash
   pip install numpy matplotlib
4. Lancer les programmes

Projet réalisé pour analyser la stabilité numérique des systèmes dynamiques.
