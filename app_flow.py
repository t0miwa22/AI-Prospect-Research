import getpass
import os
from langchain import hub
import requests
from bs4 import BeautifulSoup
from langchain import hub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI



#os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")


#function to scrape the company website
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    content = ' '.join([para.get_text() for para in paragraphs])
    return content


# Define the prompt template for summarization
prompt_template = PromptTemplate(
    input_variables=["company_info"],
    template=(
        "Based on the following information about a prospective company, create an article "
        "tailored for the sales team. The article should clearly outline the company's core business activities, "
        "that could impact our sales strategy. Additionally, suggest specific ways these insights can be leveraged "
        "to enhance our sales approach.\n\n"
        "Only include the article content, and do not provide a final answer afterward.\n\n"
        "Company Information:\n{company_info}\n\n"
        "Generate the article below:\n"
    )
)

# Initialize OpenAI LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Create an LLM chain for summarization
summarization_chain = LLMChain(llm=llm, prompt=prompt_template)

# Define the gather and summarize function
def generate_report(url):
    raw_content = scrape_website(url)  # Scrape website content
    article = summarization_chain.run(company_info=raw_content)
    return article

#define the tools
tools = [
    Tool(
        name="Scraper",
        func=scrape_website,
        description="Scrapes a given company's website to extract data."
    ),
    Tool(
        name="Report Generator",
        func=generate_report,
        description="Summarizes the extracted company data and generates a report."
    )
]
prompt = hub.pull("hwchase17/react")
# Create the ReAct agent using the create_react_agent function
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
    stop_sequence=True,
)

# Create an agent executor from the agent and tools
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
)
#print(generate_report("https://www.orderly.io/about"))

import streamlit as st

# Import the function that generates the article (from your previous code)
#from your_module import generate_article  # Replace 'your_module' with the actual file/module name

st.title("Sales Prospect Article Generator")

# Input field for the URL
company_url = st.text_input("Enter the Company URL", "")

if company_url:
    # Generate the article
    article_text = generate_report(company_url)

    # Display the article
    st.subheader("Sales Prospect Article")
    st.write(article_text)
