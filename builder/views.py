from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import JodDescriptionForm 
from .services import OpenAIService, markdown_to_pdf


# Create your views here.
def build_resume(request):
    if request.method == 'POST':
        form = JodDescriptionForm(request.POST)
        if form.is_valid():
            job_data = form.cleaned_data
            include_cover_letter = job_data.get('include_cover_letter', False)
            ai_service = OpenAIService()
            ai_response = ai_service.execute_generate(job_data, include_cover_letter=include_cover_letter)

            # Store in session for downloads
            request.session['resume_content'] = ai_response.get('resume', '')
            if include_cover_letter:
                request.session['cover_letter_content'] = ai_response.get('cover_letter', '')
            request.session['include_cover_letter'] = include_cover_letter

            context = {
                'resume_content': ai_response.get('resume', ''),
            }
            if include_cover_letter:
                context['cover_letter_content'] = ai_response.get('cover_letter', '')

            return render(request, 'forms/review_content.html', context)

    else:
        form = JodDescriptionForm()
    return render(request, 'forms/job_description_form.html', {'form': form})

def resume_pdf_download(request):
    resume_content = request.session.get('resume_content', None)
    if resume_content:
        resume_pdf, message = markdown_to_pdf(resume_content, filename='Atticus Ezis Resume', request=request)
        print(message)
        return resume_pdf
    else:
        messages.error(request, 'No resume content found.')
        return redirect('build_resume')

def cover_letter_pdf_download(request):
    cover_letter_content = request.session.get('cover_letter_content', None)
    if cover_letter_content:
        cover_letter_pdf, message = markdown_to_pdf(cover_letter_content, filename='Atticus EzisCover Letter', request=request)
        print(message)
        return cover_letter_pdf
    else:
        messages.error(request, 'No cover letter content found.')
        return redirect('build_resume')