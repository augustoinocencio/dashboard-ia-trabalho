import streamlit as st

st.title("🧠 2. Referencial Teórico")
st.markdown("---")

st.markdown("""
O referencial teórico da pesquisa fundamenta-se em três eixos principais que estruturam a discussão sobre a tecnologia e o mercado de trabalho atual[cite: 1]:
""")

# Utilizando abas (tabs) para organizar os conceitos de forma interativa
tab1, tab2, tab3 = st.tabs(["🤖 IA Generativa e LLMs", "⚖️ Substituição vs. Complementaridade", "🎓 Competências Profissionais"])

with tab1:
    st.subheader("Inteligência Artificial Generativa e Transformação Tecnológica")
    st.markdown("""
    * A **Inteligência Artificial (IA)** engloba técnicas computacionais capazes de executar atividades tradicionalmente humanas (aprendizado, reconhecimento de padrões e tomada de decisão)[cite: 1].
    * O surgimento dos **Grandes Modelos de Linguagem (LLMs)**, como o ChatGPT, representou uma mudança profunda: a tecnologia passou a impactar atividades **predominantemente cognitivas**, e não apenas trabalhos manuais ou repetitivos[cite: 1].
    """)

with tab2:
    st.subheader("Mecanismos de Impacto no Trabalho")
    col_sub, col_comp = st.columns(2)
    
    with col_sub:
        st.markdown("""
        <div style="background-color: #261a1a; padding: 15px; border-radius: 8px; border-left: 4px solid #ff4b4b;">
            <h4>🔴 Substituição</h4>
            <p>Ocorre quando sistemas tecnológicos assumem tarefas previsíveis, estruturadas e padronizadas, reduzindo a necessidade de certas funções profissionais[cite: 1].</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_comp:
        st.markdown("""
        <div style="background-color: #1a261a; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">
            <h4>🟢 Complementaridade</h4>
            <p>Ocorre quando a IA atua como apoio ao trabalhador, ampliando sua produtividade e eficiencia. A ocupação não é eliminada, mas a forma de execução é modificada[cite: 1].</p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.subheader("Competências Profissionais e Adaptação")
    st.markdown("""
    * Habilidades puramente repetitivas enfrentam maior risco de substituição[cite: 1].
    * Competências como **criatividade, pensamento crítico, comunicação e resolução de problemas** ganham relevância central[cite: 1].
    * A adaptação depende de estratégias de requalificação (*reskilling*) e aperfeiçoamento (*upskilling*), além de condições sociais e institucionais adequadas (especialmente no contexto brasileiro)[cite: 1].
    """)
