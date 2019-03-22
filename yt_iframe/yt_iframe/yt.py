from bs4 import BeautifulSoup as bs
import requests
from time import sleep


def video(link):
    # link = youtube video url. Return iframe as string
    string = ''     # iframe string

    try:
        link = link.split('watch?v=')[1]
        string = '<iframe width="560" height="315" src="https://www.youtube.com/embed/' + link + '" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    except:
        print('yt.video - Error! Not a valid link.')

    return string

def channel(link):
    # link = youtube channel url. Return iframes in list
    iframes = []       # list of iframes
    links = []      # list of video links

    # Inner methods for finding RSS URL
    def userURL(link):
        user = requests.get(link).text
        soup = bs(user, 'lxml')
        link = soup.find("link", {"rel":"canonical"})
        return channel(link['href'])
    def channelURL(link):
        link = link.split('/channel/')[1]
        link = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + link
        return link

    # Get RSS URL from channel URL
    if link.split('/channel/')[1]:
        link = channelURL(link)
    elif link.split('/user/')[1]:
        link = userURL(link)
    else:

    try:
        # Get RSS feed
        feed = requests.get(link).text
        soup = bs(feed, "lxml")
    except:
        print('yt.channel - Error! Could not parse xml feed.')

    # Add video links to links list
    for entry in soup.findAll('link'):
        if '/watch?v=' in entry['href']:
            links.append(entry['href'])

    # Convert links to iframes
    for vid in links:
        frame = video(vid)
        iframes.append(frame)
    return iframes
