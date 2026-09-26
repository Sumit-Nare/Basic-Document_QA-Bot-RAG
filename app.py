import streamlit as st
from src.rag import retrieve
st.title("Basic Document Q&A Bot")
q=st.text_input("Ask a question about the documents")
if st.button("Ask") and q:
    try:
        results=retrieve(q)
        if not results or results[0][1]<0.30: st.warning("I couldn't find this information in the provided documents.")
        else: st.write(results[0][0]["text"])
        st.subheader("Sources")
        for r,s in results: st.write(f"{r['source']} - Page {r['page']} | similarity {s:.3f}")
    except Exception as e: st.error(str(e))
