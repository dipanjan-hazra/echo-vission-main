    
import streamlit as st
from src.database.db import create_subject
import segno
import io

@st.dialog('Share class link')
def share_subject_dialog(name,code,join_code):
    app_domain="echo-vission-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={join_code}"
    
    st.header("scan to join")
    qr =segno.make(join_url)
    out = io.BytesIO()

    qr.save(out,kind='png',scale=10,border=1)

    col1 , col2 = st.columns(2)

    with col1: 
        st.markdown("### copy link")
        st.code(join_url,language='text')
        st.code(join_code,language='text')
        st.info('Copy this  link  to share !')
    
    with col2:
        st.markdown("### Scan to join")
        st.image(out.getvalue(),caption='QR Code for class joining')        
