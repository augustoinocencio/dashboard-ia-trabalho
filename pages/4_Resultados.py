import streamlit as st

st.title("📊 4. Resultados e Discussão")
st.markdown("---")

# Seção de KPIs (Indicadores-Chave)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="Estudos Analisados", value="5 Trabalhos", delta="Revisão Bibliográfica")
with col_m2:
    st.metric(label="Eixos Principais", value="2 Vertentes", delta="Substituição & Complementaridade")
with col_m3:
    st.metric(label="Foco Geográfico/Setorial", value="Global & Brasil", delta="Mercado de Trabalho")

st.markdown("---")
st.markdown("A análise dos estudos evidencia que os impactos da IA Generativa combinam efeitos de **substituição** e **complementaridade**.")
