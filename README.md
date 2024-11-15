Overview

This project is a Streamlit web application designed to generate tailored sales prospect articles. It scrapes a company's website, extracts relevant information, and uses OpenAI's GPT-4o-mini model to create insightful articles. These articles help the sales team better understand the company's business activities and align sales strategies accordingly.
Features

    Website Scraping:
        Uses BeautifulSoup to extract text content (<p> tags) from a given company URL.

    Summarization with OpenAI:
        Utilizes LangChain’s LLMChain with a predefined prompt to generate detailed articles based on the scraped website content.

    Streamlit UI:
        Provides a simple and interactive interface to input a company URL and view the generated sales article.

    Agent-Oriented Design:
        Implements LangChain's tools and ReAct agent framework for modularity and extensibility.

Prerequisites

    Python 3.8 or later

    Streamlit and required libraries:
        Install dependencies with:

    pip install -r requirements.txt

    Ensure libraries such as streamlit, beautifulsoup4, requests, and langchain are included.

OpenAI API Key:

    Add your API key in the st.secrets configuration or as an environment variable:

        os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

File Structure

    Main Application:
        generate_report: Combines web scraping and AI-based summarization to generate a custom sales article.
        scrape_website: Extracts content from a provided URL.
        Streamlit UI: Collects user input and displays the result.

    LangChain Components:
        PromptTemplate: Defines the article's structure and tone.
        LLMChain: Executes the summarization logic with GPT-4o-mini.
        Tools:
            Scraper: Extracts website data.
            Report Generator: Generates sales articles.

How to Run

    Clone Repository:

git clone https://github.com/your-repo-url.git
cd your-repo

Run Streamlit Application:

    streamlit run app.py

    Input Company URL:
        Enter the URL of a company website in the input field.
        View the generated sales prospect article under the "Sales Prospect Article" section.

Future Enhancements

    Add more robust error handling for scraping and API failures.
    Expand article generation with industry-specific insights.
    Enable multi-page scraping for detailed analysis.
    Enhance prompt flexibility for other use cases like product reviews or competitor analysis.

