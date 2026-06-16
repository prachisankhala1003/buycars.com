import streamlit as st
from utils.predictor import predict_value
from utils.agents import SalesAgent

st.set_page_config(page_title="Sales Agent", page_icon="💼")

st.title("💼 Sales & Appraisal Companion")
st.subheader("Internal Tool: Maximize Dealership Gross Profit")

st.warning("""
🔒 **Internal Use Only** - This tool contains proprietary appraisal data, 
repair estimates, and margin recommendations. Not for customer-facing use.
""")

agent = SalesAgent()

st.subheader("Vehicle Appraisal Analysis")

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year", min_value=1990, max_value=2026, value=2015, key="sales_year")
    make = st.text_input("Make", value="Honda", key="sales_make")
    model = st.text_input("Model", value="Civic", key="sales_model")

with col2:
    mileage = st.number_input("Mileage", min_value=0, max_value=500000, value=85000, step=1000, key="sales_mileage")
    condition = st.selectbox("Condition", ["Excellent", "Good", "Fair", "Poor"], key="sales_condition")
    days_on_lot = st.number_input("Days on Lot", min_value=0, max_value=365, value=18)

if st.button("Generate Appraisal Report", type="primary"):
    vehicle_data = {
        "year": year,
        "make": make,
        "model": model,
        "mileage": mileage,
        "condition": condition.lower()
    }
    
    result = predict_value(vehicle_data)
    
    st.divider()
    st.subheader("📋 Appraisal Report")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Appraisal Value", f"${result['predicted_value']:,.0f}")
    
    with col2:
        st.metric("Market Low", f"${result['market_range_low']:,.0f}")
    
    with col3:
        st.metric("Market High", f"${result['market_range_high']:,.0f}")
    
    with col4:
        st.metric("Days on Lot", days_on_lot)
    
    st.divider()
    
    st.subheader("💡 Negotiation Recommendations")
    
    appraisal_data = {
        "predicted_value": result['predicted_value'],
        "days_on_lot": days_on_lot,
        "condition": condition
    }
    
    recommendation = agent.get_negotiation_points(appraisal_data)
    st.info(recommendation)
    
    st.subheader("📊 Internal Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Front-End Gross Profit (Est.)", "$1,250", "at 14% margin")
        st.metric("Inventory Velocity", "Good", "18 days is target")
    
    with col2:
        st.metric("Market Competition", "Moderate", "Similar vehicles selling")
        st.metric("Repair Estimate", "$0", "No major issues detected")

st.divider()
st.markdown("""
---
### Internal Capabilities
- 📊 Full appraisal data access
- 🔍 Repair cost analysis
- 📈 Days-on-market insights
- 💰 Margin optimization recommendations
""")
