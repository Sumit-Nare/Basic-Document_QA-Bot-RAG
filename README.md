# Basic Document Q&A Bot (RAG Pipeline)

**AI Internship Technical Assignment — Bookxpert Pvt. Ltd.**

**Developed by:** Sumit Nare  
**Language:** Python 3.11

## 1. Project Overview

Basic Document Q&A Bot is a document-based question-answering application built using Retrieval-Augmented Generation (RAG).

The system allows users to ask natural-language questions about uploaded documents. It extracts text from documents, divides the text into chunks, generates embeddings, stores them in a FAISS vector database, and retrieves relevant information to answer questions with source references.

## 2. Objectives

- Build a document question-answering system using RAG.
- Extract text from multiple PDF documents.
- Divide documents into manageable text chunks.
- Generate document embeddings using Sentence Transformers.
- Store and retrieve embeddings using FAISS.
- Answer user questions using relevant document content.
- Display source filenames, page numbers and similarity scores.
- Provide an interactive command-line interface.

## 3. Technology Stack

- Python 3.11
- Sentence Transformers
- Hugging Face Transformers
- FAISS
- PyPDF
- NumPy
- Streamlit (optional user interface)

## 4. System Architecture

Document Collection
        |
        v
Document Ingestion
        |
        v
PDF Text Extraction
        |
        v
Text Chunking
        |
        v
Batch Embedding Generation
        |
        v
FAISS Vector Database
        |
        v
User Question
        |
        v
Query Embedding
        |
        v
Similarity Search
        |
        v
Relevant Document Chunks
        |
        v
Answer Generation
        |
        v
Answer with Source References

## 5. Project Structure

    Basic_Document_QA_Bot/
    |
    |-- data/
    |   |-- PDF documents
    |
    |-- src/
    |   |-- ingest.py
    |
    |-- vector_store/
    |   |-- faiss/
    |       |-- index.faiss
    |
    |-- app.py
    |-- main.py
    |-- requirements.txt
    |-- README.md
    |-- .gitignore
    |-- run.bat

## 6. Document Ingestion

The ingestion process reads the documents stored in the data folder and extracts their text.

The extracted text is divided into chunks, converted into numerical embeddings and stored in the FAISS vector database.

## 7. Text Chunking

Text chunking divides large documents into smaller sections before embedding.

The purpose of chunking is to make document retrieval more efficient and help preserve relevant context.

Overlapping chunks can help prevent important information from being lost at chunk boundaries.

## 8. Embedding Model

Sentence Transformers is used to convert document chunks and user questions into numerical vector representations.

These embeddings enable semantic similarity search between user questions and document content.

## 9. Vector Database

FAISS is used to store document embeddings and retrieve relevant document chunks.

The vector database is saved locally so that the documents do not need to be processed again for every question.

## 10. Retrieval and Answer Generation

When a user submits a question:

1. The question is converted into an embedding.
2. FAISS searches for similar document embeddings.
3. The most relevant document chunks are retrieved.
4. Retrieved content is used to produce an answer.
5. Source references are displayed alongside the answer.

Source references include document filenames, page numbers and similarity scores.

## 11. Installation and Setup

### Prerequisites

- Python 3.11 or higher
- pip
- Internet connection for the initial model download

### Step 1: Clone the repository

    git clone https://github.com/Sumit-Nare/Basic-Document_QA-Bot-RAG.git

### Step 2: Open the project directory

    cd Basic-Document_QA-Bot-RAG

### Step 3: Install dependencies

    pip install -r requirements.txt

### Step 4: Prepare documents

Place the PDF documents inside the data folder.

### Step 5: Create the vector database

    python src/ingest.py

The ingestion script processes the documents and creates the FAISS vector store.

### Step 6: Run the application

    python main.py

The application starts an interactive question-answering session.

Type exit to stop the application.

## 12. Example Questions

1. What is data science?
2. What is artificial intelligence?
3. Explain the fundamentals of data science.
4. What are the applications of artificial intelligence?
5. What is exploratory data analysis?

## 13. Example Output

Question: What is data science?

Answer:

Data science is an interdisciplinary field that uses statistics, programming, machine learning and domain knowledge to extract useful information from data.

Sources:

- data_science.pdf, Page 1
- artificial_intelligence.pdf, Page 1

The actual answer and source references depend on the retrieved document content.

## 14. Key Features

- Multiple-document processing
- PDF text extraction
- Document chunking
- Batch embedding generation
- Persistent FAISS vector database
- Semantic similarity search
- Document-based question answering
- Source citation display
- Interactive command-line interface

## 15. Limitations

- Answer quality depends on the uploaded documents.
- Poorly formatted PDFs may affect text extraction.
- Scanned documents may require OCR.
- Retrieval may occasionally select irrelevant chunks.
- The system may not answer questions that are outside the available documents.
- Initial model downloads require an internet connection.

## 16. Future Enhancements

- Improved document retrieval
- Support for additional document formats
- Streamlit-based web interface
- Advanced language model integration
- Improved citation accuracy
- Document upload functionality

## 17. Project Demonstration

The project demonstrates document ingestion, embedding generation, FAISS vector storage, semantic retrieval and question answering with source references.

## 18. Developer

**Sumit Nare**

AI Internship Technical Assignment

Bookxpert Pvt. Ltd.
