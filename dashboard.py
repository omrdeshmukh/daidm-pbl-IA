import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI-Powered Student Learning Path Optimizer Dashboard", layout="wide")

@st.cache_data

def load_data():
    return pd.read_excel("PBL_IA1_DAIDM_GJ25NS016.xlsx")

df = load_data()

# Define section names
sections = {
    "Overview": "Distribution of Learning Gain",
    "Learning Style": "Learning Style vs Learning Gain",
    "Quiz Scores": "Quiz Improvement (Initial vs Final)",
    "Engagement": "Engagement Level vs Learning Gain",
    "Device": "Device Usage Distribution",
    "3D View": "3D: Engagement vs Completion vs Gain"
}

# Sidebar navigation
st.sidebar.title("📋 Dashboard Menu")
selected_section = st.sidebar.radio("Jump to Section:", list(sections.keys()))

# Simulate avatar (Part 2 will animate and interact)
avatar_placeholder = st.empty()
avatar_placeholder.markdown("<img src='https://media.giphy.com/media/3o7aCVpH1EtsrG5kLK/giphy.gif' width='100' style='position:fixed; bottom:30px; left:30px;'>", unsafe_allow_html=True)

st.title("🤖 AI-Powered Student Insight Dashboard")
st.markdown("Navigate through the list to explore focused visualizations and actionable insights.")

# --- SECTION RENDERING BASED ON SELECTION ---
if selected_section == "Overview":
    st.header("📌 Distribution of Learning Gain")
    st.markdown("Understand how students are performing overall on the platform.")
    fig = px.histogram(df, x="Learning_Gain", nbins=20, color_discrete_sequence=["indianred"])
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "Learning Style":
    st.header("🎓 Learning Style vs Learning Gain")
    st.markdown("Which learning styles are most effective in boosting student performance?")
    fig = px.box(df, x="Learning_Style", y="Learning_Gain", color="Learning_Style")
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "Quiz Scores":
    st.header("📈 Quiz Improvement")
    st.markdown("See how student scores changed before and after content engagement.")
    fig = px.scatter(df, x="Quiz_Score_Initial", y="Quiz_Score_Final", color="Learning_Gain", size="Learning_Gain")
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "Engagement":
    st.header("🔥 Engagement Level vs Learning Gain")
    st.markdown("Higher engagement usually means better learning outcomes.")
    fig = px.box(df, x="Engagement_Level", y="Learning_Gain", color_discrete_sequence=["green"])
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "Device":
    st.header("📱 Device Usage Distribution")
    st.markdown("Identify which platforms students use most.")
    fig = px.pie(df, names="Device_Type", title="Device Usage")
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "3D View":
    st.header("🌐 3D Analysis: Engagement vs Completion vs Gain")
    st.markdown("Visualize key drivers of success in a 3D view.")
    fig = px.scatter_3d(df, x="Engagement_Level", y="Course_Completion_Rate", z="Learning_Gain", color="Learning_Style")
    st.plotly_chart(fig, use_container_width=True)

# Footer animation line
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Plotly | AI agent and insight engine coming up next →")
