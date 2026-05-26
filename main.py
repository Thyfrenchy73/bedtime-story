import requests
import os
from datetime import datetime

DEEPSEEK_KEY = os.environ.get("DEEPSEEK_API_KEY")
ELEVENLABS_KEY = os.environ.get("ELEVENLABS_API_KEY")

def generate_story(day):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-v4-flash",
        "messages": [
            {"role": "system", "content": "You are a children's author. Write soothing bedtime stories. No markdown, no emojis."},
            {"role": "user", "content": f"Write a bedtime story for Leo, age 5. Chapter {day} of 5. Space adventure. 200-300 words."}
        ],
        "temperature": 0.8,
        "max_tokens": 500
    }
    response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

def main():
    day = datetime.now().day % 5 + 1
    story = generate_story(day)
    print(f"Day {day}: {story}")

if __name__ == "__main__":
    main()
