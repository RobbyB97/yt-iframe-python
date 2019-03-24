import logging
from bs4 import BeautifulSoup as bs
import requests

class InvalidLink(Exception):
    pass


class InvalidFeed(Exception):
    pass


logger = logging.getLogger("yt_iframe")

def video(link):
    # link = youtube video url. Return iframe as string
    string = ''     # iframe string

    try:
        link = link.split('watch?v=', 1).pop()
        if not link:
            raise InvalidLink("Link not found")

        string = '<iframe width="560" height="315" src="https://www.youtube.com/embed/' + link + '" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    except Exception as e:
        raise InvalidLink('yt.video - Error! Not a valid link.') from e

    return string


def channel(link):
    # link = youtube channel url. Return iframes in list
    iframes = []       # list of iframes
    links = []      # list of video links

    try:
        # Get from channel link to RSS
        link = link.split('/channel/', 1).pop()
        if not link:
            raise InvalidLink("Link not found")

        link = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + link
    except Exception as e:
        raise InvalidLink('yt.channel - Error! Not a valid link.') from e

    try:
        # Get RSS feed
        feed = requests.get(link).text
        soup = bs(feed, "lxml")
    except Exception as e:
        raise InvalidFeed('yt.channel - Error! Could not parse xml feed.') from e

    # Add video links to links list
    for entry in soup.findAll('link'):
        if '/watch?v=' in entry['href']:
            links.append(entry['href'])

    # Convert links to iframes
    for vid in links:
        try:
            frame = video(vid)
            iframes.append(frame)
        except InvalidLink as e:
            logger.error(e)

    return iframes
