import openai
import sys

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Get user input for the news article to summarize
article = input("Enter the news article you'd like to summarize: ")

# Set up OpenAI GPT-3 model and parameters
model_engine = "text-davinci-002"
max_tokens = 60
temperature = 0.5

# Use OpenAI API to generate summary
response = openai.Completion.create(
    engine=model_engine,
    prompt=f"Please summarize the following news article:\n{article}\nSummary:",
    max_tokens=max_tokens,
    temperature=temperature
)

# Print summary
summary = response.choices[0].text.strip()
print(f"Summary: {summary}")