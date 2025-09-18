from django.shortcuts import render

def home(request):
    # Bio Section
    bio = {
        "name": "Nayna",
        "title": "Aspiring Data Enthusiast | Python Developer | Problem Solver"
    }

    # About Section
    about_text = (
        "I am passionate about Python, Data Science, and FullStack Development. "
        "I love solving real-world problems and building projects that make an impact."
    )

    # Skills Section
    skills = [
        "Python, Django",
        "Pandas, NumPy, Matplotlib",
        "SQL (MongoDB, MySQL)",
        "JavaScript (React.js, Node.js)"
    ]

    # Projects Section
    projects = [
        {
            "title": "CLI Project - Database Management",
            "description": "Developed and managed SQLite database using Python's sqlite3 library, implemented CRUD operations, CSV integration, and console-based user interaction.",
            "link": "https://github.com/NaynaKoju/cli-project-python"
        },
        {
            "title": "Heart-Stroke Prediction",
            "description": "Evaluated multiple ML models with scikit-learn, performed hyperparameter tuning and model evaluation, using metrics like F1-Score, ROC Curve, and Confusion Matrix.",
            "link": "https://github.com/NaynaKoju/Heartstroke-Prediction"
        },
        {
            "title": "Web Scraping Project",
            "description": "Built a Python web scraper using BeautifulSoup, requests, Pandas, JSON, Regex, and OOP to fetch stock price data from Sharesansar and store it in JSON.",
            "link": "https://github.com/NaynaKoju/Web-Scrapping"
        },
        {
            "title": "Fully Funded Login/Registration",
            "description": "Designed a secure login system with captcha, email verification, password hashing, and Django backend integration.",
            "link": "https://github.com/NaynaKoju/Flutter-Login-DB"
        },
        {
            "title": "Bank Application (Java)",
            "description": "Developed a full bank app with account/user management, CRUD operations, and GUI using Java classes.",
            "link": "https://github.com/NaynaKoju/BankApplication-JavaFunctions"
        },
        {
            "title": "Baby Buy (Mobile App)",
            "description": "Implemented user authentication, product management, shopping cart, checkout process, and messaging features for mobile app.",
            "link": "https://github.com/NaynaKoju/Baby-buy"
        },
        {
            "title": "Fun-Olympic Live Streaming",
            "description": "Developed a live streaming website with user registration, live chat, and additional interactive features using Django, Python, and JavaScript.",
            "link": "https://github.com/NaynaKoju/funolympic"
        },
        {
            "title": "School Website (React + CMS)",
            "description": "Full-stack school website with custom CMS, JWT-based admin auth, dynamic page content, and MySQL/MongoDB backend integration.",
            "link": "https://github.com/NaynaKoju/React-projects"
        },
        {
            "title": "Blog Backend API",
            "description": "Built secure RESTful API for a blogging platform with JWT authentication, role-based authorization, and CRUD operations for posts, users, comments, and tags.",
            "link": "https://github.com/NaynaKoju/blog-api-nayna-koju"
        }
    ]

    # Contact Section
    contact = {
        "email": "kojunayna@gmail.com",
        "linkedin": "https://www.linkedin.com/in/nayna-koju/",
        "github": "https://github.com/NaynaKoju"
    }

    context = {
        "bio": bio,
        "about_text": about_text,
        "skills": skills,
        "projects": projects,
        "contact": contact
    }

    return render(request, "home.html", context)
