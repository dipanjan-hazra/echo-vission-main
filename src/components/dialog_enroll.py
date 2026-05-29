import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("Enroll in subjects")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher to enroll")
    join_code=st.text_input('Subject Code',placeholder='Eg. A3F9K2').strip()

    if st.button('Enroll now',type='primary',width='stretch'):
        if join_code:
            res = supabase.table('subjects').select('subject_id,name,subject_code,join_code,section,teacher_id').eq('join_code',join_code).single().execute()

            if res.data:
                subject = res.data
                student_id = st.session_state.student_data['student_id']

                check = supabase.table('subject_student').select("*").eq('subject_id',subject['subject_id']).eq('student_id',student_id).execute()

                if check.data:
                    st.warning('You are already enrolled in this program')
                else:
                    enroll_student_to_subject(student_id,subject['subject_id'])
                    st.success('Succesfully enrolled')
                    time.sleep(1) 
                    st.rerun()     
        
        else:
            st.warning('Please enter a subject code')