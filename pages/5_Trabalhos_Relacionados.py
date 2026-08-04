import streamlit as st

st.title("📚 Trabalhos Relacionados e Autores")
st.markdown("---")

st.markdown("Utilize o filtro abaixo para explorar individualmente o foco de cada estudo analisado:")

# Dicionário com os dados detalhados
trabalhos_dict = {
    "de Oliveira (2025)": "Analisa a automação no mercado brasileiro, apontando que trabalhadores com menor acesso à qualificação enfrentam maiores barreiras de adaptação tecnológica.",
    "de Araújo & Rayol (2024)": "Discutem os reflexos da Quarta Revolução Industrial nas relações de trabalho, enfatizando os riscos de desemprego tecnológico e a urgência de regulação.",
    "Zarifhonarvar (2023)": "Mapeia a economia do ChatGPT, demonstrando que profissões intelectuais, administrativas e científicas sofrem forte alteração devido ao processamento automatizado de dados.",
    "Hartley et al. (2025)": "Evidenciam empiricamente os ganhos de produtividade e a redução do tempo de execução de tarefas promovidos pela IA.",
    "Chen et al. (2025)": "Investigam o dilema entre deslocamento e complementaridade, reforçando o caráter heterogêneo da tecnologia nas funções corporativas."
}

# Filtro interativo
autor_selecionado = st.selectbox("Selecione um autor para visualizar o resumo:", list(trabalhos_dict.keys()))

# Exibição dinâmica
st.markdown(f"""
<div style="background-color: #1E2130; padding: 20px; border-radius: 8px; border-left: 4px solid #9013FE; margin-top: 15px;">
    <strong>Estudo em destaque: {autor_selecionado}</strong><br><br>
    <span style="color: #d0d0d0; font-size: 16px;">{trabalhos_dict[autor_selecionado]}</span>
</div>
""", unsafe_allow_html=True)
