
import streamlit as st
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header_home import header_dashboard
from src.components.footer import footer_dashboard

from src.database.db import create_teacher,check_teacher_exists,teacher_login

def teacher_screen():
    style_base_layout()
    style_background_dashboard()
    
    
    if 'teacher_data' in st.session_state:
        teacher_dashboard()

    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login" :
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


    

def login_teacher(username,password):
    if not username or not password:
        return False
    teacher = teacher_login(username,password)

    if teacher:
        st.session_state.user_role='teacher'
        st.session_state.teacher_data=teacher
        st.session_state.is_loged_in = True
        return True

    return False

def teacher_dashboard():
    teacher_data=st.session_state.teacher_data
    
    st.header(f"""Hii {teacher_data["name"]}""")

def teacher_screen_login():
    col1,col2 =st.columns(2,vertical_alignment='center',gap='large')

    with col1:
        header_dashboard()
    with col2:
       if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
           st.session_state['login_type'] = None
           st.rerun()
    
    
    st.header("Login using password",text_alignment='center')
    
    st.space()
    st.space()
    teacher_username=st.text_input("Enter username",placeholder="enter your name")
    teacher_password=st.text_input("Enter Your Password",placeholder="password",type="password")

    st.divider()

    c1,c2 =st.columns(2)

    with c1:
       if st.button("Login",icon=":material/passkey:",shortcut="control+enter",type='secondary',width='stretch'):
           if login_teacher(teacher_username,teacher_password):
                st.toast("welcome back!",icon="👋")
                import time 
                time.sleep(1)
                st.rerun()
           else:
               st.error("Invalid Username or password")
    with c2:
        if st.button("Register Insted",icon=":material/passkey:",type='primary',width='stretch'):
            st.session_state['teacher_login_type'] = "register"

    
    footer_dashboard()


def register_teacher(teacher_username,teacher_name,teacher_password,teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_password:
        return False,"All Field  are  required !"
    
    if check_teacher_exists(teacher_username):
        return False,"username already taken"

    if teacher_password != teacher_pass_confirm:
        return False,"Password  missmatch"
    
    try:
        create_teacher(teacher_username,teacher_password,teacher_name)
        return True,"Successfully Register|  Login now!"
    except Exception as e:
        return False,"Unexpected Error! Retry"

# Register  Function

def teacher_screen_register():

    col1,col2 =st.columns(2,vertical_alignment='center',gap='large')

    with col1:
        header_dashboard()
    with col2:
       if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
           st.session_state['login_type'] = None
           st.rerun()



    st.header("Register your teacher profile",text_alignment='center')
     
    st.space()
    st.space()
    teacher_username=st.text_input("Enter username",placeholder="enter your name")
    teacher_name=st.text_input("Enter name",placeholder="enter your name")

    teacher_password=st.text_input("Enter Your Password",placeholder="password",type="password")
    teacher_pass_confirm = st.text_input("Confirm Your Password ",placeholder="password",type="password")
    st.divider()

    c1,c2 =st.columns(2)
    with c1:
       if st.button("Register Now",icon=":material/passkey:",shortcut="control+enter",type='secondary',width='stretch'):
           success,message = register_teacher(teacher_username,teacher_name,teacher_password,teacher_pass_confirm)
           if success:
                st.success(message)

                import time
                time.sleep(2)

                st.session_state.teacher_login_type = "login"
                st.rerun()
           else:
                st.error(message)


    with c2:
        if st.button("Login Insted",icon=":material/passkey:",type='primary',width='stretch'):
            st.session_state['teacher_login_type'] ="login"


    footer_dashboard()