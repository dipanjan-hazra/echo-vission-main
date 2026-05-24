import streamlit as st
from src.components.header_home import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout,style_background_home
def home_screen():

    header_home()
    style_background_home()
    style_base_layout()
    

    
    col1 ,col2 = st.columns(2,gap='large')

    with col1:
       st.header("I'm Teacher")
       st.image("https://i.ibb.co/jP5bsLJT/b0266a74-65ea-49a0-b718-a83afbcb2fb7.png",width=110)
       if st.button('Teacher Portal',type='primary',icon=':material/arrow_outward:',icon_position='right'):
           st.session_state['login_type']='teacher'
           st.rerun()
    with col2:
        st.header("I'm Student")
        st.image("https://i.ibb.co/FL30F3gv/845c1cdb-a666-4493-bafb-dbdd41177355.pnghttps://i.ibb.co/FL30F3gv/845c1cdb-a666-4493-bafb-dbdd41177355.png",width=100)
        if st.button('Student Portal',type='primary',icon=':material/arrow_outward:',icon_position='right'):
            st.session_state["login_type"] ='student'
            st.rerun()


    footer_home()