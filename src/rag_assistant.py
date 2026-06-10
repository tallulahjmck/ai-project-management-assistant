from document_loader import load_document

project_brief = load_document("project_brief.txt")
risk_register = load_document("risk_register.txt")

print("=== PROJECT BRIEF ===")
print(project_brief)

print("\n=== RISK REGISTER ===")
print(risk_register)
