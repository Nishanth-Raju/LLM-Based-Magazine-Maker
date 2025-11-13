# LLM-Based Magazine Maker

## Overview
A free, open-source tool that uses Large Language Models (LLMs) to automatically generate magazines or newsletters for organizations. Users provide event and achievement details (PDF, Word, images), and the tool creates a professional magazine or newsletter.

## Features
- Accepts PDF, Word, and image inputs
- Extracts text and images from documents
- Uses LLMs to summarize, organize, and beautify content
- Generates professional magazine/newsletter in PDF or HTML format
- Magazine-style layout with sections, headers, and styling
- 100% free and open-source (no paid APIs or assets)

## Tech Stack
- Python (core logic)
- Free LLMs (OpenRouter free API or Ollama TinyLlama locally)
- Free document parsing libraries (PyPDF2, python-docx, Pillow)
- Free PDF generation (ReportLab, WeasyPrint)

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. For Ollama fallback: Install Ollama and pull TinyLlama model
3. Run: `python main.py file1.pdf file2.docx image.jpg --output magazine.pdf --api-key YOUR_OPENROUTER_KEY`

## Usage
- Input files: PDF, Word (.docx), images (PNG, JPG, etc.)
- Output: PDF or HTML
- API Key: Optional for OpenRouter, falls back to Ollama

## License
MIT (or other free license)

## Credits
This project is for educational/non-commercial use. All libraries and assets used must be free.

---

