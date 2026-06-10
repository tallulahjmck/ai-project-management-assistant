from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Project delay caused by resource constraints",
    "Stakeholder meeting scheduled for Friday",
    "Budget approval pending"
]

embeddings = model.encode(sentences)

print(f"Created {len(embeddings)} embeddings")
print(f"Embedding length: {len(embeddings[0])}")