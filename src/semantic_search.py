from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Project delay caused by resource constraints",
    "Stakeholder meeting scheduled for Friday",
    "Budget approval pending"
]

query = "resource issues"

document_embeddings = model.encode(documents)

query_embedding = model.encode([query])

scores = cosine_similarity(query_embedding, document_embeddings)[0]

for document, score in zip(documents, scores):
    print(f"{score:.3f} - {document}")