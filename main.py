#coding:utf-8

import openai
import ask

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"



# ask without any default prompt:

def example1():
    query = "How can ChatGPT help me with daily life and work?"
    print(ask.ask(query))

# examples: you can just paste the string here as the input of the target function instead of using terminal.

def example2():
    article = input("Enter the news article you'd like to summarize and give some opinion: ")
    print(ask.summarize_article(article))

def example3():
    article = input("输入你想翻译的内容: ")
    print(ask.translate2english(article))

def example4():
    movie = input("Enter the movie name you want to give some reviews:")
    print(ask.movie_critic(movie))

def example5():
    qu = input("Enter your questions:")
    print(ask.response_scientific_question(qu))


example1()
example2()
example3()
example4()
example5()