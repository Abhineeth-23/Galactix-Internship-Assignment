import requests
import json

API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = "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"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def call_ai(prompt):
    try:
        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        response = requests.post(API_URL, headers=headers, json=data)

        if response.status_code != 200:
            print("Error occurred while calling API")
            print("Status code:", response.status_code)
            print("Response:", response.text)
            return None

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None


prompt = input("Enter your prompt: ")

result = call_ai(prompt)

if result:
    ai_response = result["choices"][0]["message"]["content"]

    print("\nAI Response:\n")
    print(ai_response)

    with open("output.txt", "w") as file:
        file.write("Prompt:\n")
        file.write(prompt + "\n\n")
        file.write("AI Response:\n")
        file.write(ai_response)

    print("\nResponse saved to output.txt")

else:
    print("Failed to get response from AI")