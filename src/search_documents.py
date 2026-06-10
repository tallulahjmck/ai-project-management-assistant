from document_loader import load_document

def chunk_document(document):
    return document.split("\n\n")

def search_documents(keyword):
    documents = {
        "project_brief.txt": load_document("project_brief.txt"),
        "risk_register.txt": load_document("risk_register.txt")
    }

    results = []

    for filename, document in documents.items():
        chunks = chunk_document(document)

        for chunk in chunks:
            if keyword.lower() in chunk.lower():
                results.append((filename, chunk))

    return results


search_term = "risk"

results = search_documents(search_term)

print(f"Results for '{search_term}':")

for filename, chunk in results:
    print(f"\n--- {filename} ---")
    print(chunk)