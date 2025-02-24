from career_profile.utils.generators import generate_profile

def display_profile(profile):

    print(f"Role: {profile['Role']}")

    print("\nJob History:");
    for job in profile["Job History"]:      print(f"- {job.title} at {job.company} ({job.start_date} - {job.end_date})")

    print("\nProjects:");
    for project in profile["Projects"]:     print(f"- {project.name}: {project.description} [Technologies: {', '.join(project.technologies)}]")

    print("\nSkills:");                     print(", ".join(profile["Skills"]))

    print("\nCareer Highlights:");
    for highlight in profile["Highlights"]: print(f"- {highlight}")

if __name__ == "__main__":   # __name__ built-in variable set to __main__ when script run directly

    role    = input("Enter job role: ")
    profile = generate_profile(role)
    display_profile(profile)