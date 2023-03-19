import openai
import re
import default_prompts
# Set up OpenAI API credentials



# Define function to summarize an article based on a prompt

def summarize_article(article, prompt=default_prompts.Commentariat):    # Set up the prompt and article for the GPT-3 API request
    text = prompt + '\n\n' +'please summary and give opinion on this article:' + article
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


