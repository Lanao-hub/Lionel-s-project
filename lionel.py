import streamlit as st


if st.sidebar.button("Accueil",use_container_width=True):   
    st.title("Lionel Albert Nandy Amar OUDIANE")

    with st.expander("PROFIL"):
        st.write("Date de Naissance: 10/10/2005")
        st.write("Addresse: Gandigal,Mbour")
        st.markdown("""Technicien en production végétale et animale. Souhaitant """)

    with st.expander("PARCOURS"):
        st.write("Licence en science agricoles, alimentaires et nutritionnelles")
        st.write("Baccalaurioat Scientifique")
        
    with st.expander("COMPETENCE"):
        st.write("Gérance d'une exploitation agricole")
        st.write("Gérance d'une exploitation porcine et de volaille")
        st.write("Bureautique(Word,Excel,Powerpoint)")
if st.sidebar.button("Projet",use_container_width=True):
    st.header("Projet")
    st.write("Gestion d'un poulailler")
    with st.expander("Description"):
        st.markdown("""Gérer un poulailler de 100 poulets sur une période de 45 jours. Au terme duquel on a eu une perte de 5 poulets et le reste vendu 4000 FCFA""")
    with st.expander("Média"):
        st.image("1.jpg")
        st.image("2.jpg")
if st.sidebar.button("Contact", use_container_width=True):
    st.subheader("Contact")
    with st.expander("Contact"):
        st.write("Contact: +221 77 015 78 86")
    with st.expander("E-mail"):
        st.markdown("oudianelionel@gmail.com")
