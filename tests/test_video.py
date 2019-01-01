import unittest
import math

from videos_processing import Video

FILENAME = "tests/two_scenes.mp4"
VIDEO = Video(FILENAME)

class TestVideo(unittest.TestCase):
    def test_load_scenes(self):
        self.assertEqual(len(VIDEO.scenes), 2)

        scene1, scene2 = VIDEO.scenes
        self.assertEqual(scene1.start_second, 0)
        self.assertEqual(scene1.end_second, 5)

        self.assertEqual(scene2.start_second, 11)
        self.assertEqual(scene2.end_second, None)

    def test_thumbnail_frames(self):
        times = [3, 13]
        data = self._base_dict()

        for i, t in enumerate(times):
            data["scenes"][i]["thumbnail_second"] = t

        video = Video.from_dict(data)
        frames = video.thumbnail_frames()

        self.assertEqual([math.floor(f.time) for f in frames], times)

    def test_to_dict(self):
        self.assertEqual(VIDEO.to_dict(), self._base_dict())

    def test_from_dict(self):
        self.assertEqual(Video.from_dict(self._base_dict()).to_dict(), self._base_dict())

    def _base_dict(self):
        return {
            "filename": FILENAME,
            "scenes": [
                {
                    "start_second": 0,
                    "end_second": 5,
                    "thumbnail_second": None,
                    "date": None,
                    "location": None,
                    "people": [],
                    "description": ""
                },
                {
                    "start_second": 11,
                    "end_second": None,
                    "thumbnail_second": None,
                    "date": None,
                    "location": None,
                    "people": [],
                    "description": ""
                }
            ]
        }
