from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Prompt
prompt = PromptTemplate(
    template="Write a summary for the following text:\n{poem}",
    input_variables=["poem"]
)

# Parser
parser = StrOutputParser()

# Loader
loader = TextLoader(
    "/Users/shivam/Python-Advanced/RAG/cricket.txt",
    encoding="utf-8"
)

documents = loader.load()

# Chain
chain = prompt | model | parser

# Invoke
response = chain.invoke({
    "poem": documents[0].page_content
})

print(response)