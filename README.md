#  Proof of Concept – TabNet vs RandomForest

**Projet OpenClassrooms – Développez une preuve de concept (DataSpace)**  
Auteur : **Omar Fdale**  
Date : **Octobre 2025**

---

##  Objectif du projet

L’objectif de ce projet est de **tester une méthode récente (TabNet, Google AI, 2020)** afin d’améliorer la performance d’un modèle de machine learning sur des données tabulaires.

Cette preuve de concept (POC) vise à comparer **TabNet** à une méthode classique (**RandomForestRegressor**) sur un jeu de données réel.  
L’évaluation porte sur la **qualité des prédictions**, la **capacité de généralisation**, et la **pertinence de l’interprétation**.

---

##  Dataset utilisé

**Seattle Building Energy Benchmarking (Open Data Seattle)**  
Ce jeu de données recense plus de 3 000 bâtiments non résidentiels à Seattle avec leurs caractéristiques structurelles et énergétiques :  
- Surface, nombre d’étages, type de bâtiment  
- Consommation totale d’énergie (SiteEnergyUse(kBtu))  
- Émissions de CO₂ (TotalGHGEmissions)  
- Score ENERGY STAR  

Variable cible utilisée pour la POC :  
`SiteEnergyUse(kBtu)`

---

##  Méthodologie

###  Modèle de référence (baseline)
- **Algorithme :** RandomForestRegressor (Scikit-Learn)
- **Objectif :** servir de base de comparaison.

###  Nouveau modèle testé
- **Algorithme :** TabNet (Arik & Pfister, Google AI, 2020)
- **Librairie :** PyTorch TabNet  
- **Particularité :** mécanisme d’attention séquentielle et interprétabilité native.

---

##  Résultats comparatifs

| Modèle           | R²   | RMSE   | MAE   | Temps (s) |
|------------------|------|--------|-------|-----------|
| RandomForest     | 0.71 | 85000  | 56000 | 4.3       |
| **TabNet**       | **0.78** | **74000** | **49000** | 38.2     |

 **TabNet surpasse la baseline** : meilleure performance et meilleure interprétation grâce aux masques d’attention.

---

##  Dashboard Streamlit

Le dashboard interactif permet de :
- Visualiser la comparaison des performances entre RandomForest et TabNet  
- Afficher les métriques clés (R², RMSE, MAE)  
- Présenter une interprétation textuelle de la preuve de concept  

###  Lien de déploiement
 [https://omarfdale-cyber-dashboard-poc-tabnet.streamlit.app](https://omarfdale-cyber-dashboard-poc-tabnet.streamlit.app)

---

##  Références

- **Arik, S. O., & Pfister, T. (2020)** – *TabNet: Attentive Interpretable Tabular Learning*, Arxiv: [https://arxiv.org/abs/1908.07442](https://arxiv.org/abs/1908.07442)  
- **Machine Learning Mastery (2022)** – *A Gentle Introduction to TabNet*  
- **KDNuggets (2023)** – *Why TabNet Matters for Tabular Data*  

---

##  Installation locale

Pour exécuter le dashboard localement :

```bash
# 1. Cloner le dépôt
git clone https://github.com/omarfdale-cyber/dashboard-poc-tabnet.git
cd dashboard-poc-tabnet

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l’application
streamlit run app.py
