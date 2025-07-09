import streamlit as st
import pandas as pd
import plotly.express as px

# Load and clean column names
@st.cache_data
def load_data():
    df = pd.read_excel("Cleaned_And_Combined_Data_Updated.xlsx")
    df.rename(columns=lambda x: x.strip(), inplace=True)  # Remove extra spaces
    return df

df = load_data()

st.title("📊 Electricity Usage & Pricing Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filter Data")
utilities = st.sidebar.multiselect("Select Utility", options=df["Utility"].unique(), default=df["Utility"].unique())
zones = st.sidebar.multiselect("Select Congestion Zone", options=df["Congestion Zone"].unique(), default=df["Congestion Zone"].unique())
products = st.sidebar.multiselect("Select Product", options=df["Product"].unique(), default=df["Product"].unique())

filtered_df = df[
    (df["Utility"].isin(utilities)) &
    (df["Congestion Zone"].isin(zones)) &
    (df["Product"].isin(products))
]

# KPIs Section
st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Rows", len(filtered_df))
col2.metric("Unique Utilities", filtered_df["Utility"].nunique())
col3.metric("Source Files", filtered_df["Source File"].nunique())

# Monthly Rate Trends (First 12 months)
month_columns = [col for col in df.columns if "Month" in col and col.split()[0].isdigit()][:60]
if month_columns:
    st.subheader("📈 Monthly Rate Trend (First 60 Months)")
    avg_by_month = filtered_df[month_columns].mean().reset_index()
    avg_by_month.columns = ["Month", "Average Rate"]
    fig_line = px.line(avg_by_month, x="Month", y="Average Rate", markers=True, title="Average Rate by Month")
    st.plotly_chart(fig_line, use_container_width=True, key="line_chart")

# Load Factor Distribution
st.subheader("🧭 Load Factor Distribution")
fig_pie = px.pie(filtered_df, names="Load Factor", title="Load Factor Breakdown")
st.plotly_chart(fig_pie, use_container_width=True, key="pie_chart")

# Source File Frequency
st.subheader("📂 Data Source Distribution")
source_count_df = filtered_df["Source File"].value_counts().reset_index()
source_count_df.columns = ["Source File", "Count"]
fig_bar = px.bar(source_count_df, x="Source File", y="Count", title="Entries by Source File")
st.plotly_chart(fig_bar, use_container_width=True, key="bar_chart")

# Footer
st.markdown("📁 Data Source: `Cleaned_And_Combined_Data_Updated.xlsx`")
