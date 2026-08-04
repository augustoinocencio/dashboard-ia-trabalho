import streamlit as st
import pandas as pd

st.title("📊 4. Resultados e Discussão")
st.markdown("---")

st.markdown("""
A análise dos estudos evidencia que os impactos da IA Generativa não são homogêneos: eles combinam efeitos de **substituição** (em tarefas estruturadas e repetitivas) e de **complementaridade** (em atividades que exigem julgamento humano e colaboração).
""")

st.subheader("📋 Matriz SWOT da IA Generativa no Mercado de Trabalho")
st.markdown("A tabela abaixo sintetiza os fatores internos da tecnologia e os fatores externos do mercado identificados na literatura:")

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
Os resultados demonstram que o futuro do trabalho com a IA Generativa depende diretamente da forma como as organizações implementam a tecnologia e de como os trabalhadores desenvolvem suas competências para utilizá-la como ferramenta de apoio.
""")
