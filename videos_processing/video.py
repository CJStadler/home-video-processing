import av
import numpy
import math
from pathlib import Path

from .scene import Scene

GRAY = 75 # RGB Value
TOLERANCE = 10 # Allowable distance from GRAY

class Video:
    def from_dict(video_data):
        scenes = [Scene.from_dict(s) for s in video_data["scenes"]]
        return Video(video_data["filename"], scenes=scenes)

    def __init__(self, filename, scenes=None):
        if scenes:
            self.scenes = scenes
        else:
            self.scenes = load_scenes(filename)

        self.filename = filename

    def display_name(self):
        return self.name().replace('_', ' ')

    def name(self):
        return Path(self.filename).stem

    def to_dict(self):
        return {
            "filename": self.filename,
            "scenes": [s.to_dict() for s in self.scenes]
        }

    def thumbnail_frames(self):
        container = av.open(self.filename)
        frame_generator = container.decode(video=0)

        thumbnail_times = sorted([s.thumbnail_second for s in self.scenes if s.thumbnail_second])
        thumbnail_frames = []

        current_frame = next(frame_generator)

        for second in thumbnail_times:
            while current_frame.time < second:
                current_frame = next(frame_generator)

            thumbnail_frames.append(current_frame)

        return thumbnail_frames


def load_scenes(filename):
    container = av.open(filename)

    scenes = []
    current_scene_start = 0
    previous_is_blank = True

    for frame in container.decode(video=0):
        blank = is_blank(frame)

        if blank and not previous_is_blank:
            # End scene
            scenes.append(Scene(current_scene_start, math.ceil(frame.time)))
        elif not blank and previous_is_blank:
            # Start a new scene
            current_scene_start = max(math.floor(frame.time) - 1, 0)

        previous_is_blank = blank
        previous_frame = frame

    # If the video ended on a non-blank frame then add the last scene
    if not previous_is_blank:
        scenes.append(Scene(current_scene_start, None))

    return scenes

def is_blank(frame):
    pixels = frame.to_rgb().to_ndarray().astype(numpy.int8)
    # uint8 -> int8 to prevent overflow.

    return (numpy.absolute(pixels - GRAY) < TOLERANCE).all()
