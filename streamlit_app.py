import streamlit as st

# Page config
st.set_page_config(
    page_title="BuyCars - AI-Powered Car Valuation",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and intro
st.title("🚗 BuyCars.com")
st.subheader("AI-Powered Car Valuation & Sales Support")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### 👤 Consumer Agent
    Get fair market valuations for your trade-in or find your next car.
    """)

with col2:
    st.success("""
    ### 💼 Sales Agent
    Data-driven insights for dealership appraisals and negotiations.
    """)

with col3:
    st.warning("""
    ### 📊 Executive Agent
    Strategic inventory and financial analysis.
    """)

st.divider()

st.markdown("""
## How It Works

Select an agent from the sidebar to get started:

1. **Consumer Agent** – Find fair market value for vehicles
2. **Sales Agent** – Access internal appraisal data and negotiation insights
3. **Executive Agent** – Monitor inventory health and financial metrics

---

*Powered by AI | Secured by Guardrails | Built for Results*
""")
