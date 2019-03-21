
from bs4 import BeautifulSoup as bs

def video(link):
    # Link = youtube video url. Return iframe as string

    try:
        link = link.split('watch?v=')[1]
        string = '<iframe width="560" height="315" src="https://www.youtube.com/embed/' + link + '" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

    except:
        print('yt_iframe - Error! Not a valid link.')
        string = ''

    return string

def channel(link):
    # https://www.youtube.com/feeds/videos.xml?channel_id= UCBcRF18a7Qf58cCRy5xuWwQ
