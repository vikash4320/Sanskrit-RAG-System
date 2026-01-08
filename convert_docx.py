from docx import Document

def convert_docx_to_txt(input_path, output_path):
    doc = Document(input_path)
    with open(output_path, "w", encoding="utf-8") as f:
        for para in doc.paragraphs:
            text = para.text.strip()
            if text:
                f.write(text + "\n")

if __name__ == "__main__":
    convert_docx_to_txt(
        "data/Rag-docs.docx",
        "data/sample_sanskrit.txt"
    )
