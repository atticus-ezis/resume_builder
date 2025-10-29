
experiences = [
    {
        "company": "Mugna Tech",
        "address": "Davao City, Philippines",
        "title": "Junior Backend Developer",
        "start_date": "2024-06-01",
        "end_date": "2025-08-01",
        "tech_stack": ["Python", "Django", "Django REST Framework", "Pytest", "PostgreSQL", "Celery", "Redis", "Docker", "Git"],
        "summary": (
            "Developed the accounting software for Rizal Memorial Colleges Inc."
            "Designed REST API endpoints using Django REST Framework."
            "Collaborated in Agile workflows. Participated in bi-weekly Sprints, Daily Stand-ups, Backlog Grooming and Retrospectives."
            "reviews to ensure best practices."
            "integrated tests, CI/CD, and deployment workflows."
            "collaborated closely with frontend developers."
        ),
        "accomplishments": [
            {"Payment Processor": [
                "Designed and implemented a scalable payment processing system handling both student payments and government subsidies."
                "Developed database schema, API endpoints, and business logic to manage multiple payment types (cash, check, post-dated check, online)."
                "Translated complex business rules into maintainable, configuration-driven code, enabling rapid addition of new payment methods without altering core logic."
                "Utilized inheritance and polymorphism to manage transaction types and validation logic, improving modularity and reducing code duplication."
                "Resolved race conditions in transaction numbering through database-level locking (select_for_update) and atomic transactions to ensure data integrity."
                "Linked multiple bank accounts across government and student profiles, ensuring accurate reconciliation of outstanding balances and installment payments."
                "Result: Reduced payment processing errors and improved system reliability, enabling seamless scaling for future payment types."
                ]
            },
            {"Soft Delete Feature":[
                "Implemented a soft delete manager for all models.",
                "Designed a Manager class and custom QuerySet to easily manage and view soft deleted objects in a repeatable way.",
            ]},
            {"CSV Export Feature":[
                "Created a CSV export for Jounral Entries, cleaned data from postgres into csv format using pandas and numpy.",
                "Used redis to run the creation and download of CSV files in the background without compromising user experience.",
                "Architecture & Design Patterns",
                "I implemented a service-oriented architecture where CSV generation logic is encapsulated in a dedicated service class. This follows the Single Responsibility Principle and makes the code highly testable and reusable across different parts of the application."
                "I used asynchronous task processing with Celery to handle CSV generation in the background. This prevents API timeouts on large datasets and provides a much better user experience. The API responds immediately with a task ID that clients can use to track progress."
                "I created a response builder pattern with GenerateCSVResponse that standardizes how we return CSV task information. This means any endpoint that generates CSVs uses the same response format, making the API consistent and easier to maintain."
                "I separated the data processing logic (JournalEntryCSVServices) from the API logic (ViewSet action) and response formatting (GenerateCSVResponse). This makes each component focused on one responsibility and easier to test and modify independently."
                "The asynchronous approach also provides better error handling - if CSV generation fails, it doesn't crash the API request. The task system can retry failed operations and provide detailed error logging."
                "This pattern is highly extensible - I can easily add new CSV generation endpoints by creating new service classes and using the same response builder. The architecture supports different data sources while maintaining consistent behavior."
            ]},
            {"Data Cleaning and Analysis":[
                "Imported third party student payment data. Handled logic that created downpayments based on academic term. Used prefetcth and bulk queries to optimize database queries."
            ]},
            {"Statistics":[
                "Creating 78 testcases."

            ]}

        ],

    },
    {
        "company": "AmericanLiterature.com",
        "address": "Boulder, CO",
        "title": "Intern Developer",
        "start_date": "2024-01-01",
        "end_date": "2024-05-01",
        "tech_stack": ["Python", "Django", "Django REST Framework", "PostgreSQL", "Celery", "Redis", "Docker", "Git"],
        "summary": (
            "Helped maintain the website and database for AmericanLiterature.com"
        ),
        "accomplishments": (
            "Completed 700+ hours of backend development training, gaining hands-on experience with modern"
            "backend technologies and best practices."
            "Built and optimized a high-traffic website serving 400K+ monthly users, leveraging PostgreSQL and Redis for scalability and performance."
            "Strengthened skills in database design, API development, and asynchronous processing, applying concepts to real-world projects."
        ),
    }
]

projects = [
    
    {
        "Portfolio with AI Chat": [
            {
                "Tech Stack": ["Next.js", "Tailwind CSS", "TypeScript", "React", "Git", "GitHub Actions", "AI", "RAG"]
            },
            {
                "Description": (
                    "I created a full stack application with Next.js. The site uses a RAG powered AI chatbot to answer questions about my experiences and projects"
                    "to mock personal interviews."
                )
            },
        ]
    },
    {
        "Blogsforthecriminallyinsane": [
            {
                "Tech Stack": ["Django", "AWS"]
            },
            {
                "Description": (
                    "I created a full stack application with Django."
                    "Used a custom custom domain, was SSL certified, and hosted on AWS through Elastic Beanstalk."
                    "configured Ec2 instance to run the application and database using Bash."
                )
            }
        ]
    }
]

my_personal_info = {
    "name": "Atticus Ezis",
    "nationality": "United States",
    "email": "ezisatticus@gmail.com",
    "address": "5101 5th St, Boulder, CO 80304",
    "linkedin": "https://www.linkedin.com/in/atticus-ezis",
    "github": "https://github.com/atticus-ezis",
    "portfolio": "https://next-js-portfolio-git-main-atticus-ezis-projects.vercel.app/",
    "skills": {
        "Languages/Frameworks": ["Python", "Django REST Framework", "PostgreSQL"],
        "Infra/Tools": ["Docker", "Redis", "Celery", "Git/GitHub", "GitHub Actions"],
        "Testing/Quality": ["Pytest", "Factory Boy", "Faker", "Parametrized tests", "CI/CD"],
        "API": ["RESTful design", "DRF ViewSets/Serializers/Permissions", "Swagger", "Postman"],
        "Auth/Security": ["JWT/Token auth"],
        "Cloud/DevOps": ["AWS Elastic Beanstalk deployments", "Amazon S3 pre-signed URL integration"]
    },
    "experience": experiences,
    "projects": projects,
    "education": [
        "Bachelor of Science in Business Administration", 
        "University of Colorado Boulder", 
        {
            "Relevant Courses": ["Intro to Python", "Computer Data Science and Analytics", "Digital Marketing", "Calculus 2" ]
        },
        {
            "Accomplishments": [
                "Voted Project Leader for entreprenuership Captstone Project. Designed and picthed a business plan for a cottage industry online marketplace.",
                "Alteryx Core Certified, a corporate sponsored certification by Alteryx Inc. Demonstrating storng analytical thinking and data analysis skills."
            ]
        },
    ],
       
}

