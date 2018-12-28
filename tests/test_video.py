import unittest

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

    def test_to_dict(self):
        expected = {
            "filename": FILENAME,
            "scenes": [
                {
                    "start_second": 0,
                    "end_second": 5,
                    "date": None,
                    "location": None,
                    "people": [],
                    "description": ""
                },
                {
                    "start_second": 11,
                    "end_second": None,
                    "date": None,
                    "location": None,
                    "people": [],
                    "description": ""
                }
            ]
        }

        self.assertEqual(VIDEO.to_dict(), expected)
