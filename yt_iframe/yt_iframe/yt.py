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
    links = []      # list of video links

    try:
        # Get from channel link to RSS
        link = link.split('/channel/')[1]
        link = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + link
    except:
        print('yt.channel - Error! Not a valid link.')

    try:
        # Get RSS feed
        feed = requests.get(link).text
        print(link)
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
