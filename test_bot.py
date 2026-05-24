import streamlit as st
from google import genai

# Setup page title and description
st.set_page_config(page_title="AI Budget Planner", page_icon="💰")
st.title("💰 Smart AI Budget Planner")
st.write("Enter your financial details below to get a breakdown and percentage analysis.")

# 1. Create the Visual Input Fields for the User
income = st.number_input("Monthly Income ($)", min_value=0, value=4000, step=100)

st.subheader("Monthly Expenses")
rent = st.number_input("Rent / Mortgage ($)", min_value=0, value=1500, step=50)
groceries = st.number_input("Groceries ($)", min_value=0, value=450, step=25)
auto = st.number_input("Car & Insurance ($)", min_value=0, value=500, step=25)
utilities = st.number_input("Utilities & Internet ($)", min_value=0, value=250, step=25)
fun = st.number_input("Dining Out & Fun ($)", min_value=0, value=600, step=50)

# 2. When the user clicks the action button, run the AI model
if st.button("Generate My Financial Breakdown"):
    with st.spinner("Analyzing your budget percentages..."):
        # Safe initialization of the Gemini client
        client = genai.Client()
        
        # Structure the inputs into a dynamic instruction prompt
        prompt = f"""
        You are a professional financial planner. Analyze this user's monthly budget input:
        - Monthly Income: ${income}
        - Rent: ${rent}
        - Groceries: ${groceries}
        - Car & Insurance: ${auto}
        - Utilities & Internet: ${utilities}
        - Dining out & Fun: ${fun}

        Provide a clean, beautifully structured response with:
        1. A clear breakdown of what mathematical percentage of their total income goes to each specific item.
        2. An assessment of their spending allocations using the standard 50/30/20 rule.
        3. A recommended realistic budget adjustment to help them optimize their monthly savings.
        Keep the tone encouraging, structured, and use clear markdown bullet points.
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        
        # Display the AI response beautifully on the website screen!
        st.success("Analysis Complete!")
        st.markdown(response.text)

                                   
                                        
