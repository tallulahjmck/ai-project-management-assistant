from pathlib import Path
from document_loader import load_document

SAMPLE_DOCS = Path("sample_docs")

def chunk_document(document):
    return document.split("\n\n")

def search_documents(keyword):

    documents = {}

    for file in SAMPLE_DOCS.glob("*.txt"):
        documents[file.name] = load_document(file.name)

    results = []

    for filename, document in documents.items():
        chunks = chunk_document(document)

        for chunk in chunks:
            if keyword.lower() in chunk.lower():
                results.append((filename, chunk))

    return results


search_term = input("What would you like to search for? ")

results = search_documents(search_term)

print(f"Results for '{search_term}':")

for filename, chunk in results:
    print(f"\n--- {filename} ---")
    print(chunk)