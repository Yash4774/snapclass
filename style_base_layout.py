import streamlit as st



def style_background_home():

    st.markdown("""
    <style>

    .stApp{
        background:#5865F2 !important;
    }

    div[data-testid="stColumn"] > div{
        background-color:#E8E8FF !important;
        padding:2.5rem !important;
        border-radius:5rem !important;
    }

    </style>
    """, unsafe_allow_html=True)



def style_background_dashboard():

    st.markdown("""
    <style>

    .stApp{
        background:#E8E8FF !important;
    }

    div[data-testid="stColumn"] > div{
        background-color:#E8E8FF !important;
    }
    [data-testid="stWidgetLabel"] p{
    color:black !important;
    font-weight:600 !important;
    font-size:16px !important;

[data-testid="stTextInput"]{
    background:white !important;
    border-radius:18px !important;
}

[data-testid="stTextInput"] input{
    background:white !important;
    color:black !important;
    border:none !important;
    border-radius:12px !important;
    padding:8px 12px !important;
}
[data-testid="stTextInput"] div{
    border:none !important;
    box-shadow:none !important;
    background:white !important;
}
[data-testid="stTextInput"] div{
        border:none !important;
        box-shadow:none !important;
        background:white !important;
}

 </style>
    """, unsafe_allow_html=True)



def style_base_layout():

    st.markdown("""
    <style>

    #MainMenu, footer, header{
        visibility:hidden;
    }

    .block-container{
        padding-top:2rem !important;
    }

    </style>
    """, unsafe_allow_html=True)




    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                style="color:#2E2E2E;

                font-size: 2rem !important;
                style="color:#2E2E2E;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)