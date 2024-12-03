!pip install streamlit-option-menu
!pip install streamlit-authenticator

import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import json

# Initialisation du module d'authentification
with open('utilisateurs.json', 'r') as file:
    users = json.load(file)


authenticator = Authenticate(
    users, 
    "cookie_name", 
    "cookie_key", 
    30 
)

authenticator.login()

def page_accueil():
    st.title("Bienvenue sur la page d'accueil")
    st.markdown(
        """
        ![Welcome unicorn](https://media1.tenor.com/m/Cw9-JsdTFVEAAAAd/ta-da-izzy-moonbow.gif)
        """
    )

def page_photos():
    st.title("Voici mon album photo")
    st.write('ma collection de jeux de mots pourris')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('Json Statham')
        st.image('https://miro.medium.com/v2/resize:fit:720/1*UIMV2Y9vmJ616miOh5r9Fw.jpeg')

    with col2:
        st.write('Array Potter')
        st.image('https://i.redd.it/pxan6g2ruw051.png')

    with col3:
        st.write('Json array')
        st.image('https://preview.redd.it/wib3uomy1e151.jpg?auto=webp&s=b272a5e30ec737b39b0f7a675787780145dd0413')

def accueil():
    with st.sidebar:
        authenticator.logout()
        st.write(f'Bienvenue {st.session_state['name']}')
        selection = option_menu(
            menu_title = None,
            options = [
                "Accueil",
                "Photos"],
            icons = [
                'house',
                'images']
            )
            
        
    if selection == 'Accueil':
        page_accueil()

    elif selection == 'Photos':
        page_photos()



if st.session_state['authentication_status'] is False:
    st.error("Il semblerait qu'il y ait une erreur dans le mot de passe ou le nom d'utilisateur.")

elif st.session_state['authentication_status'] is None:
    st.warning("Les champs Username et Mot de passe doivent être remplis.")

elif st.session_state['authentication_status']:
    accueil()
    










