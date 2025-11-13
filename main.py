import os
import argparse
from parser import DocumentParser
from llm import LLMHandler
from generator import MagazineGenerator

def analyze_content_type(text):
    """Analyze the type of content in the input text."""
    text_lower = text.lower()

    content_types = {
        'sports': ['sports', 'tournament', 'championship', 'medal', 'athlete', 'competition'],
        'academic': ['academic', 'achievement', 'scholarship', 'cgpa', 'research', 'publication'],
        'cultural': ['cultural', 'festival', 'music', 'dance', 'drama', 'art', 'performance'],
        'infrastructure': ['infrastructure', 'facility', 'laboratory', 'building', 'construction'],
        'events': ['event', 'conference', 'seminar', 'workshop', 'celebration']
    }

    detected_types = []
    for content_type, keywords in content_types.items():
        if any(keyword in text_lower for keyword in keywords):
            detected_types.append(content_type)

    return detected_types if detected_types else ['general']

def create_dynamic_prompt(content, content_types, file_names):
    """Create a dynamic prompt based on content analysis."""
    base_prompt = f"""Please analyze the following content from files: {', '.join(file_names)}

CONTENT TO ANALYZE:
{content}

DETECTED CONTENT TYPES: {', '.join(content_types)}

CRITICAL INSTRUCTIONS:
1. Create an appropriate magazine title based on the content
2. Extract and organize ONLY the information provided in the input - do not add external information
3. Structure the content into logical sections based on the detected content types
4. Use bullet points for lists and achievements
5. Keep the language engaging and professional
6. Fix any typos in the original content (e.g., 'Winers' → 'Winners', 'gamings' → 'gaming')
7. Maintain accuracy - if something isn't mentioned, don't add it
8. Focus on the actual events, achievements, and details from the provided content

REQUIRED SECTIONS:"""

    # Add specific sections based on content type
    if 'sports' in content_types:
        base_prompt += """
- Event Overview (date, location, participants, theme)
- Competition Results (actual results from the content)
- Achievements & Winners (medals, championships, records)
- Event Highlights (key moments, special features)
- Participant Feedback (testimonials from students/faculty)
- Future Plans (mentioned future developments)"""

    if 'academic' in content_types:
        base_prompt += """
- Academic Excellence (top performers, CGPA, awards)
- Student Achievements (projects, research, publications)
- Department Highlights (placement rates, patents, facilities)
- Scholarships & Awards (financial support, merit scholarships)
- Faculty Achievements (research papers, awards)
- Upcoming Events (mentioned future activities)"""

    if 'cultural' in content_types:
        base_prompt += """
- Event Overview
- Competition Results
- Performances & Highlights
- Organizing Team
- Participant Feedback
- Future Events"""

    if 'infrastructure' in content_types:
        base_prompt += """
- New Facilities
- Infrastructure Updates
- Technology Enhancements
- Future Developments
- Impact on Students"""

    base_prompt += """

FORMATTING RULES:
- Use proper capitalization and punctuation
- Correct spelling errors from the original content
- Organize information chronologically or by importance
- Use clear section headers
- Keep the content concise but comprehensive
- End with a positive conclusion based on the actual content

OUTPUT FORMAT: Create a well-structured magazine article that accurately reflects ONLY the provided content. Use this exact format:

TITLE: [Magazine Title]

[SECTION HEADER 1]
[Content for section 1]

[SECTION HEADER 2]
[Content for section 2]

[CONCLUSION]
[Final thoughts]"""

    return base_prompt

    return base_prompt

def main():
    print("Starting magazine maker...")
    parser = argparse.ArgumentParser(description="LLM-Based Magazine Maker")
    parser.add_argument('files', nargs='+', help='Input files (PDF, Word, images)')
    parser.add_argument('--output', default='magazine.pdf', help='Output file name')
    parser.add_argument('--api-key', help='OpenRouter API key')
    parser.add_argument('--theme', default='professional',
                       choices=['professional', 'modern', 'academic', 'sports'],
                       help='Magazine theme (professional, modern, academic, sports)')
    args = parser.parse_args()
    print(f"Arguments parsed: files={args.files}, output={args.output}, theme={args.theme}")

    doc_parser = DocumentParser()
    llm = LLMHandler(args.api_key)
    gen = MagazineGenerator(theme=args.theme)
    all_text = ""

    print("Parsing files...")
    for file_path in args.files:
        if os.path.exists(file_path):
            try:
                text = doc_parser.parse_file(file_path)
                all_text += f"\n--- Content from {os.path.basename(file_path)} ---\n{text}\n"
                print(f"Parsed: {file_path} ({len(text)} chars)")
            except Exception as e:
                print(f"Error parsing {file_path}: {e}")
        else:
            print(f"File not found: {file_path}")

    print(f"Total text length: {len(all_text)}")

    # Analyze content types
    content_types = analyze_content_type(all_text)
    file_names = [os.path.basename(fp) for fp in args.files]

    print(f"Detected content types: {', '.join(content_types)}")

    # Create dynamic prompt based on content analysis
    prompt = create_dynamic_prompt(all_text, content_types, file_names)
    print("Generated prompt, calling LLM...")
    organized_content = llm.generate(prompt)

    print("LLM response received, generating output...")
    print("\nOrganized Content:")
    print(organized_content)

    # Generate output
    if args.output.endswith('.pdf'):
        gen.generate_pdf_reportlab(organized_content, args.output)
    elif args.output.endswith('.html'):
        gen.generate_html(organized_content, args.output)
    else:
        print("Unsupported output format. Use .pdf or .html")

    print(f"Magazine generated as: {args.output}")

if __name__ == "__main__":
    main()
