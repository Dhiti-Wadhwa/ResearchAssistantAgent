from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.document_loaders import PyPDFLoader
import matplotlib.pyplot as plt
import os 
from dotenv import load_dotenv

llm = ChatOpenAI(model = "openai/gpt-3.5-turbo", 
                 api_key="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" , 
                 base_url = "https://openrouter.ai/api/v1",
                 temperature=0)

search_tool = DuckDuckGoSearchRun()

@tool
def web_search(query:str) -> str:
    """Search net for latest information"""
    return search_tool.run(query)

@tool
def read_pdf(query:str) -> str:
    """Reads and summarizes content"""
    try: 
        loader = PyPDFLoader("AI - LAB CA Instructions - SEM VI - 2026.pdf")
        pages = loader.load()
        text = ""
        for p in pages:
            text += p.page_content
        return text[:3000] 
    except Exception as e:
        return f"Error reading PDF: {str(e)}"
    
@tool
def calculator(query:str) -> str:
    """Performs basic math calculations"""
    try:
        return str(eval(query))
    except:
        return "Error in calculation"
    
    
tools = [web_search,read_pdf,calculator]

agent = create_agent(llm, tools=tools, system_prompt="You are a helpful assistant. Use the available tools to answer questions accurately.")

while True:
    query = input("/nAsk something (or type exit)")
    
    if query.lower() == "exit":
        break
    
    response = agent.invoke({"messages":[{"role":"user", "content" :query}]})
    
    for message in reversed(response["messages"]):
        if hasattr(message,'type') and message.type == "ai":
            print("\n FINAL ANSWER: \n", message.content)
            break