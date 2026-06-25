from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)

#messages = [
#    SystemMessage(content="Translate following word in Turkish."),
#    HumanMessage(content="Sheep")
#]

system_prompt = "Translate following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt), ("user", "{text}")
    ]
)
parser = StrOutputParser()

chain = prompt_template | model | parser

if __name__ == "__main__":
    print(chain.invoke({"language":"italian", "text":"hello mom"}))
