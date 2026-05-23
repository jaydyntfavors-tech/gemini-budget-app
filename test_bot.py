import os
from google import genai
client = genai.Client()
response = client.models.generate_content(model = 'gemini-1.5-flash',contents='Give me a 1 sentence tip on how to save money on groceries)
print(response.text)                                         
                                        
