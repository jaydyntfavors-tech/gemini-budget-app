import os
from google import genai

client = genai.Client()

# 1. Open and read the user's input file from the cloud folder
with open("user_data.txt", "r") as file:
    user_budget_data = file.read()

# 2. Build the instruction dynamically based on the file contents
prompt = f"""
You are a professional financial planner. Analyze this user's monthly budget input:

{user_budget_data}

Provide a personalized response with:
1. A clear breakdown of what percentage of income goes to each expense item listed.
2. An assessment of their spending using the standard 50/30/20 rule.
3. A recommended realistic budget adjustment to optimize their monthly savings.
Keep the tone encouraging, structured, and easy to read.
"""

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt)

print(response.text)
                                   
                                        
