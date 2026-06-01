import streamlit as st
import numpy as np
import time
from style_base_layout import style_base_layout, style_background_dashboard
from PIL import Image
from  src_screens.components.header import header_dashboard
from  src_screens.components.footer import footer_dashboard

from  src_screens.database.db import (
    get_all_students,
    create_student,
    get_student_subjects,
    get_student_attendance,
    unenroll_student_to_subject
)

from  src_screens.components.dialog_enroll import enroll_dialog
from  src_screens.components.dialog_auto_enroll import auto_enroll_dialog
from  src_screens.components.subject_card import subject_card

from  pipelines.voice_pipeline import get_voice_embedding

from  pipelines.face_pipeline import (
    predict_attendance,
    get_face_embedding,
    train_classifier
)
def student_dashboard():
    join_code = st.query_params.get("join-code")

    if join_code and 'auto_enroll_done' not in st.session_state:
        st.session_state.auto_enroll_done = True
        auto_enroll_dialog(join_code)

    if 'student_data' not in st.session_state:
        st.error('No student data found!')
        return

    student_data = st.session_state.student_data
    style_background_dashboard()
    style_base_layout()

    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
       st.markdown(
            f"""
            <h1 style='color:black; font-size:42px; font-weight:700;white-space:nowrap; margin:0; line-height:1.2'>
                Welcome,<br>
                  {student_data['name']}
            </h1>
            """,
            unsafe_allow_html=True
)
       if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()


    st.space()

    left, right = st.columns([3, 1])
    with left:
        st.markdown(
            """
            <h1 style="
                color:#111;
                font-size:72px;
                font-weight:900;
                line-height:0.85;
                letter-spacing:-4px;
                margin-top:10px;
                margin-left:-100px;
                font-family:'Arial Black', sans-serif;
                white-space:nowrap;
                width:900px;
            ">
                Your Enrolled<br>
                Subjects
            </h1>
            """,
            unsafe_allow_html=True
)
  
      

       

               
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your enrolled subjects...'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}

        stats_map[sid]['total'] +=1

        for log in logs:
            if log.get('is_present'):
                stats_map[sid]['attended'] +=1


    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node
        sid = sub['subject_id']

        stats = stats_map.get(sid, {"total": 0, "attended": 0} )
        def unenroll_button():
                if st.button('Unenroll from this course', type='tertiary', width='stretch', icon=':material/delete_forever:', key=f'unenroll_{sub["subject_id"]}'):
                    unenroll_student_to_subject(student_id, sid)
                    st.toast(f'Unenrolled from {sub['name']} successfully')
                    st.rerun()
                
        
        with left:
            subject_card(
                name = sub['name'],
                code = sub['subject_code'],
                section = sub['section'],
                stats = [
                    ('🗓️', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),


                ],
                footer_callback=unenroll_button




            )

    footer_dashboard()
 


def student_screen():


    style_background_dashboard()
    style_base_layout()


    if "student_data" in st.session_state:
        student_dashboard()
        return
    
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
    st.markdown("""
            <h1 style="
                text-align:center;
                color:#111111;
                font-size:60px;
                font-weight:900;
                margin-top:25px;
                margin-bottom:35px;
                letter-spacing:-2px;
                line-height:1;
                font-family:'Arial Black', sans-serif;
            ">
                Login Using<br>Face ID
            </h1>
        """, unsafe_allow_html=True)
    st.space()
    st.space()
    
    show_registration = False
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        img = np.array(Image.open(photo_source))
        st.markdown("""
            <style>
            div[data-testid="stSpinner"] p {
                color: black !important;
                font-weight: 700 !important;
                font-size: 20px !important;
            }
            </style>
            """, unsafe_allow_html=True)

        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')
            elif num_faces >1:
                st.warning('Multiple faces found')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id']==student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        join_code = st.query_params.get("join-code")
                        show_registration=True


                        st.session_state.student_data = student

                        if join_code and not show_registration:
                            auto_enroll_dialog(join_code)
                        st.toast(f"Welcome Back 👋 {student.get('name') or student.get('student_name')}")
                        time.sleep(1)
                else:
                    st.info('Face not recognized! You might be a new student!')
                    show_registration = True
    if show_registration:
        with st.container(border=True):
            st.markdown(
                    """
                    <h1 style="
                        color:black;
                        font-size:52px;
                        font-weight:900;
                        line-height:1;
                        letter-spacing:-2px;
                        margin-bottom:25px;
                        font-family:'Arial Black', sans-serif;
                    ">
                        Register New Profile
                    </h1>
                    """,
                    unsafe_allow_html=True
)
            new_name = st.text_input("Enter your name", placeholder='E.g. Yash Sinha')
            st.markdown(
                    """
                    <h3 style="
                        color:black;
                        font-size:24px;
                        font-weight:700;
                        margin-top:-10px;
                        margin-bottom:25px;
                        font-family:Arial, sans-serif;
                    ">
                        Optional: Voice Enrollment
                    </h3>
                    """,
                    unsafe_allow_html=True
)

            st.info("Enroll your for voice only attendance")


            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like I am present, My name is Sahil.')
            except Exception:
                st.error('Audio Data failed!')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings= get_face_embedding(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Couldnt capture your facial features for registration')

                else:
                    st.warning('Please enter your name!')


        
    footer_dashboard()