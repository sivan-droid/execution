import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)


def summarize_node(state):

    text = state["input_text"]

    prompt = f"""
    Summarize the following text clearly and concisely:

    {text}
    """

    response = llm.invoke(prompt)

    return {
        "summary": response.content
    }