from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", top_k=100, temperature=1)
messages = [
    SystemMessage(content="Write a story about following word in Turkish."),
    HumanMessage(content="Sheeps")
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content)
