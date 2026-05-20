import os
import gradio as gr

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)

from langchain.chains.question_answering import load_qa_chain


# =========================================================
# Load Environment Variables
# =========================================================

load_dotenv()

GOOGLE_API_KEY = "AIzaSyDeCq7MLz464F4jz6ajGZO490VEYML_hww"

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")


# =========================================================
# Global Vector Store
# =========================================================

vectorstore = None


# =========================================================
# Process PDF
# =========================================================

def process_pdf(pdf):

    global vectorstore

    try:

        if pdf is None:
            return "Please upload a PDF file."

        # Load PDF
        loader = PyPDFLoader(pdf.name)

        documents = loader.load()

        if not documents:
            return "No text found inside PDF."

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

        # Gemini Embeddings
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=GOOGLE_API_KEY
        )

        # Create FAISS vector DB
        vectorstore = FAISS.from_documents(
            chunks,
            embeddings
        )

        return f"PDF processed successfully! Total chunks created: {len(chunks)}"

    except Exception as e:
        return f"Error while processing PDF:\n{str(e)}"


# =========================================================
# Ask Question
# =========================================================

def ask_question(question):

    global vectorstore

    try:

        if vectorstore is None:
            return "Please upload and process a PDF first."

        if not question.strip():
            return "Please enter a question."

        # Retrieve relevant chunks
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

        docs = retriever.get_relevant_documents(question)

        # Gemini LLM
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=GOOGLE_API_KEY,
            temperature=0.3
        )

        # QA Chain
        chain = load_qa_chain(
            llm,
            chain_type="stuff"
        )

        response = chain.run(
            input_documents=docs,
            question=question
        )

        return response

    except Exception as e:
        return f"Error while answering question:\n{str(e)}"


# =========================================================
# Gradio UI
# =========================================================

with gr.Blocks() as demo:

    gr.Markdown(
        """
        # PDF Question Answering System
        
        Upload any PDF and ask questions about the document.
        """
    )

    with gr.Row():

        pdf_input = gr.File(
            label="Upload PDF",
            file_types=[".pdf"]
        )

    process_button = gr.Button("Process PDF")

    process_output = gr.Textbox(
        label="Processing Status"
    )

    process_button.click(
        fn=process_pdf,
        inputs=pdf_input,
        outputs=process_output
    )

    gr.Markdown("## Ask Questions")

    question_input = gr.Textbox(
        label="Enter Question",
        placeholder="Example: What was the total revenue in 2024?"
    )

    ask_button = gr.Button("Get Answer")

    answer_output = gr.Textbox(
        label="Answer",
        lines=10
    )

    ask_button.click(
        fn=ask_question,
        inputs=question_input,
        outputs=answer_output
    )


# =========================================================
# Launch App
# =========================================================

demo.launch(
    share=True,
    debug=True,
    inbrowser=True
)