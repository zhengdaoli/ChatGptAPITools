import openai
import re
import default_prompts
# Set up OpenAI API credentials


# Define function to summarize an article based on a prompt

def ask(query):
    # Use OpenAI's GPT-3 API to generate a summary
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=query,
      temperature=0.5,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    res = response.choices[0].text
    res = res.strip()
    res = re.sub(r'[\r\n]+', ' ', res)
    return res


def summarize_article(input_content, prompt=default_prompts.Commentariat):
    text = prompt + '\n\n' +'please summary and give opinion on this article:' + input_content
    return ask(text)


def translate2english(input_content, prompt=default_prompts.Improver):
    text = prompt + '\n\n' +'please translate to English:' + input_content
    return ask(text)


def polish_manuscript(input_content, prompt=default_prompts.Researcher):
    text = prompt + '\n\n' +'please polish my manuscript:' + input_content
    return ask(text)

def movie_critic(input_content, prompt=default_prompts.Researcher):
    text = prompt + '\n\n' +'write a movie review for the movie' + input_content
    return ask(text)