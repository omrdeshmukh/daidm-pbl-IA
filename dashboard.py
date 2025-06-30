import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Learning Performance Dashboard", layout="wide")

@st.cache_data

def load_data():
    return pd.read_excel("PBL_IA1_DAIDM_GJ25NS016.xlsx")

df = load_data()

# Sidebar Filters
st.sidebar.header("🔎 Filter Options")
gender_filter = st.sidebar.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique())
device_filter = st.sidebar.multiselect("Device Type", df["Device_Type"].unique(), default=df["Device_Type"].unique())
style_filter = st.sidebar.multiselect("Learning Style", df["Learning_Style"].unique(), default=df["Learning_Style"].unique())
source_filter = st.sidebar.multiselect("Enrollment Source", df["Enrollment_Source"].unique(), default=df["Enrollment_Source"].unique())

filtered_df = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Device_Type"].isin(device_filter)) &
    (df["Learning_Style"].isin(style_filter)) &
    (df["Enrollment_Source"].isin(source_filter))
]

st.title("🎓 Student Learning Performance Dashboard")
st.markdown("This platform gives detailed insights into student performance and engagement metrics using **Learning Gain** as the outcome indicator.")

# Tabs
overview, drivers, engagement, advanced = st.tabs(["📌 Overview", "📈 Learning Drivers", "🖥️ Platform Engagement", "🌐 Advanced 3D Views"])

with overview:
    st.header("📌 Overview")

    st.subheader("1. Distribution of Learning Gain")
    st.markdown("Understand how students are performing overall on the platform.")
    fig = px.histogram(filtered_df, x="Learning_Gain", nbins=20, color_discrete_sequence=["indianred"])
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("2. Learning Gain by Gender")
    st.markdown("Are there any performance gaps between genders?")
    fig = px.box(filtered_df, x="Gender", y="Learning_Gain", color="Gender")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("3. Learning Style vs Learning Gain")
    st.markdown("Analyze which learning styles are driving higher gains.")
    fig = px.box(filtered_df, x="Learning_Style", y="Learning_Gain", color="Learning_Style")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("4. Content Type Used vs Learning Gain")
    st.markdown("Some content types might be more effective.")
    fig = px.box(filtered_df, x="Content_Type_Used", y="Learning_Gain", color="Content_Type_Used")
    st.plotly_chart(fig, use_container_width=True)

with drivers:
    st.header("📈 Learning Drivers")

    st.subheader("5. Quiz Improvement (Initial vs Final)")
    st.markdown("See how much quiz scores improved after module completion.")
    fig = px.scatter(filtered_df, x="Quiz_Score_Initial", y="Quiz_Score_Final", color="Learning_Gain", size="Learning_Gain")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("6. Time Spent on Modules vs Learning Gain")
    fig = px.scatter(filtered_df, x="Time_Spent_on_Modules", y="Learning_Gain", color="Learning_Style", size="Learning_Gain")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("7. Engagement Level vs Learning Gain")
    fig = px.box(filtered_df, x="Engagement_Level", y="Learning_Gain", color_discrete_sequence=["green"])
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("8. Satisfaction Rating vs Learning Gain")
    fig = px.box(filtered_df, x="Satisfaction_Rating", y="Learning_Gain", color_discrete_sequence=["blue"])
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("9. Completion Rate vs Learning Gain")
    fig = px.scatter(filtered_df, x="Course_Completion_Rate", y="Learning_Gain", color="Device_Type")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("10. Help Requests vs Learning Gain")
    fig = px.scatter(filtered_df, x="Help_Request_Count", y="Learning_Gain", color="Enrollment_Source")
    st.plotly_chart(fig, use_container_width=True)

with engagement:
    st.header("🖥️ Platform Engagement")

    st.subheader("11. Device Usage Distribution")
    fig = px.pie(filtered_df, names="Device_Type", title="Device Usage Distribution")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("12. Enrollment Source Distribution")
    fig = px.pie(filtered_df, names="Enrollment_Source", title="Where are students coming from?")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("13. Technical Issues vs Learning Gain")
    fig = px.box(filtered_df, x="Technical_Issues_Encountered", y="Learning_Gain", color_discrete_sequence=["red"])
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("14. Session Duration vs Learning Gain")
    fig = px.scatter(filtered_df, x="Average_Session_Duration_Minutes", y="Learning_Gain", color="Gender")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("15. Module Revisit Count vs Learning Gain")
    fig = px.scatter(filtered_df, x="Module_Revisit_Count", y="Learning_Gain", color="Learning_Style")
    st.plotly_chart(fig, use_container_width=True)

with advanced:
    st.header("🌐 Advanced 3D Analysis")

    st.subheader("16. Quiz Improvement in 3D")
    fig = px.scatter_3d(filtered_df, x="Quiz_Score_Initial", y="Quiz_Score_Final", z="Learning_Gain", color="Gender")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("17. Engagement vs Completion vs Gain")
    fig = px.scatter_3d(filtered_df, x="Engagement_Level", y="Course_Completion_Rate", z="Learning_Gain", color="Device_Type")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("18. Age vs Session Duration vs Gain")
    fig = px.scatter_3d(filtered_df, x="Age", y="Average_Session_Duration_Minutes", z="Learning_Gain", color="Learning_Style")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | Data Source: Internal Platform Logs")
