import ollama

def embed(text):
    try:
        embedding = ollama.embeddings(
        model='nomic-embed-text',
        prompt=text
        )
        result = embedding['embedding']
    except Exception:
        print(f"Could not embed text: {text}")
        result = None
    return result