import streamlit as  st

from src.database.db import create_attendance



def show_attendance_result(df,logs):
    st.write('Please review attendance')
    st.dataframe(df,hide_index=True,width='stretch')

    col1,col2 = st.columns(2)

    with col1:
        if st.button('Discard',width='stretch'):
            st.session_state.voice_attendance_results=None
            st.session_state.attendance_images=[]
            st.rerun()


    with col2:
     
        if st.button('Confirm & Save', width='stretch', type='primary'):
            st.write("BUTTON CLICKED")

            result = create_attendance(logs)

            st.write("RESULT:")
            st.write(result)

            st.write("LOGS:")
            st.write(logs)

            st.stop()


@st.dialog("Attendance Reports")
def attendance_result_dialog(df,logs):
    show_attendance_result(df,logs)


