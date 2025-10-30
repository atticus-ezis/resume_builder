from django import forms

class JodDescriptionForm(forms.Form):
    company_name = forms.CharField(label='Company Name', max_length=100)
    address = forms.CharField(label='Company Address', max_length=100)
    hiring_manager_name = forms.CharField(label='Hiring Manager Name', max_length=100, required=False)
    job_title = forms.CharField(label='Job Title', max_length=100)
    company_description = forms.CharField(
        label='Company Description', 
        max_length=5000,
        widget=forms.Textarea(
            attrs={
                'rows': 10, 
                'cols': 50,
                'placeholder': 'Enter the job description here'
            }
        )
    )
    job_description = forms.CharField(
        label='Job Responsibilities',
        max_length=5000,
        widget=forms.Textarea(
            attrs={
                'rows': 20, 
                'cols': 50, 
                'placeholder': 'Enter the role description here'
            }
        )
    )
    desired_experience = forms.CharField(
        label='Job Requirements',
        max_length=5000,
        widget=forms.Textarea(
            attrs={
                'rows': 20, 
                'cols': 50, 
                'placeholder': 'Enter the job requirements here'
            }
        )
    )
    include_cover_letter = forms.BooleanField(label='Include Cover Letter', required=False)


# class ResumeReviewForm(forms.Form):
#     content = forms.CharField(
#         label='Resume Content',
#         widget=forms.Textarea(
#             attrs={
#                 'rows': 30,
#                 'cols': 80,
#                 'class': 'form-control'
#             }
#         )
#     )


# class CoverLetterReviewForm(forms.Form):
#     content = forms.CharField(
#         label='Cover Letter Content',
#         widget=forms.Textarea(
#             attrs={
#                 'rows': 25,
#                 'cols': 80,
#                 'class': 'form-control'
#             }
#         )
#     )
