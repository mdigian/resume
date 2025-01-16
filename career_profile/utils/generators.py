from career_profile.data.job_history import JOB_HISTORY
from career_profile.data.projects    import PROJECTS

from career_profile.data.skills      import TECHNICAL_SKILLS
from career_profile.data.highlights  import CAREER_HIGHLIGHTS
from career_profile.utils.filters    import filter_by_role

def generate_profile(role):
    filtered_jobs     = filter_by_role(JOB_HISTORY, role)
    filtered_projects = filter_by_role(PROJECTS, role)

    profile = {
        "Role": role,
        "Job History": filtered_jobs,
        "Projects": filtered_projects,
        "Skills": TECHNICAL_SKILLS,
        "Highlights": CAREER_HIGHLIGHTS
    }

    return profile