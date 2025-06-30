# daidm-pbl-IA
# 📊 Student Learning Performance Dashboard

This is a comprehensive Streamlit dashboard for visualizing and analyzing student learning performance based on the `Learning_Gain` metric from the dataset `PBL_IA1_DAIDM_GJ25NS016.xlsx`. Designed for professors, academic leaders, and stakeholders to understand key trends, patterns, and engagement indicators at both macro and micro levels.

---

## 🚀 Features

✅ 20+ interactive data visualizations  
✅ Tabs for Overview, Learning Drivers, Engagement, and 3D Analysis  
✅ Filters for Gender, Device Type, Learning Style, and Enrollment Source  
✅ Sliders, dropdowns, pie charts, scatter plots, 3D plots and boxplots  
✅ Designed for strategic insight and decision-making

---

## 🗂️ Project Structure

```bash
student_learning_dashboard/
├── dashboard.py                       # Streamlit code
├── PBL_IA1_DAIDM_GJ25NS016.xlsx       # Dataset
├── requirements.txt                   # Python packages
├── README.md                          # Project description
└── .gitignore                         # Optional: exclude files
```

---

## 📥 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/student_learning_dashboard.git
cd student_learning_dashboard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard
```bash
streamlit run dashboard.py
```

---

## 📊 Data Columns
The dashboard analyzes the following features:

- **Demographics**: Age, Gender, Learning Style
- **Performance**: Quiz Scores, Learning Gain, Completion Rate
- **Engagement**: Time Spent, Help Requests, Satisfaction, Device
- **Behavioral**: Revisit Count, Enrollment Source, Session Duration

---

## 🌐 Deployment
To deploy this on **Streamlit Cloud**:
1. Push your code to GitHub.
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect GitHub and select your repo.
4. Set `dashboard.py` as the main file.
5. Click **Deploy**!

---

## 📬 Contact
For queries, improvements, or collaboration, please raise an issue or connect via your GitHub profile.

---

Built with ❤️ using Streamlit and Plotly.
