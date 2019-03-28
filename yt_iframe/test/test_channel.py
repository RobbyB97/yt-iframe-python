from unittest import TestCase
from unittest.mock import patch, MagicMock
from yt_iframe import yt
from requests import Response
from os import path


class TestChannel(TestCase):
    def setUp(self):
        self.channelUrl = "https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw"
        basedir = path.dirname(path.realpath(__file__))
        with open(path.join(basedir, "channel_header.xml"), 'r') as header:
            self.header = header.read()
        with open(path.join(basedir, "channel_entry.xml"), 'r') as entry:
            self.entry = entry.read()
        with open(path.join(basedir, "channel_footer.xml"), 'r') as footer:
            self.footer = footer.read()



    def test_channel(self):
        expected = ['<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']

        def _get(url):
            response = MagicMock(spec=Response)
            response.text = self.header + self.entry + self.footer
            return response

        with patch('requests.get', new=_get):
            iframes = yt.channel(self.channelUrl)
            self.assertEqual(iframes, expected)

    def test_channel_invalid_url(self):
        with self.assertRaises(yt.InvalidLink):
            iframes = yt.channel(self.channelUrl[:32])

    def test_channel_invalid_feed(self):
        with patch('requests.get', side_effect=Exception()):
            with self.assertRaises(yt.InvalidFeed):
                iframes = yt.channel(self.channelUrl)

    def test_invalid_links(self):
        def _get(url):
            response = MagicMock(spec=Response)
            entry = '<entry><link rel="alternate" href="" /></entry>'
            response.text = self.header + entry + self.footer
            return response

        with patch('requests.get', new=_get):
            iframes = yt.channel(self.channelUrl)
            self.assertEqual(iframes, [])
