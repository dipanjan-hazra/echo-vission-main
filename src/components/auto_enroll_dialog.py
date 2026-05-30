
import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("Quick Enrollment 🔍")
def auto_enroll_dialog(join_code):

    if 'student_data' not in st.session_state:
        st.warning("Please login or create an account first. Then  try  any  enrollment  method")


    student_id =st.session_state.student_data['student_id']

    res = supabase.table('subjects').select('subject_id,name').eq('join_code',join_code).execute()
    if not res.data:
        st.error('Join Code not found!')
        if st.button('Close'):
            st.query_params.clear()
            st.rerun()
        return
    
    subject=res.data[0]
    check = supabase.table('subject_student').select("*").eq('subject_id',subject['subject_id']).eq('student_id',student_id).execute()

    if check.data:
        st.info("You are already enrolled!")
        if st.button('Close'):
            st.query_params.clear()
            st.rerun()
        return

    st.markdown(f"Would You Like to enroll in **{subject['name']}**?")

    col1,col2 =st.columns(2)

    with col1:
        if st.button('No thanks'):
            st.query_params.clear()
            st.rerun()

    with col2: 
        if st.button('Yes Join now!',type='primary',width='stretch'):
            enroll_student_to_subject(student_id,subject['subject_id'])
            st.success('joined succesfully!')
            st.query_params.clear()
            time.sleep(2)
            st.rerun()
            