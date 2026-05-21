from google import genai
client = genai.Client(api_key="AIzaSyBbwMzBS2pZWXZIzg-v3ZUURKD5Xqq0fOQ")

user_input = input("How are you feeling today? ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=f"Give a short motivational response for: {user_input}"
)

print(response.text)