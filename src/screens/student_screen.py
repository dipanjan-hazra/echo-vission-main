
import streamlit as st
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header_home import header_dashboard
from src.components.footer import footer_dashboard
import numpy as np

from PIL import Image

def student_screen():
    style_base_layout()
    style_background_dashboard()
    col1,col2 =st.columns(2,vertical_alignment='center',gap='large')

    with col1:
        header_dashboard()
    with col2:
       if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
           st.session_state['login_type'] = None
           st.rerun()
    
    st.header("Login Using Face Id",text_alignment='center')
    st.space()

   
    camera_source = st.camera_input("Postion Your face in the center")
    
    if camera_source:
        np.array(Image.open(camera_source))
    st.space()
    footer_dashboard()