# 用于日常生活和工作的ChatGPT API

这个仓库是基于OpenAI训练的ChatGPT API构建的工具和应用程序的集合,已经经过调教，无需再进行调教，直接调用函数即可。我们旨在通过提供各种有用的工具和服务来改善和增强我们的日常生活和工作，以协助我们完成各种任务。

# 功能概述

新闻摘要：将新闻文章总结成简短、易于阅读的摘要，提供文章主要观点的快速概述。

翻译：构建一种翻译工具，可以在不同语言之间翻译文本，使我们更容易与说不同语言的人交流。

英语教学：创建语言学习工具，如语法和词汇测验、英语会话练习等。

手稿润色：帮助我们提高写作水平，提供建议，包括语法、风格和语气等。这对需要撰写清晰简明文件的专业人士尤其有用。

等等.

# 入门指南

要使用这个仓库中的工具和应用程序，您需要从OpenAI获取API密钥。您可以在OpenAI网站上注册API密钥。

获得API密钥后，您可以克隆这个仓库，按照每个工具的README文件中的说明开始使用。

# 例子：

比如要提炼一段新闻的内容，直接运行:
```
python news_summary/news.py
```
然后terminal会有如下提示：
```
Enter the news article you'd like to summarize:
``` 
最后把新闻内容复制粘贴内容到终端，回车即可。

另外一种方式是用您的其它程序调用`news.py`里面的函数:

```
import news_summary

news = 'ChatGPT4.0 is released today!'
news_summary.summary_news(news)

```


# 贡献

我们欢迎社区的贡献，以改进和扩展这个仓库中的工具和应用程序。如果您有新工具或功能的想法，请随时打开问题或提交拉取请求。


# ChatGPT API for Daily Life and Work
This repository is a collection of tools and applications built on top of the ChatGPT API, this repo contains awsome prompts, so you don't have to prompt again. With this repo, we aim to improve and enhance our daily life and work by providing useful tools and services that can assist us in various tasks.

# Summary of Features

News Summary: summarize news articles into short, easy-to-read summaries, providing a quick overview of the article's main points.

Translator: build a translator that can translate text between different languages, making it easier for us to communicate with people who speak different languages.

English Teaching: create language learning tools, such as grammar and vocabulary quizzes, conversational English practice, and more.

Manuscript Polish: improve our writing by providing suggestions for grammar, style, and tone. This can be particularly useful for professionals who need to write clear and concise documents.

# Getting Started

To use the tools and applications in this repository, you will need an API key from OpenAI. You can sign up for an API key on the OpenAI website.

Once you have your API key, you can clone this repository and follow the instructions in each tool's README file to get started.

# Contributions

We welcome contributions from the community to improve and expand the tools and applications in this repository. If you have an idea for a new tool or feature, feel free to open an issue or submit a pull request.

----
以上由ChatGPT自己生成。