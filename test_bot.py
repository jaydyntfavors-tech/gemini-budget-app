import math

import matplotlib.pyplot as plt
import streamlit as st
from google import genai


st.set_page_config(
    page_title="AI Budget & Goal Planner",
    page_icon="💰",
    layout="wide",
)

st.title("💰 Smart AI Budget & Goal Planner")
st.write("Detailed budget analysis, savings projections, debt review, and AI insights for your financial plan.")


def money(value):
    return f"${value:,.2f}"


def percent(value, total):
    if total <= 0:
        return 0
    return (value / total) * 100


def months_to_goal(target, monthly_savings):
    if target <= 0:
        return 0
    if monthly_savings <= 0:
        return None
    return math.ceil(target / monthly_savings)


with st.sidebar:
    st.header("📋 Financial Details")

    income = st.number_input("Monthly Income After Taxes ($)", min_value=0, value=4000, step=100)
    other_income = st.number_input("Other Monthly Income ($)", min_value=0, value=0, step=50)
    total_income = income + other_income

    st.subheader("Monthly Needs")
    rent = st.number_input("Rent / Mortgage ($)", min_value=0, value=1500, step=50)
    groceries = st.number_input("Groceries ($)", min_value=0, value=450, step=25)
    auto = st.number_input("Car Payment, Gas & Insurance ($)", min_value=0, value=500, step=25)
    utilities = st.number_input("Utilities & Internet ($)", min_value=0, value=250, step=25)
    healthcare = st.number_input("Healthcare / Insurance ($)", min_value=0, value=150, step=25)
    childcare = st.number_input("Childcare / Family Support ($)", min_value=0, value=0, step=25)
    other_needs = st.number_input("Other Required Bills ($)", min_value=0, value=0, step=25)

    st.subheader("Monthly Wants")
    dining = st.number_input("Dining Out ($)", min_value=0, value=250, step=25)
    entertainment = st.number_input("Entertainment / Subscriptions ($)", min_value=0, value=150, step=25)
    shopping = st.number_input("Shopping / Personal Spending ($)", min_value=0, value=200, step=25)
    travel = st.number_input("Travel / Events ($)", min_value=0, value=0, step=25)
    other_wants = st.number_input("Other Flexible Spending ($)", min_value=0, value=0, step=25)

    st.subheader("Debt Payments")
    credit_card_payment = st.number_input("Credit Card Minimum Payments ($)", min_value=0, value=150, step=25)
    student_loan_payment = st.number_input("Student Loan Payment ($)", min_value=0, value=0, step=25)
    personal_loan_payment = st.number_input("Personal Loan Payment ($)", min_value=0, value=0, step=25)
    total_debt_balance = st.number_input("Total Debt Balance ($)", min_value=0, value=3000, step=100)
    average_debt_apr = st.slider("Average Debt APR (%)", min_value=0.0, max_value=35.0, value=19.0, step=0.5)

    st.subheader("🎯 Savings Goal")
    current_emergency_fund = st.number_input("Current Emergency Fund ($)", min_value=0, value=500, step=100)
    goal_name = st.text_input("What are you saving for?", value="Emergency Fund")
    target_amount = st.number_input("Target Amount ($)", min_value=0, value=5000, step=100)
    extra_goal_contribution = st.number_input("Extra Monthly Goal Contribution ($)", min_value=0, value=0, step=25)


needs = rent + groceries + auto + utilities + healthcare + childcare + other_needs
wants = dining + entertainment + shopping + travel + other_wants
debt_payments = credit_card_payment + student_loan_payment + personal_loan_payment
total_expenses = needs + wants + debt_payments
monthly_leftover = total_income - total_expenses
available_for_savings = max(0, monthly_leftover + extra_goal_contribution)
remaining_goal = max(0, target_amount - current_emergency_fund)
goal_months = months_to_goal(remaining_goal, available_for_savings)

recommended_needs = total_income * 0.50
recommended_wants = total_income * 0.30
recommended_savings = total_income * 0.20

needs_gap = needs - recommended_needs
wants_gap = wants - recommended_wants
savings_gap = recommended_savings - max(0, monthly_leftover)

housing_ratio = percent(rent, total_income)
debt_ratio = percent(debt_payments, total_income)
savings_rate = percent(max(0, monthly_leftover), total_income)

emergency_low = needs * 3
emergency_high = needs * 6
estimated_monthly_interest = total_debt_balance * (average_debt_apr / 100 / 12)


st.subheader("Budget Snapshot")
metric_cols = st.columns(4)
metric_cols[0].metric("Monthly Income", money(total_income))
metric_cols[1].metric("Total Expenses", money(total_expenses))
metric_cols[2].metric("Monthly Leftover", money(monthly_leftover))
metric_cols[3].metric("Savings Rate", f"{savings_rate:.1f}%")

if monthly_leftover < 0:
    st.error(
        f"Your budget is short by {money(abs(monthly_leftover))} each month. "
        "Review flexible spending, debt payments, or income options before increasing savings goals."
    )
elif savings_rate < 10:
    st.warning("Your savings rate is below 10%. This plan may feel tight unless your goal timeline is flexible.")
else:
    st.success("Your budget has positive monthly cash flow. Now the main question is where that leftover money should go.")


tab_overview, tab_costs, tab_goal, tab_ai = st.tabs(
    ["📊 Breakdown", "🧾 Cost Analysis", "🎯 Goal Plan", "🤖 AI Consultation"]
)

with tab_overview:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Current Budget Breakdown")
        labels = ["Needs", "Wants", "Debt Payments", "Leftover"]
        sizes = [needs, wants, debt_payments, max(0, monthly_leftover)]
        colors = ["#ff9999", "#66b3ff", "#ffcc66", "#99dd99"]

        if total_income > 0 and sum(sizes) > 0:
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
            ax.axis("equal")
            st.pyplot(fig)
        else:
            st.info("Enter your income and expenses to see your budget breakdown.")

    with col2:
        st.subheader("50/30/20 Comparison")
        comparison = {
            "Category": ["Needs", "Wants", "Savings / Leftover"],
            "Current": [money(needs), money(wants), money(max(0, monthly_leftover))],
            "Current %": [
                f"{percent(needs, total_income):.1f}%",
                f"{percent(wants, total_income):.1f}%",
                f"{savings_rate:.1f}%",
            ],
            "Recommended": [
                money(recommended_needs),
                money(recommended_wants),
                money(recommended_savings),
            ],
        }
        st.dataframe(comparison, use_container_width=True, hide_index=True)

        st.write("**Key Ratios**")
        st.write(f"- Housing ratio: **{housing_ratio:.1f}%** of income")
        st.write(f"- Debt payment ratio: **{debt_ratio:.1f}%** of income")
        st.write(f"- Monthly debt interest estimate: **{money(estimated_monthly_interest)}**")

with tab_costs:
    st.subheader("Detailed Monthly Cost Review")

    expense_rows = {
        "Expense": [
            "Rent / Mortgage",
            "Groceries",
            "Car, Gas & Insurance",
            "Utilities & Internet",
            "Healthcare",
            "Childcare / Family Support",
            "Other Required Bills",
            "Dining Out",
            "Entertainment / Subscriptions",
            "Shopping / Personal Spending",
            "Travel / Events",
            "Other Flexible Spending",
            "Debt Payments",
        ],
        "Monthly Cost": [
            money(rent),
            money(groceries),
            money(auto),
            money(utilities),
            money(healthcare),
            money(childcare),
            money(other_needs),
            money(dining),
            money(entertainment),
            money(shopping),
            money(travel),
            money(other_wants),
            money(debt_payments),
        ],
        "% of Income": [
            f"{percent(rent, total_income):.1f}%",
            f"{percent(groceries, total_income):.1f}%",
            f"{percent(auto, total_income):.1f}%",
            f"{percent(utilities, total_income):.1f}%",
            f"{percent(healthcare, total_income):.1f}%",
            f"{percent(childcare, total_income):.1f}%",
            f"{percent(other_needs, total_income):.1f}%",
            f"{percent(dining, total_income):.1f}%",
            f"{percent(entertainment, total_income):.1f}%",
            f"{percent(shopping, total_income):.1f}%",
            f"{percent(travel, total_income):.1f}%",
            f"{percent(other_wants, total_income):.1f}%",
            f"{percent(debt_payments, total_income):.1f}%",
        ],
    }

    st.dataframe(expense_rows, use_container_width=True, hide_index=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Needs vs. 50% Target", money(needs_gap), delta="over target" if needs_gap > 0 else "under target")
    col2.metric("Wants vs. 30% Target", money(wants_gap), delta="over target" if wants_gap > 0 else "under target")
    col3.metric("Savings Gap to 20%", money(max(0, savings_gap)))

    st.write("**Cost Flags**")
    if housing_ratio > 30:
        st.write("- Housing is above 30% of income, which can make the rest of the budget harder to balance.")
    if debt_ratio > 15:
        st.write("- Debt payments are above 15% of income. Consider a payoff strategy before adding aggressive new costs.")
    if wants_gap > 0:
        st.write(f"- Flexible spending is {money(wants_gap)} above the 30% benchmark.")
    if needs_gap <= 0 and wants_gap <= 0 and monthly_leftover >= recommended_savings:
        st.write("- Your major categories fit the 50/30/20 benchmark well.")

with tab_goal:
    st.subheader(f"Goal Plan: {goal_name}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Current Emergency Fund", money(current_emergency_fund))
    col2.metric("Remaining Goal", money(remaining_goal))
    col3.metric("Monthly Available", money(available_for_savings))

    if goal_months is None:
        st.error("At the current pace, this goal will not be reached because there is no monthly money available for savings.")
    elif goal_months == 0:
        st.success("This goal is already funded.")
    else:
        st.success(f"Estimated time to reach this goal: {goal_months} month(s).")

        projection_months = list(range(goal_months + 1))
        projected_savings = [
            min(target_amount, current_emergency_fund + (month * available_for_savings))
            for month in projection_months
        ]

        fig, ax = plt.subplots()
        ax.plot(projection_months, projected_savings, marker="o", color="#2e86de")
        ax.axhline(target_amount, color="#27ae60", linestyle="--", label="Target")
        ax.set_xlabel("Months")
        ax.set_ylabel("Projected Savings")
        ax.set_title("Savings Progress Projection")
        ax.legend()
        st.pyplot(fig)

    st.write("**Emergency Fund Benchmark**")
    st.write(
        f"Based on required monthly needs of {money(needs)}, a 3-6 month emergency fund is "
        f"approximately **{money(emergency_low)} to {money(emergency_high)}**."
    )

with tab_ai:
    st.subheader("🤖 AI Financial Consultation")
    st.write("Generate a detailed, personalized review using the numbers entered in the sidebar.")

    if st.button("Analyze My Complete Budget & Goal"):
        if total_income <= 0:
            st.error("Please enter monthly income before requesting an AI analysis.")
        else:
            with st.spinner("Analyzing your budget, costs, debt, and goal timeline..."):
                client = genai.Client()

                prompt = f"""
                You are a practical financial planning assistant. Analyze this user's monthly budget.
                Use plain language. Do not provide investment, tax, or legal advice. Focus on budgeting,
                savings behavior, debt pressure, and cost tradeoffs.

                MONTHLY INCOME:
                - Main income: {money(income)}
                - Other income: {money(other_income)}
                - Total income: {money(total_income)}

                MONTHLY NEEDS:
                - Rent / mortgage: {money(rent)}
                - Groceries: {money(groceries)}
                - Car, gas, insurance: {money(auto)}
                - Utilities and internet: {money(utilities)}
                - Healthcare: {money(healthcare)}
                - Childcare / family support: {money(childcare)}
                - Other required bills: {money(other_needs)}
                - Total needs: {money(needs)} ({percent(needs, total_income):.1f}%)

                MONTHLY WANTS:
                - Dining out: {money(dining)}
                - Entertainment / subscriptions: {money(entertainment)}
                - Shopping / personal spending: {money(shopping)}
                - Travel / events: {money(travel)}
                - Other flexible spending: {money(other_wants)}
                - Total wants: {money(wants)} ({percent(wants, total_income):.1f}%)

                DEBT:
                - Monthly debt payments: {money(debt_payments)} ({debt_ratio:.1f}%)
                - Total debt balance: {money(total_debt_balance)}
                - Average APR: {average_debt_apr:.1f}%
                - Estimated monthly interest: {money(estimated_monthly_interest)}

                SAVINGS AND GOAL:
                - Current emergency fund: {money(current_emergency_fund)}
                - Goal name: {goal_name}
                - Goal target: {money(target_amount)}
                - Remaining goal amount: {money(remaining_goal)}
                - Monthly leftover after expenses: {money(monthly_leftover)}
                - Extra monthly goal contribution: {money(extra_goal_contribution)}
                - Total available for goal: {money(available_for_savings)}
                - Estimated months to goal: {"not reachable" if goal_months is None else goal_months}
                - Emergency fund range: {money(emergency_low)} to {money(emergency_high)}

                BENCHMARKS:
                - 50/30/20 target needs: {money(recommended_needs)}
                - 50/30/20 target wants: {money(recommended_wants)}
                - 50/30/20 target savings: {money(recommended_savings)}

                Provide:
                1. A short budget health score from 1-10 with the reason.
                2. A category-by-category analysis of needs, wants, debt, and savings.
                3. The exact goal timeline and whether it is realistic.
                4. Three specific cost changes with estimated dollar amounts.
                5. A recommended next-month action plan.
                6. A brief caution if their cash flow, debt, or emergency fund looks risky.
                7. recommendations on inprovment of their budget
                """

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )

                st.markdown(response.text)



                                   
                                        
