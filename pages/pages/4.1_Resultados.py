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
A análise integrada da literatura evidencia que os impactos da IA Generativa não são homogêneos. Eles combinam efeitos de **substituição** (em tarefas estruturadas, repetitivas e previsíveis) e de **complementaridade** (em atividades que exigem julgamento humano, pensamento crítico e colaboração)[cite: 1].
""")

st.subheader("📈 Representação Conceitual dos Estudos Analisados")
st.markdown("Posicionamento dos autores conforme a ênfase atribuída à substituição e à complementaridade:")

# 2. Dados exatos do gráfico da apresentação
autores_data = pd.DataFrame({
    "Autor": ["Zarifhonarvar (2023)", "Araújo & Rayol (2024)", "Oliveira (2025)", "Hartley et al. (2025)", "Chen et al. (2025)"],
    "Ênfase em Substituição": [3.0, 4.2, 5.5, 7.5, 8.2],
    "Ênfase em Complementaridade": [6.0, 5.2, 5.8, 7.8, 8.6]
})

# Criação do gráfico de dispersão (scatter plot) idêntico ao slide
fig = px.scatter(
    autores_data,
    x="Ênfase em Substituição",
    y="Ênfase em Complementaridade",
    text="Autor",
    range_x=[0, 10],
    range_y=[0, 10],
    template="plotly_dark"
)

fig.update_traces(textposition='top center', marker=dict(size=12, color='#9013FE'))

fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="#FAFAFA",
    xaxis_title="Ênfase em Substituição",
    yaxis_title="Ênfase em Complementaridade"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 💡 Síntese dos Achados
Os resultados demonstram que os estudos mais recentes (como Hartley et al. e Chen et al.) pontuam uma visão mais integrada, onde tanto a substituição quanto a complementaridade ganham alta relevância simultânea[cite: 1].
""")
