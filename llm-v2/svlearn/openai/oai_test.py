import openai

# API key does not need to be valid
openai.base_url = "http://localhost:8080"
openai.api_key = 'sk-XXXXXXXXXXXXXXXXXXXX'

completion = openai.chat.completions.create(
    model="llama2-13-2q-chat.gguf",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)