import os
from dotenv import load_dotenv
from openai import OpenAI
from .personal_info import my_personal_info
import markdown
from django.http import HttpResponse

load_dotenv()

api_key = os.getenv('API_KEY')

def download_resume_pdf(markdown_text, output_path="Atticus Ezis Resume.pdf"):
    from weasyprint import HTML
    
    html_content = markdown.markdown(markdown_text, extensions=["extra", "nl2br"])

    styled_html = f"""
    <html>
      <head>
        <style>
          body {{ font-family: Helvetica, Arial, sans-serif; margin: 30px; }}
          h1, h2, h3 {{ color: #222; }}
          hr {{ border: none; border-top: 1px solid #ccc; }}
          ul {{ margin-left: 1em; }}
          a {{ color: #0366d6; text-decoration: none; }}
        </style>
      </head>
      <body>{html_content}</body>
    </html>
    """
    pdf_bytes = HTML(string=styled_html).write_pdf()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename={output_path}'
    return response




class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('API_KEY'))
        self.model = "gpt-4o-mini"

    def job_description_info(self, data):
        response = {
            'company_name': data.get('company_name'),
            'address': data.get('address'),
            'hiring_manager_name': data.get('hiring_manager_name'),
            'company_description': data.get('company_description'),
            'job_description': data.get('job_description'),
            'desired_experience': data.get('desired_experience')
        }
        return {key: value for key, value in response.items() if value is not None}

    def personal_info(self):
        return my_personal_info

    def generate_resume_prompt(self, job_description, personal_info):

        role_description = (
            f"You are a professional resume writer. "
            "Always maintain factual accuracy, use a confident tone, "
            "and follow clean formatting optimized for ATS parsing and PDF conversion. "
            "Ensure sections are clearly separated and labeled."
        )

        prompt = (
            f"Return a resume optimized for PDF export. "
            "Content must be ATS-friendly, concise, and persuasive. "
            "Focus on clarity, keyword alignment, and measurable impact.\n\n"
            "=== JOB DESCRIPTION ===\n"
            f"{job_description}\n\n"
            "=== PERSONAL DETAILS ===\n"
            f"{personal_info}\n\n"
            "=== OUTPUT REQUIREMENTS ===\n"
            "- Resume tailored to the job.\n"
            "- Do not invent qualifications or experience not present in the details.\n"
            "- Return as Markdown or plain text for clean export."
        )

        return role_description, prompt
    
    def generate_cover_letter_prompt(self, job_description, personal_info):

        role_description = (
            f"You are a professional cover letter writer. "
            "Always maintain factual accuracy, use a confident tone, "
            "and follow clean formatting optimized for ATS parsing and PDF conversion. "
            "Ensure sections are clearly separated and labeled."
        )

        prompt = (
            f"Return a cover letter optimized for PDF export. "
            "Content must be ATS-friendly, concise, and persuasive. "
            "Focus on clarity, keyword alignment, and measurable impact.\n\n"
            "=== JOB DESCRIPTION ===\n"
            f"{job_description}\n\n"
            "=== PERSONAL DETAILS ===\n"
            f"{personal_info}\n\n"
            "=== OUTPUT REQUIREMENTS ===\n"
            "- Cover letter tailored to the job.\n"
            "- Do not invent qualifications or experience not present in the details.\n"
            "- Return as Markdown or plain text for clean export."
        )

        return role_description, prompt

    def api_call(self, role_description, prompt):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": role_description},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=4000,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(e)
            return None

    def execute_generate(self, job_data, include_cover_letter=False):
        job_description_info = self.job_description_info(job_data)
        personal_info = self.personal_info()

        role_description, prompt = self.generate_resume_prompt(job_description_info, personal_info)
        resume_response = self.api_call(role_description, prompt)

        response = {
            'resume': resume_response
        }
        
        if include_cover_letter:
            role_description, prompt = self.generate_cover_letter_prompt(job_description_info, personal_info)
            cover_letter_response = self.api_call(role_description, prompt)
            response['cover_letter'] = cover_letter_response

        return response