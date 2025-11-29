import os
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai import types


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"



def main():
    print("Hello from aiagent!")
    if len(sys.argv) < 2:
        print("Please provide a model name as a command line argument.")
        sys.exit(1)
    user_prompt = sys.argv[1]
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model=model,
        contents=messages,
        #"Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        )
    print(response.text)
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
