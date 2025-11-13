from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from weasyprint import HTML, CSS

class MagazineGenerator:
    def __init__(self, theme='professional'):
        self.theme = theme
        self.styles = getSampleStyleSheet()
        self._setup_styles()

    def _setup_styles(self):
        """Setup custom styles for magazine layout based on theme."""
        if self.theme == 'professional':
            self._setup_professional_theme()
        elif self.theme == 'modern':
            self._setup_modern_theme()
        elif self.theme == 'academic':
            self._setup_academic_theme()
        elif self.theme == 'sports':
            self._setup_sports_theme()
        else:
            self._setup_professional_theme()  # Default

    def _setup_professional_theme(self):
        """Professional business-like theme with enhanced colors."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='MagazineTitle',
            parent=self.styles['Heading1'],
            fontSize=28,
            alignment=TA_CENTER,
            spaceAfter=30,
            textColor=colors.HexColor('#1e40af'),
            fontName='Helvetica-Bold'
        ))

        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=18,
            spaceAfter=15,
            textColor=colors.HexColor('#dc2626'),
            fontName='Helvetica-Bold',
            borderColor=colors.HexColor('#dc2626'),
            borderWidth=0,
            borderPadding=0
        ))

        # Event details style
        self.styles.add(ParagraphStyle(
            name='EventDetails',
            parent=self.styles['Normal'],
            fontSize=12,
            leftIndent=20,
            spaceAfter=6,
            textColor=colors.HexColor('#059669'),
            backColor=colors.HexColor('#ecfdf5'),
            alignment=TA_JUSTIFY
        ))

        # Achievement style
        self.styles.add(ParagraphStyle(
            name='Achievement',
            parent=self.styles['Normal'],
            fontSize=11,
            leftIndent=30,
            spaceAfter=4,
            bulletIndent=20,
            textColor=colors.HexColor('#7c3aed'),
            backColor=colors.HexColor('#f3e8ff'),
            alignment=TA_JUSTIFY
        ))

        # Normal text with tighter spacing and justification
        self.styles.add(ParagraphStyle(
            name='NormalTight',
            parent=self.styles['Normal'],
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            fontSize=11
        ))

    def _setup_modern_theme(self):
        """Modern, clean theme with vibrant colors."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='MagazineTitle',
            parent=self.styles['Heading1'],
            fontSize=30,
            alignment=TA_CENTER,
            spaceAfter=30,
            textColor=colors.HexColor('#7c3aed'),
            fontName='Helvetica-Bold'
        ))

        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=20,
            spaceAfter=15,
            textColor=colors.HexColor('#ec4899'),
            fontName='Helvetica-Bold'
        ))

        # Event details style
        self.styles.add(ParagraphStyle(
            name='EventDetails',
            parent=self.styles['Normal'],
            fontSize=11,
            leftIndent=20,
            spaceAfter=6,
            textColor=colors.HexColor('#059669'),
            backColor=colors.HexColor('#d1fae5'),
            alignment=TA_JUSTIFY
        ))

        # Achievement style
        self.styles.add(ParagraphStyle(
            name='Achievement',
            parent=self.styles['Normal'],
            fontSize=10,
            leftIndent=30,
            spaceAfter=4,
            bulletIndent=20,
            textColor=colors.HexColor('#dc2626'),
            backColor=colors.HexColor('#fee2e2'),
            alignment=TA_JUSTIFY
        ))

        # Normal text with tighter spacing and justification
        self.styles.add(ParagraphStyle(
            name='NormalTight',
            parent=self.styles['Normal'],
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            fontSize=11
        ))

    def _setup_academic_theme(self):
        """Academic theme with scholarly colors."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='MagazineTitle',
            parent=self.styles['Heading1'],
            fontSize=26,
            alignment=TA_CENTER,
            spaceAfter=30,
            textColor=colors.HexColor('#0f766e'),
            fontName='Helvetica-Bold'
        ))

        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=18,
            spaceAfter=15,
            textColor=colors.HexColor('#1e40af'),
            fontName='Helvetica-Bold'
        ))

        # Event details style
        self.styles.add(ParagraphStyle(
            name='EventDetails',
            parent=self.styles['Normal'],
            fontSize=11,
            leftIndent=20,
            spaceAfter=6,
            textColor=colors.HexColor('#7c2d12'),
            backColor=colors.HexColor('#fef3c7'),
            alignment=TA_JUSTIFY
        ))

        # Achievement style
        self.styles.add(ParagraphStyle(
            name='Achievement',
            parent=self.styles['Normal'],
            fontSize=10,
            leftIndent=30,
            spaceAfter=4,
            bulletIndent=20,
            textColor=colors.HexColor('#7c3aed'),
            backColor=colors.HexColor('#e9d5ff'),
            alignment=TA_JUSTIFY
        ))

        # Normal text with tighter spacing and justification
        self.styles.add(ParagraphStyle(
            name='NormalTight',
            parent=self.styles['Normal'],
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            fontSize=11
        ))

    def _setup_sports_theme(self):
        """Sports theme with energetic colors."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='MagazineTitle',
            parent=self.styles['Heading1'],
            fontSize=30,
            alignment=TA_CENTER,
            spaceAfter=30,
            textColor=colors.HexColor('#dc2626'),
            fontName='Helvetica-Bold'
        ))

        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=20,
            spaceAfter=15,
            textColor=colors.HexColor('#ea580c'),
            fontName='Helvetica-Bold'
        ))

        # Event details style
        self.styles.add(ParagraphStyle(
            name='EventDetails',
            parent=self.styles['Normal'],
            fontSize=11,
            leftIndent=20,
            spaceAfter=6,
            textColor=colors.HexColor('#0f766e'),
            backColor=colors.HexColor('#ecfdf5'),
            alignment=TA_JUSTIFY
        ))

        # Achievement style
        self.styles.add(ParagraphStyle(
            name='Achievement',
            parent=self.styles['Normal'],
            fontSize=10,
            leftIndent=30,
            spaceAfter=4,
            bulletIndent=20,
            textColor=colors.HexColor('#7c3aed'),
            backColor=colors.HexColor('#f3e8ff'),
            alignment=TA_JUSTIFY
        ))

        # Normal text with tighter spacing and justification
        self.styles.add(ParagraphStyle(
            name='NormalTight',
            parent=self.styles['Normal'],
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            fontSize=11
        ))

    def _add_cover_page(self, story, sections):
        """Add a colorful and attractive cover page."""
        # Add background color rectangle for cover
        from reportlab.lib.units import inch
        from reportlab.pdfgen import canvas

        # Cover title with enhanced styling
        if 'Title' in sections:
            story.append(Paragraph(sections['Title'][0], self.styles['MagazineTitle']))
        else:
            story.append(Paragraph("College Magazine", self.styles['MagazineTitle']))

        story.append(Spacer(1, 30))
        story.append(Paragraph("Events & Achievements", self.styles['Heading2']))
        story.append(Spacer(1, 50))

        # Add colorful decorative elements
        story.append(Paragraph("✦ ✦ ✦", ParagraphStyle('Decorative', fontSize=24, alignment=TA_CENTER, textColor=colors.HexColor('#f59e0b'))))
        story.append(Spacer(1, 30))

        # Publication info with better styling
        story.append(Paragraph("Published by: Your Organization", ParagraphStyle('PubInfo', fontSize=12, alignment=TA_CENTER, textColor=colors.HexColor('#6b7280'))))
        story.append(Paragraph(f"Generated on: {self._get_current_date()}", ParagraphStyle('PubInfo', fontSize=12, alignment=TA_CENTER, textColor=colors.HexColor('#6b7280'))))
        story.append(Spacer(1, 30))

        # Add theme-specific cover text with enhanced colors
        if self.theme == 'sports':
            story.append(Paragraph("🏆 Champions Celebrate 🏆", ParagraphStyle('CoverText', fontSize=18, alignment=TA_CENTER, textColor=colors.HexColor('#dc2626'), fontName='Helvetica-Bold')))
        elif self.theme == 'academic':
            story.append(Paragraph("📚 Excellence in Education 📚", ParagraphStyle('CoverText', fontSize=18, alignment=TA_CENTER, textColor=colors.HexColor('#059669'), fontName='Helvetica-Bold')))
        elif self.theme == 'modern':
            story.append(Paragraph("🚀 Innovation & Achievement 🚀", ParagraphStyle('CoverText', fontSize=18, alignment=TA_CENTER, textColor=colors.HexColor('#7c3aed'), fontName='Helvetica-Bold')))
        elif self.theme == 'professional':
            story.append(Paragraph("🌟 Professional Excellence 🌟", ParagraphStyle('CoverText', fontSize=18, alignment=TA_CENTER, textColor=colors.HexColor('#1e40af'), fontName='Helvetica-Bold')))

        # Add more decorative elements
        story.append(Spacer(1, 20))
        story.append(Paragraph("• • •", ParagraphStyle('Decorative', fontSize=16, alignment=TA_CENTER, textColor=colors.HexColor('#e5e7eb'))))

        story.append(PageBreak())

    def _add_table_of_contents(self, story, sections):
        """Add a colorful table of contents."""
        story.append(Paragraph("Table of Contents", self.styles['SectionHeader']))
        story.append(Spacer(1, 20))

        toc_data = []
        page_num = 2  # Start after cover page

        for section_title in sections.keys():
            if section_title not in ['Title', 'Cover']:
                toc_data.append([section_title, str(page_num)])
                page_num += 1

        if toc_data:
            toc_table = Table(toc_data, colWidths=[4*inch, 1*inch])
            
            # Create dynamic table style based on number of rows
            table_style = [
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 12),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('LEFTPADDING', (0, 0), (-1, -1), 12),
                ('RIGHTPADDING', (0, 0), (-1, -1), 12),
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e5e7eb')),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#1f2937')),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#dc2626')),
            ]
            
            # Add alternate row colors dynamically
            num_rows = len(toc_data)
            for i in range(num_rows):
                if i % 2 == 0:  # Even rows (0, 2, 4, etc.)
                    table_style.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor('#fef3c7')))
            
            toc_table.setStyle(TableStyle(table_style))
            story.append(toc_table)

        story.append(PageBreak())

    def _add_page_decorations(self, canvas, doc):
        """Add colorful page decorations like headers, footers, and borders."""
        page_num = canvas.getPageNumber()

        # Add colorful gradient border
        canvas.setStrokeColor(colors.HexColor('#667eea'))
        canvas.setLineWidth(1)
        canvas.rect(0.7*inch, 0.7*inch, 6.6*inch, 9.6*inch)

        # Add inner decorative border
        canvas.setStrokeColor(colors.HexColor('#f59e0b'))
        canvas.setLineWidth(0.3)
        canvas.rect(0.8*inch, 0.8*inch, 6.4*inch, 9.4*inch)

        # Add header with background
        canvas.setFillColor(colors.HexColor('#f8fafc'))
        canvas.rect(0.7*inch, 10.2*inch, 6.6*inch, 0.3*inch, fill=1)

        canvas.setFont('Helvetica-Bold', 10)
        canvas.setFillColor(colors.HexColor('#1e40af'))
        canvas.drawString(1*inch, 10.4*inch, "College Magazine")

        # Add decorative corner elements
        canvas.setFillColor(colors.HexColor('#dc2626'))
        canvas.circle(0.9*inch, 10.3*inch, 0.05*inch, fill=1)
        canvas.circle(7.1*inch, 10.3*inch, 0.05*inch, fill=1)

        # Add footer with background
        canvas.setFillColor(colors.HexColor('#f8fafc'))
        canvas.rect(0.7*inch, 0.2*inch, 6.6*inch, 0.3*inch, fill=1)

        # Add footer text
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#6b7280'))
        canvas.drawString(1*inch, 0.35*inch, f"Generated on {self._get_current_date()}")

        # Add page number with styling
        canvas.setFont('Helvetica-Bold', 10)
        canvas.setFillColor(colors.HexColor('#dc2626'))
        canvas.drawRightString(7*inch, 0.35*inch, f"Page {page_num}")

        # Add theme-specific decorative elements
        if self.theme == 'sports':
            canvas.setFillColor(colors.HexColor('#f59e0b'))
            canvas.drawString(6.3*inch, 10.4*inch, "🏆")
        elif self.theme == 'academic':
            canvas.setFillColor(colors.HexColor('#059669'))
            canvas.drawString(6.3*inch, 10.4*inch, "📚")
        elif self.theme == 'modern':
            canvas.setFillColor(colors.HexColor('#7c3aed'))
            canvas.drawString(6.3*inch, 10.4*inch, "🚀")

    def _get_theme_css(self):
        """Get CSS styles based on the selected theme."""
        if self.theme == 'professional':
            return """
                .title {
                    text-align: center;
                    color: #1a365d;
                    font-size: 2.8em;
                    margin-bottom: 10px;
                    font-weight: bold;
                }
                .subtitle {
                    text-align: center;
                    color: #4a5568;
                    font-size: 1.3em;
                    margin-bottom: 30px;
                }
                .section-header {
                    color: #c53030;
                    font-size: 1.6em;
                    border-bottom: 3px solid #c53030;
                    padding-bottom: 8px;
                    margin-top: 35px;
                    margin-bottom: 18px;
                    font-weight: bold;
                }
                .event-details {
                    margin-left: 20px;
                    background-color: #f7fafc;
                    padding: 12px;
                    border-left: 4px solid #3182ce;
                    border-radius: 4px;
                }
                .achievement {
                    margin-left: 30px;
                    background-color: #f0fff4;
                    padding: 10px;
                    margin-bottom: 6px;
                    border-left: 4px solid #38a169;
                    border-radius: 4px;
                }
            """
        elif self.theme == 'modern':
            return """
                .title {
                    text-align: center;
                    background: linear-gradient(45deg, #2E86AB, #A23B72);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-size: 3em;
                    margin-bottom: 10px;
                    font-weight: bold;
                }
                .subtitle {
                    text-align: center;
                    color: #F18F01;
                    font-size: 1.4em;
                    margin-bottom: 30px;
                }
                .section-header {
                    color: #A23B72;
                    font-size: 1.7em;
                    border-bottom: 3px solid #F18F01;
                    padding-bottom: 8px;
                    margin-top: 35px;
                    margin-bottom: 18px;
                    font-weight: bold;
                }
                .event-details {
                    margin-left: 20px;
                    background: linear-gradient(90deg, #FFF8DC, #F0E68C);
                    padding: 12px;
                    border-left: 4px solid #F18F01;
                    border-radius: 8px;
                }
                .achievement {
                    margin-left: 30px;
                    background: linear-gradient(90deg, #E6F3FF, #B3D9FF);
                    padding: 10px;
                    margin-bottom: 6px;
                    border-left: 4px solid #2E86AB;
                    border-radius: 8px;
                }
            """
        elif self.theme == 'academic':
            return """
                .title {
                    text-align: center;
                    color: #1e40af;
                    font-size: 2.6em;
                    margin-bottom: 10px;
                    font-weight: bold;
                    font-family: 'Times New Roman', serif;
                }
                .subtitle {
                    text-align: center;
                    color: #3730a3;
                    font-size: 1.2em;
                    margin-bottom: 30px;
                    font-style: italic;
                }
                .section-header {
                    color: #1e40af;
                    font-size: 1.5em;
                    border-bottom: 2px solid #3b82f6;
                    padding-bottom: 6px;
                    margin-top: 32px;
                    margin-bottom: 16px;
                    font-weight: bold;
                    font-family: 'Times New Roman', serif;
                }
                .event-details {
                    margin-left: 20px;
                    background-color: #eff6ff;
                    padding: 12px;
                    border-left: 4px solid #3b82f6;
                    border-radius: 4px;
                    font-family: 'Times New Roman', serif;
                }
                .achievement {
                    margin-left: 30px;
                    background-color: #f0f9ff;
                    padding: 10px;
                    margin-bottom: 6px;
                    border-left: 4px solid #0ea5e9;
                    border-radius: 4px;
                    font-family: 'Times New Roman', serif;
                }
            """
        elif self.theme == 'sports':
            return """
                .title {
                    text-align: center;
                    background: linear-gradient(45deg, #dc2626, #ea580c);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-size: 3.2em;
                    margin-bottom: 10px;
                    font-weight: bold;
                    text-transform: uppercase;
                }
                .subtitle {
                    text-align: center;
                    color: #f59e0b;
                    font-size: 1.5em;
                    margin-bottom: 30px;
                    text-transform: uppercase;
                    font-weight: bold;
                }
                .section-header {
                    color: #dc2626;
                    font-size: 1.8em;
                    border-bottom: 4px solid #f59e0b;
                    padding-bottom: 10px;
                    margin-top: 38px;
                    margin-bottom: 20px;
                    font-weight: bold;
                    text-transform: uppercase;
                }
                .event-details {
                    margin-left: 20px;
                    background: linear-gradient(90deg, #fef3c7, #fde68a);
                    padding: 14px;
                    border-left: 5px solid #f59e0b;
                    border-radius: 8px;
                    font-weight: bold;
                }
                .achievement {
                    margin-left: 30px;
                    background: linear-gradient(90deg, #dcfce7, #bbf7d0);
                    padding: 12px;
                    margin-bottom: 8px;
                    border-left: 5px solid #16a34a;
                    border-radius: 8px;
                    font-weight: bold;
                }
            """
        else:
            return self._get_theme_css()  # Default to professional

    def generate_pdf_reportlab(self, content, output_path):
        """Generate PDF using ReportLab with magazine-style layout."""
        doc = SimpleDocTemplate(output_path, pagesize=letter,
                              leftMargin=1*inch, rightMargin=1*inch,
                              topMargin=1.2*inch, bottomMargin=1*inch)
        story = []

        # Process content and create sections
        sections = self._parse_content_into_sections(content)

        # Create cover page
        self._add_cover_page(story, sections)

        # Add table of contents
        self._add_table_of_contents(story, sections)

        # Add content sections with better formatting
        for section_title, section_content in sections.items():
            print(f"DEBUG: Processing section '{section_title}' with {len(section_content)} items")
            if section_title in ['Event Overview', 'Academic Excellence']:
                story.append(PageBreak())

            story.append(Paragraph(section_title, self.styles['SectionHeader']))

            for item in section_content:
                if item.startswith(('* ', '- ', '• ')):
                    # Handle bullet points with better formatting
                    clean_item = item.lstrip('* -•').strip()
                    story.append(Paragraph(f"• {clean_item}", self.styles['Achievement']))
                elif item[0].isdigit() and item[1:3] in ['. ', ') ']:
                    # Handle numbered lists
                    story.append(Paragraph(item, self.styles['Achievement']))
                elif section_title.lower() == "event overview":
                    # Special handling for event details
                    story.append(Paragraph(item, self.styles['EventDetails']))
                else:
                    # Regular content with better spacing
                    story.append(Paragraph(item, self.styles['NormalTight']))

        print(f"DEBUG: Total story elements: {len(story)}")
        doc.build(story, onFirstPage=self._add_page_decorations,
                 onLaterPages=self._add_page_decorations)

    def _parse_content_into_sections(self, content):
        """Parse the LLM-generated content into magazine sections."""
        sections = {}
        current_section = None
        current_content = []
        lines = content.split('\n')

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check for title (first line with ** that contains magazine-related words)
            if line.startswith('**') and line.endswith('**') and not sections:
                title_text = line.strip('*').lower()
                if any(word in title_text for word in ['magazine', 'journal', 'chronicle', 'gazette', 'bulletin']):
                    sections['Title'] = [line.strip('*')]
                    continue

            # Check for section headers (marked with **)
            if line.startswith('**') and line.endswith('**'):
                # Save previous section
                if current_section and current_content:
                    sections[current_section] = current_content
                    current_content = []
                current_section = line.strip('*')
                continue

            # Handle bullet points and numbered lists
            if line.startswith(('* ', '- ', '• ')) or (line[0].isdigit() and len(line) > 2 and line[1:3] in ['. ', ') ']):
                if current_section:
                    current_content.append(line)
                continue

            # Regular content lines
            if current_section and line:
                current_content.append(line)

        # Add the last section
        if current_section and current_content:
            sections[current_section] = current_content

        # If parsing failed, fall back to line-based parsing
        if not sections:
            return self._parse_content_fallback(content)

        return sections

    def _parse_content_fallback(self, content):
        """Fallback parsing method for unstructured content."""
        sections = {}
        lines = content.split('\n')
        current_section = "Introduction"
        current_content = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Look for section-like headers
            if len(line) < 50 and (line.isupper() or line.istitle()):
                if current_content:
                    sections[current_section] = current_content
                    current_content = []
                current_section = line
                continue

            current_content.append(line)

        if current_content:
            sections[current_section] = current_content

        return sections

    def _get_current_date(self):
        """Get current date for magazine."""
        from datetime import datetime
        return datetime.now().strftime("%B %d, %Y")

    def _get_cover_styling(self):
        """Get theme-specific cover page styling."""
        if self.theme == 'professional':
            return """
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border-radius: 10px;
            """
        elif self.theme == 'modern':
            return """
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                border-radius: 15px;
            """
        elif self.theme == 'academic':
            return """
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                color: white;
                border-radius: 10px;
            """
        elif self.theme == 'sports':
            return """
                background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
                color: #2c3e50;
                border-radius: 15px;
            """
        else:
            return """
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border-radius: 10px;
            """

    def generate_html(self, content, output_path):
        """Generate HTML with magazine styling based on theme."""
        sections = self._parse_content_into_sections(content)

        # Theme-specific CSS
        theme_css = self._get_theme_css()

        # Get theme-specific cover styling
        cover_styling = self._get_cover_styling()

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>College Magazine</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 20px;
                    line-height: 1.6;
                    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                }}
                .magazine-container {{
                    background: white;
                    padding: 50px;
                    border-radius: 15px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                    position: relative;
                    overflow: hidden;
                }}
                .magazine-container::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 5px;
                    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
                }}
                {theme_css}
                .cover-page {{
                    text-align: center;
                    padding: 60px 20px;
                    min-height: 500px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    {cover_styling}
                }}
                .toc {{
                    background: #f8f9fa;
                    padding: 20px;
                    border-radius: 10px;
                    margin: 20px 0;
                }}
                .toc table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                .toc td {{
                    padding: 8px;
                    border-bottom: 1px solid #dee2e6;
                }}
                .content-section {{
                    margin-bottom: 40px;
                    padding: 20px;
                    background: #fafbfc;
                    border-radius: 8px;
                    border-left: 4px solid #667eea;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 60px;
                    color: #6c757d;
                    font-size: 0.9em;
                    border-top: 2px solid #dee2e6;
                    padding-top: 30px;
                    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                    margin: 40px -50px -50px -50px;
                    padding: 30px 50px;
                }}
                @media print {{
                    body {{ background: white; }}
                    .magazine-container {{ box-shadow: none; }}
                }}
            </style>
        </head>
        <body>
            <div class="magazine-container">
                <!-- Cover Page -->
                <div class="cover-page">
                    <h1 class="title">College Magazine</h1>
                    <h2 class="subtitle">Events & Achievements</h2>
                    <div class="decorative">✦ ✦ ✦</div>
                    <p class="pub-info">Published by: Your Organization</p>
                    <p class="pub-date">Generated on: {self._get_current_date()}</p>
                </div>

                <!-- Table of Contents -->
                <div class="toc">
                    <h3>Table of Contents</h3>
                    <table>
        """

        # Add TOC entries
        toc_entries = [section for section in sections.keys() if section not in ['Title', 'Cover']]
        for i, section in enumerate(toc_entries, 1):
            html_content += f"<tr><td>{section}</td><td>{i + 1}</td></tr>"

        html_content += """
                    </table>
                </div>
        """

        # Add content sections
        for section_title, section_content in sections.items():
            if section_title in ['Title', 'Cover']:
                continue

            html_content += f'<div class="content-section"><h3 class="section-header">{section_title}</h3>'

            for item in section_content:
                if item.startswith(('* ', '- ', '• ')):
                    clean_item = item.lstrip('* -•').strip()
                    html_content += f'<div class="achievement">• {clean_item}</div>'
                elif item[0].isdigit() and item[1:3] in ['. ', ') ']:
                    html_content += f'<div class="achievement">{item}</div>'
                else:
                    html_content += f'<p>{item}</p>'

            html_content += '</div>'

        html_content += f"""
                <div class="footer">
                    <p>Generated on: {self._get_current_date()}</p>
                    <p>Published by: Your Organization</p>
                    <div class="decorative">✦ ✦ ✦</div>
                </div>
            </div>
        </body>
        </html>
        """

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

    def generate_pdf_weasyprint(self, content, output_path):
        """Generate PDF from HTML using WeasyPrint with magazine styling."""
        # First generate HTML, then convert to PDF
        html_path = output_path.replace('.pdf', '.html')
        self.generate_html(content, html_path)
        HTML(filename=html_path).write_pdf(output_path)

# Example usage
if __name__ == "__main__":
    gen = MagazineGenerator()
    gen.generate_pdf_reportlab("Sample content", "sample.pdf")
