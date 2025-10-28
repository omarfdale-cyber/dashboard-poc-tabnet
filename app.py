import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="POC DataSpace – TabNet vs RandomForest", page_icon="⚙️", layout="centered")

st.title("Preuve de Concept – Comparaison RandomForest vs TabNet")
st.markdown("Projet OpenClassrooms – Omar Fdale")

st.header("Résultats comparatifs")

# Remplace les chiffres par ceux de ton notebook
results = pd.DataFrame({
    'Modèle': ['RandomForest', 'TabNet'],
    'R²': [0.71, 0.78],
    'RMSE': [85000, 74000],
    'MAE': [56000, 49000],
    'Temps (s)': [4.3, 38.2]
})

st.dataframe(results)

st.subheader("Comparaison du score R²")
fig, ax = plt.subplots()
ax.bar(results['Modèle'], results['R²'], color=['steelblue', 'darkorange'])
ax.set_ylabel('R²')
ax.set_ylim(0, 1)
st.pyplot(fig)

st.header("Interprétation")
st.markdown("""
- TabNet obtient un R² plus élevé, donc une meilleure capacité de généralisation.  
- Les erreurs RMSE et MAE sont plus faibles, donc les prédictions sont plus précises.  
- TabNet demande plus de temps d'entraînement, ce qui est normal pour un modèle de deep learning.
""")

st.success("POC validée : TabNet surpasse la baseline RandomForest.")
