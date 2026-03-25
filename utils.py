def calculate_resume_score(resume_text, skills):
    score = 0
    feedback = []

    if not resume_text or len(resume_text.strip()) == 0:
        return 10, ["Resume not detected properly. Upload a proper PDF/DOCX file."]

    resume_text_lower = resume_text.lower()

    # Skill Match (50 marks)
    matched = 0
    for skill in skills:
        if skill.lower() in resume_text_lower:
            matched += 1

    if skills:
        skill_score = (matched / len(skills)) * 50
        score += skill_score

    if matched < len(skills):
        feedback.append("Add more relevant skills in resume.")

    # Resume Length (20 marks)
    if len(resume_text) > 800:
        score += 20
    else:
        feedback.append("Resume is too short. Add more content.")

    # Sections Check (30 marks)
    sections = ["project", "experience", "education", "skills"]

    section_score = 0
    for sec in sections:
        if sec in resume_text_lower:
            section_score += 7.5
        else:
            feedback.append(f"Add {sec} section.")

    score += section_score

    return int(score), feedback
