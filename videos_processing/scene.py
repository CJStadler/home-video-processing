class Scene:
    def __init__(self, start_second, end_second, thumbnail_second=None, date=None, location=None, people=[], description=""):
        self.start_second = start_second
        self.end_second = end_second
        self.thumbnail_second = thumbnail_second
        self.date = date
        self.location = location
        self.people = people
        self.description = description

    def to_dict(self):
        return {
            "start_second": self.start_second,
            "end_second": self.end_second,
            "thumbnail_second": self.thumbnail_second,
            "date": self.date,
            "location": self.location,
            "people": self.people,
            "description": self.description,
        }
