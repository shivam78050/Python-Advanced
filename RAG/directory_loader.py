from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path="/Users/shivam/Python-Advanced/RAG/Books", 
    glob="**/*.pdf", 
    show_progress=True, 
    loader_cls=PyPDFLoader
)

documents = loader.load()
print(len(documents))