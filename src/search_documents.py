from pathlib import Path
from document_loader import load_document

SAMPLE_DOCS = Path("sample_docs")


def chunk_document(document):
    return document.split("\n\n")


def search_documents(keyword):

    documents = {}

    # Automatically load all .txt files
    for file in SAMPLE_DOCS.glob("*.txt"):
        documents[file.name] = load_document(file.name)

    results = []

    # Search through all documents and chunks
    for filename, document in documents.items():
        chunks = chunk_document(document)

        for chunk in chunks:

            # Count how many times the keyword appears
            match_count = chunk.lower().count(keyword.lower())

            if match_count > 0:
                results.append((filename, chunk, match_count))

    return results


# Ask user what they want to search for
search_term = input("What would you like to search for? ")

results = search_documents(search_term)

# Sort by relevance (highest match count first)
results.sort(key=lambda result: result[2], reverse=True)

print(f"\nResults for '{search_term}':")

if not results:
    print("No matching results found.")

else:
    for filename, chunk, match_count in results:
        print(f"\n--- {filename} | Matches: {match_count} ---")
        print(chunk)