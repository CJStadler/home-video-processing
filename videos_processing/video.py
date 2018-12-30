import av
import numpy
import math
from pathlib import Path

from .scene import Scene

GRAY = 75 # RGB Value
TOLERANCE = 10 # Allowable distance from GRAY

class Video:
    def __init__(self, filename):
        self.scenes = load_scenes(filename)
        self.filename = Path(filename).name

    def to_dict(self):
        return {
            "filename": self.filename,
            "scenes": [s.to_dict() for s in self.scenes]
        }

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
