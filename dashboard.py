import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI-Powered Student Dashboard", layout="wide")

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

# Simulate avatar
avatar_placeholder = st.empty()
avatar_placeholder.markdown("""
<img src='https://media.giphy.com/media/3o7aCVpH1EtsrG5kLK/giphy.gif' width='100' style='position:fixed; bottom:30px; left:30px;'>
""", unsafe_allow_html=True)

# Display avatar message
if "avatar_message" not in st.session_state:
    st.session_state.avatar_message = "👋 Hi! Click on a data point to see what I think."

st.toast(st.session_state.avatar_message, icon="🤖")

st.title("🤖 AI-Powered Student Insight Dashboard")
st.markdown("Navigate through the list to explore focused visualizations and actionable insights.")

# --- SECTION RENDERING BASED ON SELECTION ---
if selected_section == "Overview":
    st.header("📌 Distribution of Learning Gain")
    st.markdown("Understand how students are performing overall on the platform.")
    fig = px.histogram(df, x="Learning_Gain", nbins=20, color_discrete_sequence=["indianred"])
    clicked = st.plotly_chart(fig, use_container_width=True, key="overview")

elif selected_section == "Learning Style":
    st.header("🎓 Learning Style vs Learning Gain")
    st.markdown("Which learning styles are most effective in boosting student performance?")
    fig = px.box(df, x="Learning_Style", y="Learning_Gain", color="Learning_Style")
    clicked = st.plotly_chart(fig, use_container_width=True, key="style")

elif selected_section == "Quiz Scores":
    st.header("📈 Quiz Improvement")
    st.markdown("See how student scores changed before and after content engagement.")
    fig = px.scatter(df, x="Quiz_Score_Initial", y="Quiz_Score_Final", color="Learning_Gain", size="Learning_Gain")
    clicked = st.plotly_chart(fig, use_container_width=True, key="quiz")

elif selected_section == "Engagement":
    st.header("🔥 Engagement Level vs Learning Gain")
    st.markdown("Higher engagement usually means better learning outcomes.")
    fig = px.box(df, x="Engagement_Level", y="Learning_Gain", color_discrete_sequence=["green"])
    clicked = st.plotly_chart(fig, use_container_width=True, key="engage")

elif selected_section == "Device":
    st.header("📱 Device Usage Distribution")
    st.markdown("Identify which platforms students use most.")
    fig = px.pie(df, names="Device_Type", title="Device Usage")
    clicked = st.plotly_chart(fig, use_container_width=True, key="device")

elif selected_section == "3D View":
    st.header("🌐 3D Analysis: Engagement vs Completion vs Gain")
    st.markdown("Visualize key drivers of success in a 3D view.")
    fig = px.scatter_3d(df, x="Engagement_Level", y="Course_Completion_Rate", z="Learning_Gain", color="Learning_Style")
    clicked = st.plotly_chart(fig, use_container_width=True, key="3d")

# --- Insight logic for click interaction ---
if "insight_shown" not in st.session_state:
    st.session_state.insight_shown = False

clicked_data = st.session_state.get("plotly_click", None)

if clicked_data and not st.session_state.insight_shown:
    st.toast("📊 AI Insight: That point looks like a student who gained a lot from less effort!", icon="🧠")
    st.session_state.insight_shown = True

# Reset logic (optional refresh on navigation)
if st.button("🔄 Reset AI Agent"):
    st.session_state.avatar_message = "👋 I'm ready again. Click another graph!"
    st.session_state.insight_shown = False
    st.rerun()


# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Interactive agent powered by Plotly + GPT-ready hooks")
