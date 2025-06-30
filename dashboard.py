# ===== File: dashboard.py =====
import streamlit as st
import pandas as pd
import plotly.express as px
from ai_insight_engine import generate_insight

st.set_page_config(page_title="AI-Powered Student Learning Path Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("PBL_IA1_DAIDM_GJ25NS016.xlsx")

df = load_data()

# Sidebar navigation
sections = [
    "Overview",
    "Learning Style",
    "Quiz Scores",
    "Engagement",
    "Device",
    "3D View"
]
selected_section = st.sidebar.radio("📋 Dashboard Menu", sections)

# Filters (applies to all sections)
st.sidebar.markdown("---")
gender_filter = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=df["Gender"].unique())
device_filter = st.sidebar.multiselect("Device Type", df["Device_Type"].unique(), default=df["Device_Type"].unique())
style_filter = st.sidebar.multiselect("Learning Style", df["Learning_Style"].unique(), default=df["Learning_Style"].unique())
source_filter = st.sidebar.multiselect("Enrollment Source", df["Enrollment_Source"].unique(), default=df["Enrollment_Source"].unique())

filtered_df = df[
    df["Gender"].isin(gender_filter) &
    df["Device_Type"].isin(device_filter) &
    df["Learning_Style"].isin(style_filter) &
    df["Enrollment_Source"].isin(source_filter)
]

# Floating AI avatar
avatar_html = "<img src='https://media.giphy.com/media/3o7aCVpH1EtsrG5kLK/giphy.gif' width='100' style='position:fixed; bottom:20px; left:20px;'>"
st.markdown(avatar_html, unsafe_allow_html=True)

# Initialize state
if "insight" not in st.session_state:
    st.session_state.insight = "👋 Click 'Generate Insight' after selecting a section or data point."

# Title and guidance
st.title("🤖 AI-Powered Student Insight Dashboard")
st.markdown(st.session_state.insight)

# ---------- SECTION RENDERING ----------
if selected_section == "Overview":
    st.header("📌 Distribution of Learning Gain")
    st.markdown("Overall performance distribution across students.")
    fig = px.histogram(filtered_df, x="Learning_Gain", nbins=20, color_discrete_sequence=["indianred"])
    st.plotly_chart(fig, use_container_width=True)
    context = {"section":"Overview"}

elif selected_section == "Learning Style":
    st.header("🎓 Learning Style vs Learning Gain")
    st.markdown("Compare effectiveness of each learning style.")
    fig = px.box(filtered_df, x="Learning_Style", y="Learning_Gain", color="Learning_Style")
    st.plotly_chart(fig, use_container_width=True)
    context = {"section":"Learning Style"}

elif selected_section == "Quiz Scores":
    st.header("📈 Quiz Improvement")
    st.markdown("Initial vs. final quiz performance scatterplot.")
    fig = px.scatter(filtered_df, x="Quiz_Score_Initial", y="Quiz_Score_Final",
                     color="Learning_Gain", size="Learning_Gain")
    st.plotly_chart(fig, use_container_width=True)
    context = {"section":"Quiz Scores"}

elif selected_section == "Engagement":
    st.header("🔥 Engagement Level vs Learning Gain")
    st.markdown("Relationship between engagement and learning outcomes.")
    fig = px.box(filtered_df, x="Engagement_Level", y="Learning_Gain", color_discrete_sequence=["green"])
    st.plotly_chart(fig, use_container_width=True)
    context = {"section":"Engagement"}

elif selected_section == "Device":
    st.header("📱 Device Usage Distribution")
    st.markdown("Breakdown of platforms used by students.")
    fig = px.pie(filtered_df, names="Device_Type", title="Devices Used")
    st.plotly_chart(fig, use_container_width=True)
    context = {"section":"Device"}

elif selected_section == "3D View":
    st.header("🌐 3D Analysis: Engagement vs Completion vs Gain")
    st.markdown("Multi-dimensional view of key metrics.")
    fig = px.scatter_3d(filtered_df,
                        x="Engagement_Level",
                        y="Course_Completion_Rate",
                        z="Learning_Gain",
                        color="Learning_Style")
    st.plotly_chart(fig, use_container_width=True)
    context = {"section":"3D View"}

# ---------- AI Insight Generation ----------
if st.button("🧠 Generate AI Insight"):
    insight = generate_insight(context)
    st.session_state.insight = insight
    st.experimental_rerun()

# ---------- Footer ----------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, Plotly, and OpenAI GPT")
