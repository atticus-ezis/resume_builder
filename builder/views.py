from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import JodDescriptionForm, SearchForm
from .services import (
    OpenAIService,
    create_job_app_resume,
    create_job_app_cover_letter,
    markdown_to_pdf,
)
from datetime import datetime
from .models import JobApplication


# Create your views here.
def build_resume(request):
    if request.method == "POST":
        form = JodDescriptionForm(request.POST)
        if form.is_valid():
            job_data = form.cleaned_data
            include_cover_letter = job_data.get("include_cover_letter", False)
            company_name = job_data.get("company_name")

            if include_cover_letter:
                job_data["date"] = datetime.now().strftime("%Y-%m-%d")

            ai_service = OpenAIService()
            ai_response = ai_service.execute_generate(
                job_data, include_cover_letter=include_cover_letter
            )
            # Store in session for downloads
            request.session["resume_content"] = ai_response.get("resume", "")
            request.session["company_name"] = company_name
            if include_cover_letter:
                request.session["cover_letter_content"] = ai_response.get(
                    "cover_letter", ""
                )
            request.session["include_cover_letter"] = include_cover_letter

            context = {
                "resume_content": ai_response.get("resume", ""),
            }
            if include_cover_letter:
                context["cover_letter_content"] = ai_response.get("cover_letter", "")

            return render(request, "forms/review_content.html", context)

    else:
        form = JodDescriptionForm()
    return render(request, "forms/job_description_form.html", {"form": form})


def resume_pdf_download(request):
    resume_content = request.POST.get("resume_content")
    company_name = request.session.get("company_name")
    app_id = request.session.get("app_id")
    if resume_content:
        request.session["resume_content"] = resume_content
        resume_pdf, message = markdown_to_pdf(
            resume_content, filename="Atticus Ezis Resume.pdf", request=request
        )
        print(message)
        new_app_id = create_job_app_resume(company_name, app_id, resume_content)
        if app_id != new_app_id:
            request.session["app_id"] = new_app_id
        return resume_pdf
    else:
        messages.error(request, "No resume content found.")
        return redirect("build_resume")


def cover_letter_pdf_download(request):
    cover_letter_content = request.POST.get("cover_letter_content")
    company_name = request.session.get("company_name")
    app_id = request.session.get("app_id")
    if cover_letter_content:
        request.session["cover_letter_content"] = cover_letter_content
        cover_letter_pdf, message = markdown_to_pdf(
            cover_letter_content,
            filename="Atticus Ezis Cover Letter.pdf",
            request=request,
        )
        print(message)
        new_app_id = create_job_app_cover_letter(
            company_name, app_id, cover_letter_content
        )
        if app_id != new_app_id:
            request.session["app_id"] = new_app_id
        return cover_letter_pdf
    else:
        messages.error(request, "No cover letter content found.")
        return redirect("build_resume")


def view_job_applications(request):
    form = SearchForm(request.GET or None)
    job_applications = JobApplication.objects.order_by("-created_at")

    if form.is_valid():
        search_query = form.cleaned_data.get("company_name")
        if search_query:
            job_applications = job_applications.filter(
                company_name__icontains=search_query
            )

    context = {"job_applications": job_applications, "form": form}
    return render(
        request,
        "forms/view_job_applications.html",
        context,
    )


def job_application_detail(request, id):
    job_application = get_object_or_404(JobApplication, id=id)
    context = {
        "job_application": job_application,
    }
    return render(request, "forms/job_application_detail.html", context)
