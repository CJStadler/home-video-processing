class Scene:
    def from_dict(scene_data):
        return Scene(
            scene_data["start_second"],
            scene_data["end_second"],
            thumbnail_second = scene_data["thumbnail_second"],
            date = scene_data["date"],
            location = scene_data["location"],
            people = scene_data["people"],
            description = scene_data["description"]
        )

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
