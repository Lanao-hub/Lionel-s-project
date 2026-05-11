import streamlit as st


   
st.title("Lionel Albert Nandy Amar OUDIANE")
st.header("A propos de moi")
st.markdown("""Technicien supérieur en production végétale et animale. Souhaitant exprimer ses compétences dans le domaine agronomique à travers les plus grands de ce domaine """)

st.subheader("INFO")
st.write("Date de Naissance: 10/10/2005")
st.write("Addresse: Gandigal,Mbour")        

st.subheader("PARCOURS")
st.write("Licence en science agricoles, alimentaires et nutritionnelles")
st.write("Baccalauriat Scientifique")
        
st.header("Compétence")
st.write("Gestion d'une exploitation agricole")
st.write("Gestion d'une exploitation porcine et de volaille")
st.write("Analyse de sols")
st.write("Nutrition et développement des plantes")
st.write("Bureautique(Word,Excel,Powerpoint)")

st.header("Projet")
with st.expander("Cliquer pour en savoir plus"):
    
    st.write("Gestion d'un poulailler")
    st.markdown("""Gérer un poulailler de 100 poulets sur une période de 45 jours. Au terme duquel on a eu une perte de 5 poulets et le reste vendu 4000 FCFA l'unité""")
    st.image("1.jpg")
    st.image("2.jpg")

with st.sidebar:
    st.title("Contact")
    
    st.markdown("Mail: oudianelionel@gmail.com")
    st.markdown("Réactif et disponible, je réponds généralement à vos mail en moins de quelques heures.")
