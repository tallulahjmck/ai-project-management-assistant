from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_document(filename):
    file_path = BASE_DIR / "sample_docs" / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

project_brief = load_document("project_brief.txt")
risk_register = load_document("risk_register.txt")

print(project_brief)
print(risk_register)