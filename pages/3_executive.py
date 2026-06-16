import streamlit as st
from utils.agents import ExecutiveAgent

st.set_page_config(page_title="Executive Dashboard", page_icon="📊")

st.title("📊 Executive Decision Support")
st.subheader("Inventory Health & Financial Analysis")

st.warning("""
🔒 **Executive Use Only** - Strategic financial data for GSM/CFO decision-making.
""")

agent = ExecutiveAgent()

# Key Metrics
st.subheader("Inventory Health Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Inventory Value", "$2.3M", "📦 Capital tied up")

with col2:
    st.metric("Average Turn Time", "24 days", "🚀 Target: 20 days")

with col3:
    st.metric("Gross Margin", "14.2%", "📉 -0.8% vs last month")

with col4:
    st.metric("Aging Inventory Risk", "18%", "⚠️ >40 days old")

st.divider()

# Financial Summary
st.subheader("Monthly Financial Performance")

financial_summary = agent.get_financial_summary({})
st.success(financial_summary)

st.divider()

# Risk Analysis
st.subheader("⚠️ Risk Assessment")

risk_col1, risk_col2 = st.columns(2)

with risk_col1:
    st.warning("""
    ### 🔴 High Priority
    - 18% of inventory over 40 days
    - Gross margin down 0.8% MoM
    - Capital utilization at 87%
    """)

with risk_col2:
    st.info("""
    ### 💡 Recommendations
    - Promote aging inventory (>40 days)
    - Reduce new wholesale purchases
    - Focus on faster-moving segments
    """)

st.divider()

# Velocity Dashboard
st.subheader("📈 Inventory Velocity")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Turn Time Trend", "24 days", "-2 days improvement")

with col2:
    st.metric("Monthly Throughput", "32 vehicles", "+8% vs forecast")

with col3:
    st.metric("Projected Monthly Margin", "$28,400", "Based on current pace")

st.divider()

st.markdown("""
---
### Strategic Insights
- 🎯 Inventory turnover is tracking below target
- 💰 Margin compression driven by aging inventory
- 📊 Recommend promotional strategy on vehicles >40 days
- 🚀 Capital reallocation opportunity identified
""")
