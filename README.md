# Electricity-Usage-Pricing-Dashboard

An interactive dashboard built with **Streamlit**, **Pandas**, and **Plotly** that visualizes electricity usage, pricing trends, and source file contributions across various congestion zones and load factors.

🚀 **Live App**:  
👉 [Click to View Dashboard](https://electricity-usage-pricing-dashboard-6wty7zduqfrbpbgekymz32.streamlit.app/)

---

📌 Features

- 🎛️ **Filter Panel**: Interactively filter data by:
  - Utility
  - Congestion Zone
  - Product

- 📈 **Monthly Rate Trend**:
  - Line chart showing the average rate for the first 12 months

- 🧭 **Load Factor Distribution**:
  - Pie chart breakdown based on load factors

- 📂 **Source File Distribution**:
  - Bar chart showing how many entries came from each source file

- 📊 **Key Metrics (KPIs)**:
  - Total Rows
  - Unique Utilities
  - Source File Count


📁 Dataset Details

The dataset used (`Cleaned_And_Combined_Data_Updated.xlsx`) contains:
- Monthly rate columns: `1 Month` to `60 Month`
- Attributes such as:
  - `Utility`
  - `Congestion Zone`
  - `Product`
  - `Load Factor`
  - `Annual Usage`
  - 
## 🛠 Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| Python      | Data manipulation & backend      |
| Streamlit   | Frontend and web app deployment  |
| Pandas      | Data handling and filtering      |
| Plotly      | Interactive visualizations       |
| Openpyxl    | Excel file support               |
