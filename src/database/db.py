from src.database.config import supabase
import bcrypt


def hash_pass(pw):
    return bcrypt.hashpw(pw.encode(),bcrypt.gensalt()).decode()


def check_pass(pw,hased):
    return bcrypt.checkpw(pw.encode(),hased.encode())

def check_teacher_exists(username):
    response = supabase.table("teachers").select("username").eq("username",username).execute()
    return  len(response.data) > 0 

def create_teacher(username,password,name):
    data ={"username":username,"password":hash_pass(password),"name":name}

    response = supabase.table("teachers").insert(data).execute()
    return response.data


def teacher_login(username,password):
    response = supabase.table("teachers").select("*").eq("username",username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password,teacher['password']):
            return teacher
        return None
    

def get_all_students():
    response = supabase.table('student').select("*").execute()
    return response.data


def create_student(new_name, face_embedding=None,voice_embedding=None):
    data = {'name':new_name,'face_embedding':face_embedding,'voice_embedding':voice_embedding}
    response =supabase.table('student').insert(data).execute()
    return response.data


def create_subject(sub_id,sub_name,section,teacher_id,join_code):
    data ={'subject_code':sub_id,'name':sub_name,'section':section,'teacher_id':teacher_id,'join_code':join_code}
    response =supabase.table('subjects').insert(data).execute()
    return response.data


def get_teacher_subjects(teacher_id):

    response = supabase.table('subjects').select("*,subject_student(count),attendance_log(time)").eq('teacher_id', teacher_id) .execute()
    subjects = response.data

    for sub in subjects:

        sub['total_students'] = (
            sub.get('subject_student', [{}])[0].get('count', 0)
            if sub.get('subject_student') else 0
        )

        attendance = sub.get('attendance_log', [])

        unique_sessions = len(
            set(log['time'] for log in attendance)
        )

        sub['total_classes'] = unique_sessions

        sub.pop('subject_student', None)
        sub.pop('attendance_log', None)

    return subjects


def enroll_student_to_subject(student_id,subject_id):
    data={'student_id':student_id,'subject_id':subject_id}
    response= supabase.table('subject_student').insert(data).execute()
    return response.data

def unenroll_student_to_subject(student_id,subject_id):
    response= supabase.table('subject_student').delete().eq('student_id',student_id).eq('subject_id',subject_id).execute()
    return response.data

def get_student_subjects(student_id):
    response = supabase.table('subject_student').select('*,subjects(*)').eq('student_id',student_id).execute()
    return response.data


def get_student_attendance(student_id):
    response = supabase.table('attendance_log').select('*,subjects(*)').eq('student_id',student_id).execute()
    return response.data

def create_attendance(logs):
    response = supabase.table('attendance_log').insert(logs).execute()

    return response.data



def  get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_log').select("*,subjects!inner(*)").eq('subjects.teacher_id',teacher_id).execute()
    return response.data