
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
            "Collaborated in Agile workflows. Participated in bi-weekly Sprints, Daily Stand-ups, Backlog Grooming and Retrospectives "
            "using slack, discord, and github for communication and project management."
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

projects = {
    "Portfolio with AI Chat": [
        {
            "Tech Stack": ["Next.js", "TypeScript", "Tailwind CSS", "React", "GitHub Actions", "Vercel", "RAG", "AI"]
        },
        {
            "Description": (
                "Developed a full stack portfolio application using Next.js and TypeScript, deployed on Vercel."
                "Integrated a Retrieval-Augmented Generation (RAG) AI chatbot trained on my professional experiences "
                "to simulate mock interviews and answer career-related questions."
            )
        }
    ],
    "Django Blog": [
        {
            "Tech Stack": ["Django", "AWS", "EC2", "Elastic Beanstalk", "PostgreSQL", "Bash"]
        },
        {
            "Description": (
                "Built and deployed a full stack Django web application hosted on AWS Elastic Beanstalk with a custom domain and SSL certification."
                "Configured EC2 instances and PostgreSQL database via Bash scripts to automate deployment and manage backend services."
            )
        }
    ]
}



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
    "education": {
        "degree": "Bachelor of Science in Business Administration",
        "university": "University of Colorado Boulder",
        "Relevant Courses": ["Intro to Python", "Computer Data Science and Analytics", "Digital Marketing", "Calculus 2"],
        "Accomplishments": [
            "Project Leader, Entrepreneurship Capstone — Led a team to design and pitch a business plan for an online marketplace, demonstrating leadership and cross-functional collaboration.",
            "Alteryx Core Certified — Corporate-sponsored certification by Alteryx Inc., validating strong analytical, data processing, and problem-solving skills."
        ]
    },


    "certifications": [
        "Responsive Web Design (freeCodeCamp) - Designed product landing page.",
        "JavaScript Algorithms and Data Structures (freeCodeCamp) - Built RPG game and Pokémon search engine.",
        "Databases and SQL for Python (IBM) - Analyzed graduation rates of Chicago Public Schools using Excel.",
        "Python for Data Science, AI & Development (IBM) - Automated public data collection with web-scrapping.",
        "Alteryx Core Certified, (Alteryx Inc) - Validates proficiency in data preparation, workflow automation, and analytical problem-solving.",
        ["Certified LLM Developer Course (TowardsAI) - provides the core technical stack for building production-grade generative AI applications, "
        "including mastery of Prompt Engineering, integrating RAG (Retrieval-Augmented Generation) with tools like LlamaIndex, "
        "and implementing Fine-Tuning techniques across leading models such as Gemini, Llama, and OpenAI. Crucially, "
        "the course emphasizes LLM Evaluation by teaching how to rigorously test and validate application outputs based on key metrics like "
        "Relevance, Coherence, and Grounded-ness to ensure high-quality, trustworthy performance.", {"status": "In Progress"}],
    ]
       
}

