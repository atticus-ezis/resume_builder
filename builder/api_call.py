import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('API_KEY')

key_exists = api_key is not None
print(f"API key exists: {key_exists}")

client = OpenAI(api_key=api_key)

def api_call(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    result = api_call("Hello, how are you?")
    print(result)