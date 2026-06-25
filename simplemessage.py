from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import  StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", top_k=100, temperature=1)
messages = [
    SystemMessage(content="Translate following word in Turkish."),
    HumanMessage(content="Sheeps")
]


parser = StrOutputParser()

chain = model | parser
if __name__ == "__main__":
#response = model.invoke(messages)
    print(chain.invoke(messages))
