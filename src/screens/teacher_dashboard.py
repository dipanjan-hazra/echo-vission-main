import streamlit as st
from src.components.header_home import header_dashboard
from src.components.footer import footer_dashboard
from src.components.dialog import create_subject_dialog
from src.database.db import get_teacher_subjects
from src.components.subject_card import subject_card

from src.components.dialog_share_subjects import share_subject_dialog

def teacher_dashboard():
    teacher_data=st.session_state.teacher_data
    col1,col2 =st.columns(2,vertical_alignment='center',gap='large')

    with col1:
        header_dashboard()
    with col2:
       st.subheader(f"""Hii {teacher_data["name"]}""")
       if st.button("Logout",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
           st.session_state['is_logged_in'] = False
           del st.session_state.teacher_data
           st.rerun()
    

    st.space()

    if 'current_teacher_tab' not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'
    tab1 ,tab2,tab3  = st.columns(3)

    with tab1:
        type1 ='primary' if st.session_state.current_teacher_tab =='take_attendance' else 'tertiary'
        if st.button('Take attendance',width='stretch',icon=':material/ar_on_you:',type=type1):
            st.session_state.current_teacher_tab ='take_attendance'
            st.rerun()

    with tab2:
        type2 = 'primary' if st.session_state.current_teacher_tab =='manage_subjects' else 'tertiary'
        if st.button('Manage Subjects',width='stretch',icon=':material/book_ribbon:',type=type2):
            st.session_state.current_teacher_tab ='manage_subjects'
            st.rerun()

    with tab3:
        type3 ='primary' if st.session_state.current_teacher_tab =='attendance_records' else 'tertiary'
        if st.button('Attendance Records',type=type3,width='stretch',icon=':material/cards_stack:'):
            st.session_state.current_teacher_tab ='attendance_records'
            st.rerun()



    st.divider()

    if st.session_state.current_teacher_tab == 'take_attendance' :
        teacher_tab_take_attendance()
    
    if st.session_state.current_teacher_tab == 'manage_subjects' :
        teacher_tab_manage_subject()   

    if st.session_state.current_teacher_tab == 'attendance_records' :
        teacher_tab_attendance_record()

    footer_dashboard()
   



def teacher_tab_take_attendance():
    st.header('Take Ai Attendance')


# manage subject page

def teacher_tab_manage_subject():
    # st.header('Manage subject')

    teacher_id = st.session_state.teacher_data['teacher_id']

    col1,col2 = st.columns(2)

    with col1:
        st.header('Manage Subjects',width='stretch')

    with col2:
       if st.button('create new subjects', width='stretch'):
           create_subject_dialog(teacher_id)

    # List  all  subjects 
    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("👥","Students",sub['total_students']),
                ("👨‍🏫","Students",sub['total_classes'])
            ]
            def share_btn():
                if st.button(f"Share code:{sub['name']}",key=f"share_{sub['subject_code']}",icon=":material/share:"):
                    share_subject_dialog(sub['name'],sub['subject_code'])
                st.space()

            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=stats,
                footer_callback=share_btn
                )

    else:
        st.info('no subject found')  

def teacher_tab_attendance_record():
    st.header(' Attendance Record')