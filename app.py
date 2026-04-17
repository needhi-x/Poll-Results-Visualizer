import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Poll Results Dashboard")

st.write("App is running...")  # Debug line

# Load Data safely
try:
    df = pd.read_csv("data/poll_data.csv")
    st.success("Data loaded successfully!")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Show dataset
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# Check columns
st.write("Columns in dataset:", df.columns)

# Sidebar filters
st.sidebar.header("🔍 Filters")

region = st.sidebar.selectbox("Select Region", ["All"] + list(df["Region"].unique()))
age_group = st.sidebar.selectbox("Select Age Group", ["All"] + list(df["Age_Group"].unique()))

# Apply filters
filtered_df = df.copy()

if region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region]

if age_group != "All":
    filtered_df = filtered_df[filtered_df["Age_Group"] == age_group]

# Response count
st.subheader("📊 Response Distribution")

response_counts = filtered_df["Response"].value_counts()

fig, ax = plt.subplots()
response_counts.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Pie chart
st.subheader("🥧 Response Share")

fig2, ax2 = plt.subplots()
response_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
st.pyplot(fig2)

# Region-wise analysis
st.subheader("🌍 Region-wise Analysis")

region_data = pd.crosstab(df["Region"], df["Response"], normalize="index") * 100
st.dataframe(region_data)

# Insight
st.subheader("🧠 Final Insight")

top_product = df["Response"].value_counts().idxmax()
st.success(f"Most Preferred Product: {top_product}")