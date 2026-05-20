import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:white; border-left:8px solid #EB459E; padding:25px; border-radius: 20px; border: 1px solid black; margin-bottom:20px;">
        <h3 style="margin:0; color: #1e293b; font-size: 1.5rem;" >{name}</h3>
        <p style="color: #64748b; margin: 10px 0;">Code: <span style="background:#E0E3FF; color:#5865F2; padding: 2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        
        """
    if stats:
        html += """
        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:15px;">
        """

    for icon, label, value in stats:
        html += f"""
        <div style="
            background:white;
            color:black;
            padding:10px 16px;
            border-radius:14px;
            font-size:0.95rem;
            font-weight:600;
            border:1px solid #dcdcdc;
            box-shadow:0 2px 10px rgba(0,0,0,0.05);
        ">
            {icon} <b>{value}</b> {label}
        </div>
        """

    html += "</div>"
    
    
   
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()



    