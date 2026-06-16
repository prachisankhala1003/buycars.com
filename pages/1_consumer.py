import streamlit as st
from utils.predictor import predict_value
from utils.agents import ConsumerAgent
from utils.data_utils import search_cars, get_unique_makes, get_unique_models

st.set_page_config(page_title="Consumer Agent", page_icon="👤")

st.title("👤 Consumer Assistant")
st.subheader("Buy or Sell Your Car - Fair Market Prices")

agent = ConsumerAgent()

# Create two tabs: Buy and Sell
tab_buy, tab_sell = st.tabs(["🛒 Buy a Car", "💰 Sell Your Car"])

# ==================== BUY TAB ====================
with tab_buy:
    st.subheader("Browse Available Cars")
    
    st.info("""
    Search our inventory for the perfect car. All prices are fair market estimates.
    """)
    
    # Search filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        year_range = st.slider(
            "Year Range",
            min_value=2010,
            max_value=2026,
            value=(2015, 2026),
            step=1
        )
    
    with col2:
        make = st.selectbox(
            "Make",
            get_unique_makes(),
            key="buy_make"
        )
    
    with col3:
        model = st.selectbox(
            "Model",
            get_unique_models(make),
            key="buy_model"
        )
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        max_price = st.number_input(
            "Max Price",
            min_value=0,
            max_value=100000,
            value=50000,
            step=1000
        )
    
    with col5:
        condition = st.selectbox(
            "Condition",
            ["Any", "Excellent", "Good", "Fair", "Poor"],
            key="buy_condition"
        )
    
    with col6:
        st.write("")
        search_button = st.button("🔍 Search", type="primary", use_container_width=True)
    
    # Search and display results
    if search_button:
        results = search_cars(
            year_range=year_range,
            make=make,
            model=model,
            max_price=max_price,
            condition=condition
        )
        
        if len(results) > 0:
            st.success(f"Found {len(results)} car(s) matching your criteria!")
            
            st.divider()
            
            # Display each car as a card
            for idx, car in results.iterrows():
                col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
                
                with col1:
                    st.markdown(f"**{car['year']} {car['make']} {car['model']}**")
                    st.caption(f"{car['color']} • {car['condition']} • {car['mileage']:,} miles")
                
                with col2:
                    st.metric("Price", f"${car['price']:,.0f}")
                
                with col3:
                    st.metric("Year", car['year'])
                
                with col4:
                    st.metric("Mileage", f"{car['mileage']:,}")
                
                with col5:
                    if st.button("📋 Details", key=f"details_{car['id']}", use_container_width=True):
                        st.info(f"**Contact dealer for more info on this {car['year']} {car['make']} {car['model']}**")
                
                st.divider()
        else:
            st.warning("No cars found matching your criteria. Try adjusting your search filters.")

# ==================== SELL TAB ====================
with tab_sell:
    st.subheader("Get Your Car's Fair Market Value")
    
    st.info("""
    Fill in your car's details below and we'll provide a fair market estimate for your trade-in.
    """)
    
    # Vehicle input form
    col1, col2 = st.columns(2)
    
    with col1:
        year = st.number_input("Year", min_value=1990, max_value=2026, value=2015, key="sell_year")
        make = st.text_input("Make (e.g., Honda)", value="Honda", key="sell_make")
        model = st.text_input("Model (e.g., Civic)", value="Civic", key="sell_model")
    
    with col2:
        mileage = st.number_input("Mileage", min_value=0, max_value=500000, value=85000, step=1000, key="sell_mileage")
        condition = st.selectbox(
            "Condition",
            ["Excellent", "Good", "Fair", "Poor"],
            key="sell_condition"
        )
        color = st.text_input("Color (optional)", value="", key="sell_color")
    
    if st.button("💵 Get Valuation", type="primary", use_container_width=True):
        vehicle_data = {
            "year": year,
            "make": make,
            "model": model,
            "mileage": mileage,
            "condition": condition.lower(),
            "color": color
        }
        
        # Get prediction
        result = predict_value(vehicle_data)
        
        st.divider()
        st.subheader("📊 Your Car's Estimated Value")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Estimated Value", f"${result['predicted_value']:,.0f}")
        
        with col2:
            st.metric("Market Range Low", f"${result['market_range_low']:,.0f}")
        
        with col3:
            st.metric("Market Range High", f"${result['market_range_high']:,.0f}")
        
        st.warning(result['note'])
        
        st.divider()
        st.success(f"""
        ✅ **Fair Market Range**: ${result['market_range_low']:,.0f} – ${result['market_range_high']:,.0f}
        
        This range is what you can reasonably expect from a dealership trade-in. 
        Use this as leverage in your negotiation!
        """)
        
        st.info("""
        **💡 Tips for Getting the Best Trade-In Value:**
        - Clean your car thoroughly before appraisal
        - Bring maintenance records
        - Highlight any recent repairs or upgrades
        - Get multiple dealer appraisals
        """)

st.divider()
st.markdown("""
---
### Our Commitment
- ✅ Transparent, fair market-based valuations
- ✅ Privacy-focused (no internal cost data shared)
- ✅ Easy negotiation support
- ✅ No hidden fees or pressure
""")
