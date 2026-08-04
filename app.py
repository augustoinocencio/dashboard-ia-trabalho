import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="IA Generativa no Mercado",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Identidade Visual (Inspirada em IA - Tons de Azul e Roxo)
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    h1 {
        background: -webkit-linear-gradient(45deg, #4A90E2, #9013FE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Arial', sans-serif;
    }
    .highlight-card {
        background-color: #1E2130;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #9013FE;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho e Título
st.title("Inteligência Artificial Generativa no Mercado de Trabalho")
st.subheader("Uma análise sobre substituição e complementaridade das competências profissionais")

st.markdown("---")

# 4. Apresentação Inicial
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🎯 Objetivo do Projeto
    Este dashboard interativo apresenta os resultados de uma pesquisa bibliográfica qualitativa sobre os impactos da Inteligência Artificial Generativa (IA Generativa) no mercado de trabalho.
    
    A pesquisa investiga se a integração dessas tecnologias atua como um fator de **substituição** ou de **complementaridade** das competências profissionais atuais, sintetizando diferentes perspectivas acadêmicas.
    """)

with col2:
    st.markdown("""
    <div class="highlight-card">
        <strong>Informações do Artigo</strong><br>
        👤 <em>Autor:</em> Augusto da Silva Inocencio<br>
        🎓 <em>Instituição:</em> UFPB<br>
        📚 <em>Natureza:</em> Revisão Bibliográfica<br>
        🔍 <em>Estudos Analisados:</em> 5 trabalhos
    </div>
    """, unsafe_allow_html=True)

st.info("👈 Utilize o menu lateral para navegar pelas seções do artigo.")
