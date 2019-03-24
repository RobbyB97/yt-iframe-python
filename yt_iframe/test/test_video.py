from unittest import TestCase
from yt_iframe import yt


class TestVideo(TestCase):
    def setUp(self):
        self.videoUrl = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    def test_iframe(self):
        expected = '<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        iframe = yt.video(self.videoUrl)
        self.assertEqual(iframe, expected)

    def test_iframe_not_valid(self):
        with self.assertRaises(yt.InvalidLink):
            yt.video(None)

    def test_iframe_no_id(self):
        with self.assertRaises(yt.InvalidLink):
            yt.video(self.videoUrl[:32])
