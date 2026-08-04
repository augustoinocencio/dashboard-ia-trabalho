import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="IA Generativa no Mercado",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Identidade Visual
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

# 3. Cabeçalho e Título da Introdução
st.title("1. Introdução")
st.subheader("Inteligência Artificial Generativa no Mercado de Trabalho")

st.markdown("---")

# 4. Conteúdo
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Contextualização e Objetivo
    O avanço acelerado da Inteligência Artificial Generativa (IA Generativa), exemplificada por grandes modelos de linguagem (LLMs), tem transformado profundamente a dinâmica do mercado de trabalho global e nacional.
    
    Este estudo tem como objetivo principal analisar como essas tecnologias impactam as atividades profissionais, investigando o duplo efeito de **substituição** de tarefas rotineiras e **complementaridade** em funções que exigem maior cognição e julgamento humano.
    
    ### Relevância do Tema
    Compreender essas mudanças é fundamental para antecipar tendências ocupacionais, identificar riscos de desemprego tecnológico e apontar caminhos para a requalificação profissional (*reskilling* e *upskilling*).
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
