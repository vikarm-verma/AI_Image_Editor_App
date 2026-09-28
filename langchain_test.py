# Import os to read environment variables.
import os

# Import load_dotenv to load the API key from the .env file.
from dotenv import load_dotenv

# Import the LangChain integration for Google Gemini.
from langchain_google_genai import ChatGoogleGenerativeAI


# Load variables from the .env file.
load_dotenv()


# Read the Gemini API key from the environment.
api_key = os.getenv("GEMINI_API_KEY")


# Create a Gemini chat model through LangChain.
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)


# Send a simple test message through LangChain.
response = llm.invoke(
    "Explain in one sentence what AI image editing means."
)


# Display Gemini's response.
print(response.content)