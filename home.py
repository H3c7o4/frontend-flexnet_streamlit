import streamlit as st
from pages.main import landing_page
from pages.recommendations import show_recommendation
hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}

footer {
    visibility:visible;
}

footer:after {
  content:'Copyright © 2023: Flexnet';
  display:block;
  color:tomato;
  position:relative;
}
</style>
"""


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

st.markdown(hide_menu, unsafe_allow_html=True)
landing_page()
start = st.link_button("Get started", "../recommendations")

