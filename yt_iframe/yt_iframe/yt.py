import logging
from bs4 import BeautifulSoup as bs
import requests
from time import sleep

class InvalidLink(Exception):
    pass


class InvalidFeed(Exception):
    pass


logger = logging.getLogger("yt_iframe")


""" YT channel functions """

def channel(link):
    # link = youtube channel url. Return iframes in list
    iframes = []       # list of iframes
    links = []      # list of video links

    # Inner methods for finding RSS URL
    def userURL(link):
        user = requests.get(link).text
        soup = bs(user, 'lxml')
        link = soup.find("link", {"rel":"canonical"})
        return channelURL(link['href'])
    def channelURL(link):
        try:
            link = link.split('/channel/')[1]
            if not link:
                raise InvalidLink("Link not found")

            link = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + link
        except Exception as e:
            raise InvalidLink('yt.channel - Error! Not a valid link.') from e
        return link

    # Get RSS URL from channel URL
    if '/channel/' in link:
        xml = channelURL(link)
    elif '/user/' in link:
        xml = userURL(link)
    else:
        print('yt.channel - Error! Not a valid link')

    try:
        # Get RSS feed
        feed = requests.get(xml).text
        xmlsoup = bs(feed, "lxml")
    except Exception as e:
        raise InvalidFeed('yt.channel - Error! Could not parse xml feed.') from e

    # Add video links to links list
    for entry in xmlsoup.findAll('link'):
        if '/watch?v=' in entry['href']:
            links.append(entry['href'])
    return links


def channelDict(link):
    # Alternate version of channel() that returns a dictionary

    links = {}          # Key = video title, Value = video link
    channel = {}     # Master dictionary

    # Get link to RSS feed
    def userURL(link):
        user = requests.get(link).text
        soup = bs(user, 'lxml')
        link = soup.find("link", {"rel":"canonical"})
        return channelURL(link['href'])
    def channelURL(link):
        link = link.split('/channel/')[1]
        link = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + link
        return link

    # Get RSS URL from channel URL
    if '/channel/' in link:
        xml = channelURL(link)
    elif '/user/' in link:
        xml = userURL(link)
    else:
        print('yt.channel - Error! Not a valid link')

    # Get RSS feed
    feed = requests.get(xml).text
    xmlsoup = bs(feed, "lxml")

    # Get name of channel
    channel['name'] = xmlsoup.find('author').find('name').text

    # Create video dictionary entries
    for entry in xmlsoup.findAll('entry'):
        ytlink = entry.find('link')
        if '/watch?v=' in ytlink['href']:
            title = entry.find('title').text
            ytlink = ytlink['href']
            links[title] = ytlink
        else:
            continue

    channel['videos'] = links
    return channel


""" iFrame functions """

def video(link, width="560", height="315"):
    # link = youtube video url. Return iframe as string
    # width, height = size of iframe
    string = ''     # iframe string

    try:
        link = link.split('watch?v=')[1]
        if not link:
            raise InvalidLink("Link not found")
        string = '<iframe width="'+width+'" height="'+height+'" src="https://www.youtube.com/embed/'+link+'" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    except Exception as e:
        raise InvalidLink('yt.video - Error! Not a valid link.') from e
    return string

def getFrames(links, width="560", height="315", responsive=False):
    # Convert links list to iframes list
    iframes = []

    for vid in links:
        try:

            # Get responsive or statically sized iframe
            if responsive:
                frame = videoResponsive(vid, width=width, height=height)
            else:
                frame = video(vid, width=width, height=height)
            iframes.append(frame)
        except InvalidLink as e:
            logger.error(e)
    return iframes


""" Responsive iFrame functions """

def linkResponsive():
    # Return html link to css stylesheet
    return '<link rel="stylesheet" href="https://bergers.rocks/packages/yt_iframe.css">'

def videoResponsive(link, width="560", height="315"):
    # Return html for responsive yt video iframe

    responsive_video = '<div class="yt-iframe-container">'
    yt_vid = video(link, width=width, height=height)
    responsive_video += yt_vid
    responsive_video += '</div>'

    return responsive_video
