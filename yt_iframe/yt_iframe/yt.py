import logging
from bs4 import BeautifulSoup as bs
import requests
from time import sleep

# Exception handlers
class InvalidLink(Exception):
    pass

class InvalidFeed(Exception):
    pass


logger = logging.getLogger("yt_iframe")


# Global variables
css_link = 'https://raw.githubusercontent.com/RobbyB97/yt-iframe-python/master/yt_iframe/yt_iframe.css'


def channel(link):
    """Generates a list of youtube video links from a given channel.
    
    Parameters
    ----------
    link : str
        A link to a given YouTube channel.
    
    Returns
    -------
    links : list
        A list of links to youtube videos.
    """

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
    """Generates videos and metadata from a given YouTube channel.
    
    Parameters
    ----------
    link : str
        A link to a given YouTube channel.
    
    Returns
    -------
    channel : dict
        A dictionary of YouTube channel information.
        Dictionary key/value pairs:
            name = name of the YouTube channel
            videos = List of video links
    """

    links = {}       # Key = video title, Value = video link
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


def video(link, width="560", height="315"):
    """Generates a YouTube embed video iFrame from a given YouTube video link.
    
    Parameters
    ----------
    link : str
        A link to a YouTube video.
    width : str
        The width of the iFrame (in pixels).
    height : str
        The height of the iFrame (in pixels).
    
    Returns
    -------
    html : str
        The iFrame for the YouTube video.
    """

    # Ensure link is valid
    try:
        link = link.split('watch?v=')[1]
        if not link:
            raise InvalidLink("Link not found")
    except Exception as e:
        raise InvalidLink('yt.video - Error! Not a valid link.') from e
    
    # Create HTML iFrame
    html = '<iframe width="'+width+'" height="'+height+'" src="https://www.youtube.com/embed/'+link+'" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    
    return html


def getFrames(links, width="560", height="315", responsive=False):
    """Generates a list of iframes from a given list of YouTube videos.
    
    Parameters
    ----------
    links : list
        A list of links to YouTube videos.
    width : str
        The width of each iFrame (in pixels).
    height : str
        The height of each iFrame (in pixels).
    responsive : bool
        Determines whether each iframe is dynamically (true) or 
        statically (false) sized.
    
    Returns
    -------
    iframes : list
        List of iframes.
    """

    iframes = []    # List of iFrames to be returned

    for vid in links:
        # Generate iframe
        try:
            if responsive:
                frame = videoResponsive(vid, width=width, height=height)
            else:
                frame = video(vid, width=width, height=height)
            iframes.append(frame)
        except InvalidLink as e:
            logger.error(e)

    return iframes


def linkResponsive():
    """Get link to css for styling the iframes

    Returns
    -------
    str
        HTML link tag to add css for iFrames
    """
    return '<link rel="stylesheet" href="'+css_link+'">'


def videoResponsive(link, layout='onecolumn'):
    """Generates an iFrame for the repsonsive iFrame layout. It is recommended
    that you instead use the getFrames function with responsive set to true,
    instead of calling this function directly.
    
    Parameters
    ----------
    link : str
        A link to a given YouTube video.
    layout : str
        Specifies the relative size of the iFrame.
        Acceptable values:
            onecolumn - Generates one column layout
            twocolumn - Generates two column layout
    
    Returns
    -------
    iframes : list
        List of iframes.
    """

    # Set layout
    if layout == 'onecolumn':
        responsive_video = '<div class="yt-iframe-container">'
    elif layout == 'twocolumn':
        responsive_video = '<div class="yt-iframe-twocolumn">'
    else:
        log.warning('%s is not a proper layout. Defaulting to single column...' % layout)
        responsive_video = '<div class="yt-iframe-container">'

    # Get video and close tags
    yt_vid = video(link)
    responsive_video += yt_vid
    responsive_video += '</div>'

    return responsive_video
