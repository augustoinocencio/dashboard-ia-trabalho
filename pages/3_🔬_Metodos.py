import streamlit as st

st.title("🔬 3. Métodos")
st.markdown("---")

st.markdown("""
### Natureza da Pesquisa
Este estudo caracteriza-se como uma pesquisa de **natureza qualitativa, exploratória e bibliográfica**[cite: 1]. O objetivo central é analisar os impactos da Inteligência Artificial Generativa no mercado de trabalho, focando nos efeitos de substituição e complementaridade[cite: 1].
""")

st.subheader("📚 Corpus de Análise (Os 5 Estudos)")
st.markdown("A pesquisa estruturou-se a partir da análise crítica de **cinco trabalhos científicos** de referência que abordam diferentes perspectivas sobre automação e emprego[cite: 1]:")

# Exibindo os estudos em cards organizados
estudos = [
    ("de Oliveira (2025)", "Analisa o impacto da inteligência artificial e automação no mercado de trabalho brasileiro, destacando desafios de produtividade e qualificação[cite: 1]."),
    ("de Araújo & Rayol (2024)", "Discute os impactos nas relações trabalhistas durante a Quarta Revolução Industrial e os desafios regulatórios do desemprego tecnológico[cite: 1]."),
    ("Zarifhonarvar (2023)", "Examina a economia do ChatGPT a partir de uma visão de mercado de trabalho, avaliando a exposição de ocupações intelectuais e científicas[cite: 1]."),
    ("Hartley et al. (2025)", "Investiga de forma empírica e econômica os efeitos da IA generativa sobre a produtividade e o emprego[cite: 1]."),
    ("Chen et al. (2025)", "Discute o dilema entre deslocamento (substituição) e complementaridade no impacto da IA sobre o mercado de trabalho[cite: 1].")
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
O estudo seguiu três etapas metodológicas[cite: 1]:
1. **Identificação conceitual:** Mapeamento de termos como automação, substituição, complementaridade e produtividade[cite: 1].
2. **Comparação de resultados:** Contraste das diferentes interpretações dos autores sobre o impacto nas ocupações[cite: 1].
3. **Aplicação de Matriz SWOT:** Organização dos fatores internos da tecnologia e externos do mercado de trabalho[cite: 1].
""")
