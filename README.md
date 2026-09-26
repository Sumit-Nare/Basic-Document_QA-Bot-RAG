# Basic Document Q&A Bot using RAG
A document question-answering project using PDF extraction, overlapping chunks, batched Sentence Transformer embeddings, FAISS retrieval, and source/page citations.

## Setup
py -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt

## Build index
py src\\ingest.py

## Run CLI
py main.py

## Run Streamlit
streamlit run app.py

## Architecture
Documents -> Extraction -> Chunking -> Embeddings -> FAISS -> Retrieval -> Grounded answer -> Sources

## Chunking
800-character chunks with 150-character overlap.

## Embeddings
all-MiniLM-L6-v2, generated in batches.

## Vector store
FAISS index persisted as index.faiss with metadata.pkl.
