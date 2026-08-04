import streamlit as st

st.title("🔬 3. Métodos")
st.markdown("---")

st.markdown("""
### Natureza da Pesquisa
Este estudo caracteriza-se como uma pesquisa de **natureza qualitativa, exploratória e bibliográfica**. O objetivo central é analisar os impactos da Inteligência Artificial Generativa no mercado de trabalho, focando nos efeitos de substituição e complementaridade.
""")

st.subheader("📚 Corpus de Análise (Os 5 Estudos)")
st.markdown("A pesquisa estruturou-se a partir da análise crítica de **cinco trabalhos científicos** de referência que abordam diferentes perspectivas sobre automação e emprego:")

estudos = [
    ("de Oliveira (2025)", "Analisa o impacto da inteligência artificial e automação no mercado de trabalho brasileiro, destacando desafios de produtividade e qualificação."),
    ("de Araújo & Rayol (2024)", "Discute os impactos nas relações trabalhistas durante a Quarta Revolução Industrial e os desafios regulatórios do desemprego tecnológico."),
    ("Zarifhonarvar (2023)", "Examina a economia do ChatGPT a partir de uma visão de mercado de trabalho, avaliando a exposição de ocupações intelectuais e científicas."),
    ("Hartley et al. (2025)", "Investiga de forma empírica e econômica os efeitos da IA generativa sobre a produtividade e o emprego."),
    ("Chen et al. (2025)", "Discute o dilema entre deslocamento (substituição) e complementaridade no impacto da IA sobre o mercado de trabalho.")
]

for autor, desc in estudos:
    st.markdown(f"""
    <div style="background-color: #1E2130; padding: 12px; border-radius: 6px; margin-bottom: 10px; border-left: 3px solid #4A90E2;">
        <strong>{autor}</strong><br>
        <span style="color: #b0b0b0; font-size: 14px;">{desc}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
### ⚙️ Procedimento de Análise
O estudo seguiu três etapas metodológicas:
1. **Identificação conceitual:** Mapeamento de termos como automação, substituição, complementaridade e produtividade.
2. **Comparação de resultados:** Contraste das diferentes interpretações dos autores sobre o impacto nas ocupações.
3. **Aplicação de Matriz SWOT:** Organização dos fatores internos da tecnologia e externos do mercado de trabalho.
""")
