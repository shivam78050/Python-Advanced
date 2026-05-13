from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path="/Users/shivam/Python-Advanced/RAG/Books", 
    glob="**/*.pdf", 
    show_progress=True, 
    loader_cls=PyPDFLoader
)

documents = loader.load()
print(len(documents))
print(documents[90])
print("============================")
docs = loader.lazy_load()

for document in docs:
    print(document.page_content)