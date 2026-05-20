import streamlit as st

def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-left:-40px";>
        <img src="{logo_url}" height="100" />
        <h1 style="text-align:center; color:#E0E3FF;">
            SNAP<br>CLASS
        </h1>
    </div>
    """, unsafe_allow_html=True)



def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
    <div style="display:flex;  align-items:center; justify-content:center; gap:10px; margin-left:0px";>
        <img src="{logo_url}" height="85" />
        <h2 style="text-align:left; color:#5865F2; margin:0; line-height:1.1; white-space:nowrap;">SNAP<br>CLASS</h2>
    </div>
    """, unsafe_allow_html=True)
