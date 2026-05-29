
import streamlit as st
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header_home import header_dashboard
from src.components.footer import footer_dashboard
import numpy as np
from PIL import Image

from src.pipelines.facepipeline import predict_attendance,get_face_embeddings,train_classifier
from src.pipelines.voicepipeline import get_voice_embedding
from src.database.db import get_all_students,create_student
import time

from src.screens.student_dashboard import student_dashboard




def student_screen():
    style_base_layout()
    style_background_dashboard()

    if 'student_data' in st.session_state:
        student_dashboard()
        return 
    

    col1,col2 =st.columns(2,vertical_alignment='center',gap='large')

    with col1:
        header_dashboard()
    with col2:
       if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
           st.session_state['login_type'] = None
           st.rerun()
    
    st.header("Login Using Face Id",text_alignment='center')
    st.space()

    show_registration = False
    camera_source = st.camera_input("Postion Your face in the center")
    
    if camera_source:
        img = np.array(Image.open(camera_source))
    
        with st.spinner('AI  is scanning...'):
            detected,all_ids,num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')
            
            elif (num_faces > 1):
                st.warning("multiple faces found")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id']==student_id),None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student['name']}")
                        time.sleep(1)
                        st.rerun()

                else:
                    st.info("Face Not  Recognized ! You Might be  a new  student :)")
                    show_registration =True
    
    if show_registration:
        
        with st.container(border=True):
            st.header("Register your self ")
            new_name= st.text_input("Enter Your  name",placeholder="E.g. Dipanjan Hazra")
            st.subheader('Optional : Voice Enrolement')
            st.info("Enroll Your for voice only attendance")

            audio_data = None

            try:
                audio_data = st.audio_input('Record a short pharse | Introduce your self')
            except Exception:
                st.error('Audio data Failed!')

            if st.button('Create Account',type='primary'):
                if new_name:
                    with st.spinner('Creating Profile...'):

                        img = np.array(Image.open(camera_source))
                        embeddings = get_face_embeddings(img)

                        if embeddings:
                            face_emb = embeddings[0].tolist()
                            voice_emb = None

                            if audio_data:
                                st.warning("audio data exist") #
                                
                                audio_data.seek(0)
                                audio_bytes = audio_data.read()

                                st.write("audio bytes length:", len(audio_bytes))
                                voice_emb= get_voice_embedding(audio_bytes)
                                st.write("voice embedding generated:", voice_emb is not None)

                            response_data = create_student(new_name,face_embedding=face_emb,voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f"Profile created | HI {new_name}😃 ")
                                time.sleep(1)
                                st.rerun()
                                        
                            else:
                                st.error("Couldn't capture your facial features for registraion")    
                else:
                    st.warning('Please enter Your name !')
    
    st.space()
    footer_dashboard()