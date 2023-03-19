import openai
from news_summary import news

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"



article = input("Enter the news article you'd like to summarize and give some opinion: ")
print(news.summarize_article(article))