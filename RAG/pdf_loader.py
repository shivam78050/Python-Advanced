from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("/Users/shivam/Python-Advanced/RAG/dl-curriculum.pdf")
documents = loader.load()
print(documents)
print(f"Total number of pages: {len(documents)}")
print(f"Content of the first page: {documents[0].page_content}")
print(f"Metadata of the first page: {documents[0].metadata}")

