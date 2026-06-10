from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_document(filename):
    file_path = BASE_DIR / "sample_docs" / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()