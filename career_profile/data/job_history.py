class Job:
    def __init__(self, title, company, start_date, end_date, responsibilities):
        self.title       = title
        self.company     = company
        self.start_date  = start_date
        self.end_date    = end_date
        self.responsibilities = responsibilities

JOB_HISTORY = [Job("Software Engineer", "TechCorp"     , "2020-01", "2023-05", ["Developed APIs", "Optimized database queries"]),
               Job("Data Analyst"     , "DataSolutions", "2018-06", "2019-12", ["Analyzed large datasets", "Generated reports"]),
               ]