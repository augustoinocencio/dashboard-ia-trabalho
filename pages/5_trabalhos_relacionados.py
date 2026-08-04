import streamlit as st

st.title("📚 5. Trabalhos Relacionados")
st.markdown("---")

st.markdown("""
A literatura recente aborda os impactos da IA Generativa a partir de diferentes prismas metodológicos e econômicos. O quadro abaixo sintetiza as principais referências discutidas no artigo[cite: 1]:
""")

trabalhos = [
    ("de Oliveira (2025)", "Analisa a automação no mercado brasileiro, apontando que trabalhadores com menor acesso à qualificação enfrentam maiores barreiras de adaptação tecnológica[cite: 1]."),
    ("de Araújo & Rayol (2024)", "Discutem os reflexos da Quarta Revolução Industrial nas relações de trabalho, enfatizando os riscos de desemprego tecnológico e a urgência de regulação[cite: 1]."),
    ("Zarifhonarvar (2023)", "Mapeia a economia do ChatGPT, demonstrando que profissões intelectuais, administrativas e científicas sofrem forte alteração devido ao processamento automatizado de dados[cite: 1]."),
    ("Hartley et al. (2025)", "Evidenciam empiricamente os ganhos de produtividade e a redução do tempo de execução de tarefas promovidos pela IA[cite: 1]."),
    ("Chen et al. (2025)", "Investigam o dilema entre deslocamento e complementaridade, reforçando o caráter heterogêneo da tecnologia nas funções corporativas[cite: 1].")
]

for autor, desc in trabalhos:
    st.markdown(f"""
    <div style="background-color: #1E2130; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #9013FE;">
        <strong>{autor}</strong><br>
        <span style="color: #d0d0d0; font-size: 14px;">{desc}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
### 🔍 Diferencial deste Estudo
Enquanto os trabalhos da literatura focam em eixos isolados (seja o mercado brasileiro, regulação ou métricas de ocupação), este artigo **integra essas diferentes perspectivas** por meio de uma análise comparativa e de uma matriz SWOT unificada[cite: 1].
""")
