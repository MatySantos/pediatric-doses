import streamlit as st
st.set_page_config(page_title="Guia de Doses Pediátricas", layout="centered")
st.title("Calculadora Doses Pediátricas")
# 1. Escolha do Medicamento primeiro
escolha = st.selectbox("Selecione o Medicamento:", ["Paracetamol 40 mg/mL", "Ibuprofeno 20 mg/mL","Ibuprofeno 40mg/mL"])
