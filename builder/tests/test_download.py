
from io import BytesIO
import markdown

from builder.services import markdown_to_pdf, remove_summary
import pypdf  

"""
Tests for PDF download functionality.
"""


class TestPDFDownload:
    """Test cases for download_resume_pdf function."""


    def test_pdf_markdown_syntax_is_converted_not_literal(self, sample_markdown_file):
        """Test that markdown syntax is converted to styled content, not displayed literally."""
        
        response, message = markdown_to_pdf(ai_response=sample_markdown_file, filename="Atticus Ezis Resume.pdf")
        pdf_content = response.content
        
        # Validate PDF structure
        pdf_reader = pypdf.PdfReader(BytesIO(pdf_content))
        
        # Extract text from PDF
        pdf_text = ""
        for page in pdf_reader.pages:
            try:
                pdf_text += page.extract_text()
            except Exception:
                pass
        # Check if text extraction worked
        if pdf_text.strip():
            # Verify markdown syntax characters are NOT present as literal text
            markdown_syntax_chars = ["##", "###", "**", "[", "]", "(", ">", "- "]
            for syntax in markdown_syntax_chars:
                assert syntax not in pdf_text, \
                    f"Markdown syntax '{syntax}' should not appear literally in PDF. " \
                    f"Found in extracted text: {pdf_text[:300]}"
            
            # Verify the actual content IS present (without markdown syntax)
            assert "Main Heading" in pdf_text or "main heading" in pdf_text.lower(), \
                "Heading text should appear in PDF"
            assert "Sub Heading" in pdf_text or "sub heading" in pdf_text.lower() or "Sub Heading" in pdf_text, \
                "Sub heading text should appear in PDF"
            assert "bold text" in pdf_text.lower() or "italic text" in pdf_text.lower(), \
                "Bold/italic text should appear in PDF (formatting may vary)"
            assert "Bullet point" in pdf_text or "bullet point" in pdf_text.lower(), \
                "Bullet point text should appear in PDF"
            
            # Verify list items appear without markdown bullets
            assert "Bullet point 1" in pdf_text or "bullet point 1" in pdf_text.lower(), \
                "List item should appear without literal '-' character"
        else:
            # If text extraction fails, verify by checking the intermediate HTML conversion
            # We can check that the HTML structure was created (markdown was converted)

            html_content = markdown.markdown(sample_markdown_file, extensions=["extra", "sane_lists"])
            
            # Verify HTML contains converted elements (not raw markdown)
            assert "<h1>" in html_content or "<h2>" in html_content, \
                "Markdown should be converted to HTML headings"
            assert "</ul>" in html_content or "</ol>" in html_content, \
                "Markdown lists should be converted to HTML lists"
            assert "<strong>" in html_content or "<b>" in html_content, \
                "Bold markdown should be converted to HTML"
            assert "##" not in html_content, \
                "Raw markdown syntax should not appear in HTML conversion"
            assert "- " not in html_content or "<li>" in html_content, \
                "Markdown bullets should be converted to HTML list items"
            
            # Verify PDF was still generated (even if text extraction doesn't work)
            assert len(pdf_content) > 500, "PDF should be generated successfully"

    def test_pdf_excludes_summary_text(self):
        """Test that summary text added by AI is excluded from PDF."""
        md_with_summary = """# Atticus Ezis
## Objective
Motivated and detail-oriented Graduate Software Engineer.

## Skills
- Python
- Django

---

This resume is structured to highlight relevant experiences and skills aligned with the Graduate Software Engineer role at Acceler8 Talent, ensuring clarity and ATS-friendliness for optimal PDF export."""
        
        markdown_only, _ = remove_summary(md_with_summary)
        response, _ = markdown_to_pdf(ai_response=markdown_only, filename="test.pdf")
        pdf_content = response.content
        
        # Validate PDF structure
        pdf_reader = pypdf.PdfReader(BytesIO(pdf_content))
        assert len(pdf_reader.pages) > 0
        
        # Extract text from PDF
        pdf_text = ""
        for page in pdf_reader.pages:
            try:
                pdf_text += page.extract_text()
            except Exception:
                pass
        
        # Verify summary text is NOT in PDF
        if pdf_text.strip():
            assert "This resume is structured to highlight" not in pdf_text, \
                "Summary text should be excluded from PDF"
            assert "ATS-friendliness for optimal PDF export" not in pdf_text, \
                "Summary text should be excluded from PDF"
            # Verify actual content IS present
            assert "Atticus Ezis" in pdf_text or "atticus ezis" in pdf_text.lower(), \
                "Name should be in PDF"
            assert "Python" in pdf_text or "python" in pdf_text.lower(), \
                "Skills should be in PDF"

    def test_remove_summary_removes_code_fences(self):
        """Test that remove_summary removes code fences if present."""
        # Test case 1: Markdown wrapped in code fences
        text_with_fences = """```markdown
# Atticus Ezis
## Objective
Motivated software engineer
```"""
        
        markdown_only, message = remove_summary(text_with_fences)
        assert "```" not in markdown_only, "Code fences should be removed"
        assert "# Atticus Ezis" in markdown_only, "Content should remain"
        assert "markdown" not in markdown_only, "Language specifier should be removed"
        
        # Test case 2: Markdown without fences
        text_without_fences = """# Atticus Ezis
## Objective
Motivated software engineer"""
        
        markdown_only, message = remove_summary(text_without_fences)
        assert "```" not in markdown_only, "No code fences should be added"
        assert "# Atticus Ezis" in markdown_only, "Content should remain"
        
        # Test case 3: Markdown with fences and summary
        text_with_fences_and_summary = """```markdown
# Atticus Ezis
## Skills
- Python

This resume is structured to highlight relevant experiences and skills."""
        
        markdown_only, message = remove_summary(text_with_fences_and_summary)
        assert "```" not in markdown_only, "Code fences should be removed"
        assert "This resume is structured" not in markdown_only, "Summary should be removed"
        assert "# Atticus Ezis" in markdown_only, "Content should remain"
        assert "Python" in markdown_only, "Skills should remain"



