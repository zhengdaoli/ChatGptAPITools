import openai
import ask

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"



# ask without any default prompt:
query = "How can ChatGPT help me with daily life and work?"
print(ask.ask(query))

# examples: you can just paste the string here as the input of the target function instead of using terminal.

article = input("Enter the news article you'd like to summarize and give some opinion: ")
print(ask.summarize_article(article))

movie = input("Enter the movie name you want to give some reviews:")
print(ask.movie_critic(movie))


