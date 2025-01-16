class Project:

    def __init__(self, name, description, technologies, role):
        self.name         = name
        self.description  = description
        self.technologies = technologies
        self.role         = role

PROJECTS = [
    Project("AI Chatbot"     , "Built a chatbot using NLP"             , ["Python", "TensorFlow"], "Software Engineer"),
    Project("Sales Dashboard", "Designed a dashboard for sales metrics", ["Tableau", "SQL"]      , "Data Analyst"),
]