
import streamlit as st
from src.database.db import create_subject

@st.dialog('Create New Subjects')
def create_subject_dialog(teacher_id):
    st.write("Enter the details  of  new subject")
    sub_id = st.text_input("Enter subject code" ,placeholder='E.g. CS101')
    sub_name = st.text_input("Enter Subject Name",placeholder='Ai/Ml')
    section = st.text_input("Section",placeholder='A')

    if st.button("Create subject now",type='primary',width='stretch'):
        
        if sub_id and sub_name and section:
            try:
                create_subject(sub_id,sub_name,section,teacher_id)
                st.toast(f"📙- {sub_name} create successfully!")
            except Exception as e:
               error_msg = str(e)
               if "duplicate key value violates unique constraint" in error_msg:
                    st.warning("⚠️ Subject already exists for this teacher.")
               else:
                    st.error(f"Subject not created! {e}")
        else:
            st.warning("pls field all the fields")