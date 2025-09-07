import streamlit as st

st.set_page_config(page_title="📝 My Notes App", page_icon="📒", layout="wide")

st.markdown("""
    <style>
        .main {
            padding: 20px;
            border-radius: 12px;
        }
        .stTextInput>div>div>input {     
            border-radius: 8px;  
            border: 2px solid #4CAF50;
        }
        .note-box {
            background: linear-gradient(135deg, #2980b9, #6dd5fa);
            padding: 12px;
            margin-bottom: 12px;
            border-radius: 12px;
            box-shadow: 1px 2px 6px rgba(0,0,0,0.3);
            font-size: 16px;
            color: white; /* ✅ white text for dark mode */
        }
    </style>    
""", unsafe_allow_html=True)

st.title("📒 Add Your Notes Here!!")

if "List_Notes" not in st.session_state:
    st.session_state["List_Notes"] = []

text = st.text_input("💡 Enter Your Note Here:")

if st.button("✅ Add Note"):    
    if text.strip():  
        st.session_state["List_Notes"].append(text.strip())
        st.success("✨ Note added successfully!")
    else:
        st.warning("⚠️ Please enter a valid note before adding.")

if st.session_state["List_Notes"]:   
    st.subheader("🗂️ Your Notes:")    
    for idx, note in enumerate(st.session_state["List_Notes"], start=1):
        st.markdown(f"<div class='note-box'>📝 <b>{idx}.</b> {note}</div>", unsafe_allow_html=True)
