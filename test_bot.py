import streamlit as st
from google import genai
import matplotlib.pyplot as plt

# Setup page title and description
st.set_page_config(page_title="AI Budget & Goal Planner", page_icon="💰", layout="wide")
st.title("💰 Smart AI Budget & Goal Planner")
st.write("Visualized data and automated AI insights for your financial health.")

# 1. Base Financial Inputs
with st.sidebar:
    st.header("📋 Enter Financial Details")
    income = st.number_input("Monthly Income ($)", min_value=0, value=4000, step=100)
    
    st.subheader("Monthly Expenses")
    rent = st.number_input("Rent / Mortgage ($)", min_value=0, value=1500, step=50)
    groceries = st.number_input("Groceries ($)", min_value=0, value=450, step=25)
    auto = st.number_input("Car & Insurance ($)", min_value=0, value=500, step=25)
    utilities = st.number_input("Utilities & Internet ($)", min_value=0, value=250, step=25)
    fun = st.number_input("Dining Out & Fun ($)", min_value=0, value=600, step=50)

    st.subheader("🎯 Savings Goal")
    goal_name = st.text_input("What are you saving for?", value="Emergency Fund")
    target_amount = st.number_input("Target Amount ($)", min_value=0, value=5000, step=100)

# Calculate 50/30/20 Categories mathematically from inputs
needs = rent + groceries + auto + utilities
wants = fun
total_expenses = needs + wants
savings_leftover = max(0, income - total_expenses)

# Create layout columns on the website screen
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Your Current 50/30/20 Breakdown")
    
    # Generate the Pie Chart data
    labels = ['Needs', 'Wants', 'Savings/Leftover']
    sizes = [needs, wants, savings_leftover]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    
    if income > 0:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)
    else:
        st.info("Enter your income in the sidebar to see your pie chart breakdown!")

with col2:
    st.subheader("🤖 AI Financial Consultation")
    
    if st.button("Analyze My Complete Budget & Goal"):
        with st.spinner("Analyzing your budget percentages..."):
            client = genai.Client()
            
            prompt = f"""
            You are an expert financial consultant. Analyze this user's budget against the 50/30/20 rule:
            
            FINANCIAL PROFILE:
            - Income: ${income}
            - Needs (Rent, Groceries, Car, Utilities): ${needs} ({ (needs/income)*100 if income else 0 }%)
            - Wants (Fun/Dining out): ${wants} ({ (wants/income)*100 if income else 0 }%)
            - Savings/Leftover: ${savings_leftover} ({ (savings_leftover/income)*100 if income else 0 }%)
            
            GOAL TRACKER:
            - Saving for: "{goal_name}"
            - Target Amount: ${target_amount}

            Provide a clear, brief breakdown evaluation:
            1. Tell them how their current calculated percentages stack up compared to the target 50% Needs, 30% Wants, 20% Savings benchmark.
            2. State exactly how many months it will take to reach their ${target_amount} goal based on their calculated savings.
            3. Provide one realistic tip to optimize their breakdown.
            """
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            
            st.markdown(response.text)


                                   
                                        
