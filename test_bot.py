import math

import matplotlib.pyplot as plt
import streamlit as st
from google import genai


st.set_page_config(page_title="AI Budget & Goal Planner", page_icon="$", layout="wide")
st.title("Smart AI Budget & Goal Planner")
st.write("Visualized data and automated AI insights for your financial health.")

with st.sidebar:
    st.header("Enter Financial Details")
    income = st.number_input("Monthly Income ($)", min_value=0, value=4000, step=100)

    st.subheader("Needs")
    rent = st.number_input("Rent / Mortgage ($)", min_value=0, value=1500, step=50)
    groceries = st.number_input("Groceries ($)", min_value=0, value=450, step=25)
    auto = st.number_input("Car Payment & Insurance ($)", min_value=0, value=500, step=25)
    gas_transportation = st.number_input("Gas / Transportation ($)", min_value=0, value=150, step=25)
    utilities = st.number_input("Utilities & Internet ($)", min_value=0, value=250, step=25)
    phone = st.number_input("Phone Bill ($)", min_value=0, value=80, step=10)
    health = st.number_input("Medical / Health ($)", min_value=0, value=100, step=25)
    debt = st.number_input("Debt Payments ($)", min_value=0, value=200, step=25)

    st.subheader("Wants")
    fun = st.number_input("Dining Out & Fun ($)", min_value=0, value=350, step=50)
    subscriptions = st.number_input("Subscriptions ($)", min_value=0, value=60, step=10)
    personal = st.number_input("Clothing / Personal Care ($)", min_value=0, value=100, step=25)
    gifts = st.number_input("Gifts / Donations ($)", min_value=0, value=50, step=25)
    household = st.number_input("Household Items ($)", min_value=0, value=75, step=25)

    st.subheader("Investments")
    investments = st.number_input("Monthly Investments ($)", min_value=0, value=200, step=25)
    annual_return = st.slider("Estimated Annual Return (%)", min_value=0.0, max_value=15.0, value=7.0, step=0.5)
    investment_years = st.slider("Investment Timeline (Years)", min_value=1, max_value=40, value=20, step=1)

    st.subheader("Savings Goal")
    goal_name = st.text_input("What are you saving for?", value="Emergency Fund")
    target_amount = st.number_input("Target Amount ($)", min_value=0, value=5000, step=100)

needs = rent + groceries + auto + gas_transportation + utilities + phone + health + debt
wants = fun + subscriptions + personal + gifts + household
total_expenses = needs + wants + investments
net_cash_flow = income - total_expenses
savings_leftover = max(0, net_cash_flow)
savings_and_investments = investments + savings_leftover
months_to_goal = math.ceil(target_amount / savings_leftover) if savings_leftover else None
monthly_return = (annual_return / 100) / 12
investment_growth = []

for year in range(investment_years + 1):
    months = year * 12
    if monthly_return:
        future_value = investments * (((1 + monthly_return) ** months - 1) / monthly_return)
    else:
        future_value = investments * months
    investment_growth.append((year, future_value))

expense_details = {
    "Rent / Mortgage": rent,
    "Groceries": groceries,
    "Car & Insurance": auto,
    "Gas / Transportation": gas_transportation,
    "Utilities & Internet": utilities,
    "Phone": phone,
    "Medical / Health": health,
    "Debt": debt,
    "Dining Out & Fun": fun,
    "Subscriptions": subscriptions,
    "Clothing / Personal Care": personal,
    "Gifts / Donations": gifts,
    "Household Items": household,
    "Investments": investments,
}

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Your Current 50/30/20 Breakdown")

    metric1, metric2, metric3 = st.columns(3)
    metric1.metric("Income", f"${income:,.0f}")
    metric2.metric("Expenses", f"${total_expenses:,.0f}")
    metric3.metric("Left Over", f"${net_cash_flow:,.0f}")

    labels = ["Needs", "Wants", "Savings/Investments"]
    sizes = [needs, wants, savings_and_investments]
    colors = ["#ff9999", "#66b3ff", "#99ff99"]

    if income > 0:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
        ax.axis("equal")
        st.pyplot(fig)
    else:
        st.info("Enter your income in the sidebar to see your pie chart breakdown!")

    st.subheader("Expense Details")
    bar_fig, bar_ax = plt.subplots(figsize=(8, 5))


                                   
                                        
