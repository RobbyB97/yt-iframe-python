from bs4 import BeautifulSoup as bs
import requests


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

    try:
        # Get from channel link to RSS
        link = link.split('/channel/')[1]
        link = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + link
    except:
        print('yt.channel - Error! Not a valid link.')

    try:
        # Get RSS feed
        feed = requests.get(link)

    return iframes
