# ResumeHelper

A Django-based web application that uses OpenAI's GPT-4 to generate personalized resumes and cover letters tailored to specific job descriptions. The application allows users to input job details, review AI-generated content, and download professional PDFs.

## Features

- **AI-Powered Resume Generation**: Uses OpenAI GPT-4o-mini to create tailored resumes based on job descriptions
- **Cover Letter Generation**: Optional cover letter generation alongside resume creation
- **Interactive Review**: Review and edit generated content before downloading
- **PDF Export**: Download professionally formatted PDFs of resumes and cover letters
- **ATS-Friendly Formatting**: Optimized for Applicant Tracking Systems

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Homebrew (for macOS users - required for system libraries)
- OpenAI API key

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ResumeHelper
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install System Dependencies (macOS)

**Important**: WeasyPrint requires system-level libraries that must be installed via Homebrew. Install these dependencies before installing Python packages:

```bash
brew install pango gdk-pixbuf libffi cairo
```

If you don't have Homebrew installed, install it first from [https://brew.sh](https://brew.sh)

**Note for Linux users**: You may need to install similar packages using your distribution's package manager:

```bash
# Ubuntu/Debian
sudo apt-get install python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# Fedora/CentOS
sudo yum install cairo-devel pango-devel gdk-pixbuf2-devel libffi-devel
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5. Environment Setup

Create a `.env` file in the project root directory:

```bash
touch .env
```

Add your OpenAI API key to the `.env` file:

```
API_KEY=your_openai_api_key_here
```

### 6. Database Setup

Run Django migrations:

```bash
python manage.py migrate
```

### 7. Create Superuser (Optional)

If you want to access the Django admin panel:

```bash
python manage.py createsuperuser
```

## Usage

### Starting the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Using the Application

1. **Fill Out Job Description Form**:

   - Enter company name, address, and hiring manager name
   - Provide company description, job responsibilities, and requirements
   - Optionally check "Include Cover Letter" to generate both documents

2. **Review Generated Content**:

   - Review the AI-generated resume and/or cover letter
   - Edit the content if needed

3. **Download PDFs**:
   - Click "Download Resume PDF" or "Download Cover Letter PDF"
   - PDFs will be generated and downloaded automatically

## Troubleshooting

### Error: `cannot load library 'libpango-1.0-0'`

This error occurs when the system libraries required by WeasyPrint are not installed.

**Solution for macOS**:

```bash
brew install pango gdk-pixbuf libffi cairo
```

After installing, restart your Django development server:

```bash
# Stop the server (Ctrl+C) and restart
python manage.py runserver
```

### Error: OpenAI API Key Not Found

Make sure you have created a `.env` file in the project root with your API key:

```
API_KEY=your_actual_api_key_here
```

### PDF Generation Issues

If PDF downloads fail:

1. Ensure all system dependencies are installed (see Installation section)
2. Restart the Django server after installing system libraries
3. Check that WeasyPrint is properly installed: `pip show weasyprint`

## Project Structure

```
ResumeHelper/
├── builder/              # Main Django app
│   ├── forms.py         # Form definitions
│   ├── services.py      # OpenAI service and PDF generation
│   ├── views.py         # View handlers
│   └── personal_info.py # Personal information data
├── templates/           # HTML templates
│   └── forms/          # Form templates
├── resume_helper/       # Django project settings
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies

```

## Technologies Used

- **Django 5.2.7**: Web framework
- **OpenAI API**: AI content generation
- **WeasyPrint**: PDF generation from HTML
- **Markdown**: Content formatting

## License

[Add your license here]

## Contributing

[Add contribution guidelines if applicable]
