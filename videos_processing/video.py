import av

class Video:
    def __init__(self, filename):
        self.filename = filename
        self.scenes = _load_scenes(filename)

    def _load_scenes(filename):
        """
        Return a Video representing the given file.

        filename: the path to the video file to process.
        """
        container = av.open(filename)

        scenes = []
        current_scene_start = 0
        previous_is_blank = True

        for frame in container.decode(video=0):
            blank = _is_blank(frame)

            if blank and not previous_is_blank:
                # End scene
                scenes.append(Scene(current_scene_start, frame.time))
            elif not blank and previous_is_blank:
                # Start a new scene
                current_scene_start = frame.time

            previous_is_blank = blank

        return

    def _is_blank(frame):
        return False
