import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 4. Resultados e Discussão")
st.markdown("---")

# 1. Indicadores em Destaque (KPIs)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="Estudos Analisados", value="5 Trabalhos", delta="Revisão Bibliográfica")
with col_m2:
    st.metric(label="Eixos Principais", value="2 Vertentes", delta="Substituição & Complementaridade")
with col_m3:
    st.metric(label="Foco Setorial", value="Global & Brasil", delta="Mercado de Trabalho")

st.markdown("---")

st.markdown("""
A análise integrada da literatura evidencia que os impactos da IA Generativa não são homogêneos. Eles combinam efeitos de **substituição** (em tarefas estruturadas, repetitivas e previsíveis) e de **complementaridade** (em atividades que exigem julgamento humano, pensamento crítico e colaboração).
""")

st.subheader("📋 Matriz SWOT da IA Generativa no Mercado de Trabalho")
st.markdown("A visualização abaixo sintetiza os fatores internos da tecnologia e os fatores externos do mercado identificados nos estudos:")

# 2. Dados estruturados para o gráfico interativo
swot_df = pd.DataFrame({
    "Dimensão": ["Forças", "Forças", "Fraquezas", "Fraquezas", "Oportunidades", "Oportunidades", "Ameaças", "Ameaças"],
    "Fator": [
        "Aumento de Produtividade", "Redução de Tempo", 
        "Dependência de Modelos", "Necessidade de Investimento",
        "Novas Funções Híbridas", "Expansão de Competências",
        "Risco de Desemprego", "Desigualdade de Acesso"
    ],
    "Relevância (Peso Analítico)": [9, 8, 7, 6, 9, 8, 9, 8]
})

# Criação do gráfico interativo com Plotly
fig = px.bar(
    swot_df, 
    x="Relevância (Peso Analítico)", 
    y="Fator", 
    color="Dimensão", 
    orientation="h",
    color_discrete_map={
        "Forças": "#28a745",
        "Fraquezas": "#ffc107",
        "Oportunidades": "#17a2b8",
        "Ameaças": "#ff4b4b"
    },
    template="plotly_dark"
)

fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="#FAFAFA",
    xaxis_title="Relevância Analítica na Literatura",
    yaxis_title=""
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 💡 Síntese dos Achados
Os resultados demonstram que o futuro do trabalho com a IA Generativa depende diretamente da forma como as organizações implementam a tecnologia e de como os trabalhadores desenvolvem suas competências para utilizá-la como ferramenta de apoio estratégica.
""")
