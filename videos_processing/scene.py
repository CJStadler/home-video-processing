class Scene:
    def __init__(self, start_second, end_second, date=None, location=None, people=[], description=""):
        self.start_second = start_second
        self.end_second = end_second
        self.date = date
        self.location = location
        self.people = people
        self.description = description
