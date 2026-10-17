import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Health & Wellness Coach",
    page_icon="💪",
    layout="wide"
)

# App Header
st.title("🌱 Unified Health & Wellness Coach")
st.markdown("Your all-in-one dashboard to track **Exercise**, **Nutrition**, and **Wearables** data.")

# Sidebar for User Profile
st.sidebar.header("User Profile")
user_name = st.sidebar.text_input("Name", "Alex Doe")
user_goal = st.sidebar.selectbox("Primary Goal", ["Weight Loss", "Muscle Gain", "Maintenance", "General Fitness"])

# Main Navigation Tabs
tab_exercise, tab_nutrition, tab_wearables = st.tabs([
    "🏋️ Exercise", 
    "🥗 Nutrition", 
    "⌚ Wearables"
])

# ==========================================
# TAB 1: EXERCISE
# ==========================================
with tab_exercise:
    st.header("Exercise & Workout Tracker")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Log a Workout")
        with st.form("workout_form"):
            workout_type = st.selectbox("Workout Type", ["Strength Training", "Running", "Cycling", "Yoga", "HIIT"])
            duration = st.slider("Duration (minutes)", 10, 180, 45)
            intensity = st.select_slider("Intensity", options=["Low", "Moderate", "High", "Extreme"])
            submitted = st.form_submit_button("Save Workout")
            
            if submitted:
                st.success(f"Logged {duration} mins of {workout_type} ({intensity} intensity)!")

    with col2:
        st.subheader("Weekly Fitness Summary")
        # Sample data for weekly activity
        chart_data = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Calories Burned": [350, 500, 200, 450, 600, 750, 300]
        })
        st.bar_chart(chart_data, x="Day", y="Calories Burned")

# ==========================================
# TAB 2: NUTRITION
# ==========================================
with tab_nutrition:
    st.header("Nutrition & Meal Planner")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Log Meal")
        meal_type = st.selectbox("Meal", ["Breakfast", "Lunch", "Dinner", "Snack"])
        food_item = st.text_input("Food Description", "Grilled chicken salad")
        calories = st.number_input("Estimated Calories (kcal)", min_value=0, max_value=3000, value=500)
        
        if st.button("Add to Daily Log"):
            st.info(f"Added {food_item} ({calories} kcal) to {meal_type}.")

    with col2:
        st.subheader("Daily Macro Breakdown")
        # Target vs Consumed metrics
        st.metric(label="Total Calories Consumed", value="1,850 kcal", delta="-150 kcal vs target")
        
        macro_data = pd.DataFrame({
            "Macro": ["Protein", "Carbs", "Fats"],
            "Grams": [130, 180, 60]
        })
        st.dataframe(macro_data, use_container_width=True)

# ==========================================
# TAB 3: WEARABLES
# ==========================================
with tab_wearables:
    st.header("Wearables & Biometrics Sync")
    
    st.markdown("Live data synced from your connected smart device.")
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.metric(label="Daily Steps", value="8,432", delta="12% vs yesterday")
    with metric_col2:
        st.metric(label="Resting Heart Rate", value="62 bpm", delta="-2 bpm")
    with metric_col3:
        st.metric(label="Sleep Duration", value="7h 45m", delta="+45m")
    with metric_col4:
        st.metric(label="Recovery Score", value="88%", delta="Good")
        
    st.subheader("Heart Rate Trend (Last 24 Hours)")
    hr_data = pd.DataFrame(
        np.random.randn(24, 1) * 10 + 70,
        columns=["Heart Rate (bpm)"]
    )
    st.line_chart(hr_data)
