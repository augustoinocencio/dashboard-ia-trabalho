import streamlit as st
import pandas as pd

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
st.markdown("A tabela abaixo sintetiza os fatores internos da tecnologia e os fatores externos do mercado identificados nos estudos:")

# 2. Dados estruturados para a Tabela SWOT
swot_data = {
    "Categoria": ["Forças", "Fraquezas", "Oportunidades", "Ameaças"],
    "Principais Fatores Identificados": [
        "Aumento da produtividade; redução do tempo de execução de tarefas; melhoria na análise de informações; apoio à tomada de decisão; automação de atividades repetitivas.",
        "Dependência da qualidade dos modelos de IA; possibilidade de erros; necessidade de investimentos tecnológicos; necessidade constante de atualização profissional.",
        "Criação de novas funções relacionadas à tecnologia; expansão de empregos híbridos; desenvolvimento de competências digitais; aumento da produtividade econômica.",
        "Substituição de tarefas altamente automatizáveis; desigualdade no acesso tecnológico; risco de desemprego tecnológico; desafios regulatórios."
    ]
}

df_swot = pd.DataFrame(swot_data)

st.dataframe(df_swot, use_container_width=True, hide_index=True)

st.markdown("""
### 💡 Síntese dos Achados
Os resultados demonstram que o futuro do trabalho com a IA Generativa depende diretamente da forma como as organizações implementam a tecnologia e de como os trabalhadores desenvolvem suas competências para utilizá-la como ferramenta de apoio estratégica.
""")
