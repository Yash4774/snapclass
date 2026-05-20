import streamlit as st
from src.src_screens.database.db import enroll_student_to_subject
from src.src_screens.database.db import supabase
import time


@st.dialog("Enroll in Subject")
def enroll_dialog():

    st.write('Enter the subject code provided by your teacher to enroll:')
    
    join_code = st.text_input(
        ' ',
        placeholder='Eg. CS101'
    )

    join_code = join_code.strip().upper()

    if st.button('Enroll now', type='primary', width='stretch'):

        if join_code:

            res = supabase.table('subjects').select(
                'subject_id, name, subject_code'
            ).eq(
                'subject_code',
                join_code
            ).execute()


            if res.data:

                subject = res.data[0]

                student_id = st.session_state.student_data['student_id']

                enroll_student_to_subject(
                    student_id,
                    subject['subject_id']
                )

                st.success('Successfully Enrolled!')
                time.sleep(1)
                st.rerun()

            else:
                st.error('Invalid Subject Code')

        else:
            st.warning('Please enter a subject code')