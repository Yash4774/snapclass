import streamlit as st
from src.src_screens.database.db import create_subject



@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.markdown("""
        <style>

        /* ALL TEXT */
        [data-testid="stDialog"] label,
        [data-testid="stDialog"] p,
        [data-testid="stDialog"] h1,
        [data-testid="stDialog"] h2,
        [data-testid="stDialog"] h3 {
            color: white !important;
        }

        /* INPUT BOX */
        [data-testid="stDialog"] input {
            color: white !important;
            background-color: #1f2430 !important;
            border: 1px solid #555 !important;
        }

        /* PLACEHOLDER */
        [data-testid="stDialog"] input::placeholder {
            color: #bdbdbd !important;
        }

        </style>
        """, unsafe_allow_html=True)
    
        
    st.write("Enter the details of new subject")
    sub_id = st.text_input("Subject Code", placeholder="CS101")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="A")


    if st.button("Create Subject Now", type='primary', width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject Created Succesfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str[e]}")

        else:
            st.warning("Please fill all the fields")
        

