from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

SAMPLE_DOCS = Path("sample_docs")


def load_documents():
    documents = []

    for file in SAMPLE_DOCS.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

            chunks = content.split("\n\n")

            for chunk in chunks:
                if chunk.strip():
                    documents.append({
                        "filename": file.name,
                        "content": chunk.strip()
                    })

    return documents


def semantic_search(query, documents, model, top_k=5):
    document_texts = [document["content"] for document in documents]

    document_embeddings = model.encode(document_texts)
    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, document_embeddings)[0]

    results = []

    for document, score in zip(documents, scores):
        results.append({
            "filename": document["filename"],
            "content": document["content"],
            "score": score
        })

    results = sorted(results, key=lambda result: result["score"], reverse=True)

    return results[:top_k]


model = SentenceTransformer("all-MiniLM-L6-v2")

documents = load_documents()

print(f"Loaded {len(documents)} document chunks.")

query = input("What would you like to ask? ")

results = semantic_search(query, documents, model)

print(f"\nTop semantic search results for: '{query}'")

for result in results:
    print(f"\n--- {result['filename']} | Similarity: {result['score']:.3f} ---")
    print(result["content"])