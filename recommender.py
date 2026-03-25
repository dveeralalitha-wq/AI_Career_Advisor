def recommend_roles(skills, interest):
    roles = []

    interest = interest.lower()

    if "data" in interest:
        roles = [
            "Data Analyst",
            "Data Scientist",
            "Business Intelligence Analyst",
            "Data Engineer"
        ]

    elif "ai" in interest:
        roles = [
            "AI Engineer",
            "Machine Learning Engineer",
            "Deep Learning Engineer",
            "NLP Engineer"
        ]

    elif "banking" in interest:
        roles = [
            "Business Analyst",
            "Risk Analyst",
            "Credit Analyst",
            "Financial Analyst"
        ]

    else:
        roles = [
            "Software Developer",
            "Backend Developer",
            "Frontend Developer"
        ]

    return roles


# ✅ THIS FUNCTION WAS MISSING (CAUSE OF ERROR)
def recommend_skills(skills, interest):
    rec = []

    interest = interest.lower()

    if "data" in interest:
        rec = ["Python", "SQL", "Pandas", "NumPy", "Power BI"]

    elif "ai" in interest:
        rec = ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch"]

    elif "banking" in interest:
        rec = ["Excel Advanced", "Financial Analysis", "Risk Management", "SQL"]

    else:
        rec = ["Python", "Git", "DSA"]

    return rec


def recommend_industries(interest):
    interest = interest.lower()

    if "ai" in interest:
        return ["IT", "AI Startups", "Research Labs"]

    if "banking" in interest:
        return ["Banking", "Finance", "FinTech"]

    if "data" in interest:
        return ["IT", "E-commerce", "Consulting"]

    return ["IT", "General Industry"]


def career_path(interest):
    interest = interest.lower()

    if "data" in interest:
        return [
            "Step 1: Learn Python (basics → advanced)",
            "Step 2: Learn SQL for data handling",
            "Step 3: Learn Pandas, NumPy",
            "Step 4: Data Visualization (Power BI)",
            "Step 5: Build 3 projects",
            "Step 6: Upload to GitHub",
            "Step 7: Apply internships",
            "Step 8: Get Data Analyst job"
        ]

    elif "ai" in interest:
        return [
            "Step 1: Learn Python + Math",
            "Step 2: Learn Machine Learning",
            "Step 3: Build ML projects",
            "Step 4: Learn Deep Learning",
            "Step 5: Build AI apps",
            "Step 6: Apply internships",
            "Step 7: Become AI Engineer"
        ]

    return [
        "Step 1: Learn basics",
        "Step 2: Build projects",
        "Step 3: Apply internships",
        "Step 4: Get job"
    ]


def recommend_courses(interest):
    interest = interest.lower()

    if "data" in interest:
        return [
            ("Google Data Analytics", "https://www.coursera.org/professional-certificates/google-data-analytics"),
            ("IBM Data Science", "https://www.coursera.org/professional-certificates/ibm-data-science"),
            ("Kaggle", "https://www.kaggle.com/")
        ]

    elif "ai" in interest:
        return [
            ("Machine Learning - Andrew Ng", "https://www.coursera.org/learn/machine-learning"),
            ("Deep Learning Specialization", "https://www.coursera.org/specializations/deep-learning"),
            ("FastAI", "https://course.fast.ai/")
        ]

    return [
        ("Python Bootcamp", "https://www.udemy.com/course/complete-python-bootcamp/")
    ]
