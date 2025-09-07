import streamlit as st

st.set_page_config(page_title="🏠 Project Overview", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
        .card {
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 4px 12px rgba(0,0,0,0.2);
            margin-bottom: 20px;
            color: white;
        }
        .card h2 {
            color: #ffffff;
        }
        .card p, .card li {
            font-size: 16px;
            line-height: 1.6;
            color: #f8f9fa;
        }
        .blue-card {
            background: linear-gradient(135deg, #2980b9, #6dd5fa);
        }
        .green-card {
            background: linear-gradient(135deg, #27ae60, #6dd5c4);
        }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Welcome to the Project!")

st.markdown("""
<div class="card blue-card">
    <h2>📊 Part 1: Interactive Data Visualization App</h2>
    <p>
    This part of the project allows you to:
    <ul>
        <li>📂 Upload your dataset in CSV format</li>
        <li>🔍 Automatically detect numerical and categorical columns</li>
        <li>⚙️ Handle missing values automatically (Mean for numerical, Most Frequent for categorical)</li>
        <li>📈 Create interactive plots using <b>Plotly</b> (Line, Scatter, Histogram, Box, and Bar charts)</li>
    </ul>
    </p>
</div>

<div class="card green-card">
    <h2>📝 Part 2: My Notes App</h2>
    <p>
    This part of the project is designed for easy note-taking:
    <ul>
        <li>✍️ Add new notes quickly</li>
        <li>📋 View all your notes in an organized list</li>
        <li>✨ Modern UI with styled note cards</li>
    </ul>
    </p>
</div>
""", unsafe_allow_html=True)
