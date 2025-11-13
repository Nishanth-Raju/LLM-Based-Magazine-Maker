import os
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import pytesseract
from bs4 import BeautifulSoup
import requests

class DocumentParser:
    def __init__(self):
        # Initialize Tesseract for OCR if needed
        pass

    def parse_pdf(self, file_path):
        """Parse PDF and extract text."""
        text = ""
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    def parse_word(self, file_path):
        """Parse Word document and extract text."""
        doc = Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

    def parse_image(self, file_path):
        """Parse image and extract text using OCR."""
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text

    def parse_html(self, file_path):
        """Parse HTML and extract text."""
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            text = soup.get_text()
        return text

    def parse_text(self, file_path):
        """Parse plain text file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    def parse_file(self, file_path):
        """Parse file based on extension."""
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            return self.parse_pdf(file_path)
        elif ext in ['.docx', '.doc']:
            return self.parse_word(file_path)
        elif ext in ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']:
            return self.parse_image(file_path)
        elif ext == '.html':
            return self.parse_html(file_path)
        elif ext == '.txt':
            return self.parse_text(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

# Example usage
if __name__ == "__main__":
    parser = DocumentParser()
    # Test with a sample file
    print("Document parser ready.")
