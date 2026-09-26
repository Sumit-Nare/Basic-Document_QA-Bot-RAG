from src.rag import retrieve
print("BASIC DOCUMENT Q&A BOT")
print("Type exit to stop.")
while True:
    q=input("\nQuestion: ").strip()
    if q.lower() in ("exit","quit"): break
    try:
        results=retrieve(q)
        if not results or results[0][1]<0.30:
            print("\nAnswer: I couldn't find this information in the provided documents.")
        else:
            print("\nAnswer:\n"+results[0][0]["text"])
        print("\nSources:")
        for r,s in results: print(f"- {r['source']}, Page {r['page']} (similarity {s:.3f})")
    except Exception as e: print("Error:",e)
