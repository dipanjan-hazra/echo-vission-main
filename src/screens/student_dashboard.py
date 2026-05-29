import streamlit as st
from src.components.header_home import header_dashboard
from src.components.footer import footer_dashboard

from src.components.dialog_enroll import enroll_dialog
from src.database.db import get_student_subjects,get_student_attendance,enroll_student_to_subject,unenroll_student_to_subject
from src.components.subject_card import subject_card
import time



def student_dashboard():
    student_data=st.session_state.student_data
    student_id = student_data['student_id']
    col1,col2 =st.columns(2,vertical_alignment='center',gap='large')

    with col1:
        header_dashboard()
    with col2:
       st.subheader(f"""Hii {student_data["name"]}""")
       if st.button("Logout",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
           st.session_state['is_logged_in'] = False
           del st.session_state.student_data
           st.rerun()
    

    st.space()
    c1,c2 =st.columns(2)

    with c1:
        st.header("Your Enrolled Subjects")
    with c2:
        if st.button("Enroll in subject",type='primary',width='stretch'):
            enroll_dialog()

    
    st.divider()

    with st.spinner('Loading Your enrolled subjects..'):
        subjects=get_student_subjects(student_id)
        logs = get_student_attendance(student_id)
    
    st.space()
    stats_map={}

    for log in  logs:
        sid = log['subject_id']

        if sid not  in stats_map:
            stats_map[sid] = {"total":0,"attendend":0}

        stats_map[sid]['total'] +=1

        if logs.get('is_present'):
            stats_map[sid]['total'] +=1


    cols = st.columns(2)

    for i,sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid=sub['subject_id'] 


        stats=stats_map.get(sid,{"total":0,"attended":0}) 
        def unenroll_button():
            if st.button("Unenroll from this course",type='tertiary',width='stretch',icon=":material/delete_forever:"): 
                unenroll_student_to_subject(student_id,sid)
                st.toast(f"Unenrolled from {sub['name']} successfully")
                time.sleep(1)
                st.rerun()

        
        with cols[i % 2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats= [
                    ('📆','Total',stats['total']),
                    ('✅','Attended',stats['attended']),

                ],
                footer_callback=unenroll_button
                )

    footer_dashboard()