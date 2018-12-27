import unittest

from videos_processing import Video

class TestVideo(unittest.TestCase):
    def test_scenes(self):
        video = Video("two_scenes.mp4")

        self.assertEqual(len(video.scenes), 2)

        self.assertEqual(video.scenes[0].start_second, 0)
        self.assertEqual(video.scenes[0].end_second, 5)

        self.assertEqual(video.scenes[1].start_second, 11)
        self.assertEqual(video.scenes[1].end_second, 15)
