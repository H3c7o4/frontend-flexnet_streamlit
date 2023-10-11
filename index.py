import streamlit as st
from pages.main import landing_page
from pages.recommendations import show_recommendation


#st.set_page_config(
#    page_title="Flexnet",
#    page_icon=":clapper:",
#    layout="wide",
#    initial_sidebar_state="expanded",
#    menu_items={
#        'Get Help': 'https://www.extremelycoolapp.com/help',
#        'Report a bug': "mailto:hectorvladitok@gmail.com",
#        'About': "# This is a header. This is an *extremely* cool app!"
#    }
#)

landing_page()
start = st.link_button("Get started", "../recommendations")

