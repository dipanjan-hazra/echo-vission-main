import streamlit as st
def footer_home():
    st.markdown("""
        <div style="
            bottom: 10px;
            width: 100%;
            text-align: center;
            font-size: 14px;
        ">
           <p style="color:white;font-weight:bold; margin:0;"> Created by Dipanjan Hazra </p>
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    st.markdown("""
        <div style="
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            font-size: 14px;
            padding: 12px 0;
            background-color: transparent;
            z-index: 999;
        ">
           <p style="color:black; font-weight:bold; margin:0;">
               Created by Dipanjan Hazra
           </p>
        </div>
    """, unsafe_allow_html=True)