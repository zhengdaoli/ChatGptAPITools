import openai
import re

# Set up OpenAI API credentials
openai.api_key = "INSERT_YOUR_API_KEY_HERE"


# Define function to summarize an article based on a prompt
def summarize_article(article, prompt=""):
    # Set up the prompt and article for the GPT-3 API request
    text = prompt + '\n\n' + article
    # Use OpenAI's GPT-3 API to generate a summary
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=text,
      temperature=0.5,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    # Extract the summary from the API response
    summary = response.choices[0].text
    # Clean up the summary by removing any leading/trailing whitespace and extra line breaks
    summary = summary.strip()
    summary = re.sub(r'[\r\n]+', ' ', summary)
    return summary


