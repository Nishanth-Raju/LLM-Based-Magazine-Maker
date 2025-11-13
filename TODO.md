# TODO

## Core Tasks
- [x] Research and select free/open-source LLMs
    - Primary: OpenRouter free API model
    - Fallback: Ollama TinyLlama locally
- [x] Set up document parsing for PDF, Word, and images
    - Libraries: PyPDF2, python-docx, Pillow, pytesseract
    - Created parser.py with DocumentParser class
- [x] Build input pipeline for uploading files
    - Created main.py with CLI for file input
- [x] Extract and organize event/achievement details
    - Integrated LLM in main.py for summarization and organization
- [x] Summarize and beautify content using LLM
    - Handled in LLM integration
- [x] Design magazine/newsletter layout (PDF/web)
    - Enhanced with professional styling, sections, headers
    - Added magazine-like formatting with ReportLab and HTML/CSS
- [x] Generate final output (PDF/web)
    - Integrated in main.py
- [x] Add support for images in output
    - Basic support in generator.py (can be enhanced)
- [x] Ensure all dependencies/assets are free
    - All libraries in requirements.txt are free/open-source

## Optional/Advanced
- [ ] Add web interface (Flask/Django/Streamlit)
- [ ] Add templates/themes for magazine
- [ ] Multi-language support
- [ ] Export to other formats (HTML, EPUB)
- [ ] Automated testing

## Documentation
- [x] Write user guide
    - Updated README.md with usage instructions
- [ ] Add example inputs/outputs
- [ ] Document codebase

---

(DA sir son project)
