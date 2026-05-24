import streamlit as st
from google import genai

# Setup page title and description
st.set_page_config(page_title="AI Budget & Goal Planner", page_icon="💰")
st.title("💰 Smart AI Budget & Goal Planner")
st.write("Enter your financial details and savings goals to get a customized timeline.")

# 1. Base Financial Inputs
income = st.number_input("Monthly Income ($)", min_value=0, value=4000, step=100)

st.subheader("Monthly Expenses")
rent = st.number_input("Rent / Mortgage ($)", min_value=0, value=1500, step=50)
groceries = st.number_input("Groceries ($)", min_value=0, value=450, step=25)
auto = st.number_input("Car & Insurance ($)", min_value=0, value=500, step=25)
utilities = st.number_input("Utilities & Internet ($)", min_value=0, value=250, step=25)
fun = st.number_input("Dining Out & Fun ($)", min_value=0, value=600, step=50)

# 2. NEW FEATURE: Financial Goal Inputs
st.subheader("🎯 Financial Savings Goal")
goal_name = st.text_input("What are you saving for?", value="Emergency Fund")
target_amount = st.number_input("Target Amount ($)", min_value=0, value=5000, step=100)

# Calculate total expenses and current monthly surplus mathematically
total_expenses = rent + groceries + auto + utilities + fun
monthly_surplus = income - total_expenses

# 3. Trigger the AI Analysis
if st.button("Generate My Financial Plan & Timeline"):
    if monthly_surplus <= 0:
        st.error(f"Your current monthly expenses (${total_expenses}) are equal to or higher than your income. You don't have a surplus to put toward your goal right now. Try adjusting your expenses below!")
    else:
        with st.spinner("Analyzing your budget and calculating your timeline..."):
            client = genai.Client()
            
            # Pack all data into a detailed prompt for Gemini
            prompt = f"""
            You are an expert financial consultant. Analyze this user's budget and target goal:
            
            FINANCIAL PROFILE:
            - Monthly Income: ${income}
            - Total Monthly Expenses: ${total_expenses}
            - Current Leftover Savings Capacity: ${monthly_surplus} per month
            
            SAVINGS TARGET:
            - Goal: "{goal_name}"
            - Target Amount: ${target_amount}

            Provide a beautifully structured, encouraging response with:
            1. **Timeline Calculation**: State exactly how many months it will take them to reach the ${target_amount} goal if they save their full current surplus (${monthly_surplus}/month).
            2. **Milestone Breakdown**: Break the timeline down into realistic checkpoints (e.g., 25% marks, halfway mark) so they can track progress.
            3. **AI Fast-Track Recommendation**: Give 2 specific, actionable budgeting tips based on their expense profile to cut back slightly and achieve the goal even faster.
            
            Keep the tone motivating and use bold headings and clean markdown lists.
            """
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            
            st.success("Analysis Complete!")
            st.markdown(response.text)


                                   
                                        
