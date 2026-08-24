from google import genai
from dotenv import load_dotenv
#import os
#Imports Python's standard os module, used here to read environment variables
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def analyze_resume(resume_text):

    prompt = f"""
    Analyze the following resume and provide:

    1. Candidate Name
    2. Profession
    3. Key Skills
    4. Experience Level
    5. Strengths
    6. Areas for Improvement
    7. Suitable Job Roles
    8. Resume Score out of 100

    Resume:
    {resume_text}
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text
