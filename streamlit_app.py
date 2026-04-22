import streamlit as st
st.set_page_config(page_title="Guia de Doses Pediátricas", layout="centered")
st.title("Calculadora Doses Pediátricas")
# 1. Escolha do Medicamento primeiro
escolha = st.selectbox("Selecione o Medicamento:", ["Selecione o Medicamento", "Paracetamol 40 mg/mL", "Ibuprofeno 20 mg/mL","Ibuprofeno 40mg/mL", "Amoxicilina + Ác. Clavulanico 250/64.5", "Amoxicilina + Ác.Clavulanico 400/57", "Amoxicilina + Ác.Clavulanico 600/42.9", "Azitromicina 40 mg/mL"])

#2 Lógica específica de cada um 
if escolha == "Paracetamol 40 mg/mL":
    st.subheader ("Paracetamol 40 mg/mL")
    st.write ("Dose máxima 60 mg/kg/dia")
    peso = st.number_input ( "Peso (Kg):")
    tomas = st.radio ("Nº de tomas por dia:", [3, 4])
    if peso > 0:
        dose = (1.5 * peso) / tomas
    st.divider()
    st.metric(label="Volume a tomar (mL)", value = f"{dose} mL" )
