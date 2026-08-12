from google import genai

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