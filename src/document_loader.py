from pathlib import Path

file_path = Path("../sample_docs/project_brief.txt")

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
