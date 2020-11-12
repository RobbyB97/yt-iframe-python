YT iframe Generator
===================

_yt_iframe_ is a python module which can convert a youtube video link into an embeddable iframe.

---

## Getting started

In order to use this module, install it through your terminal.
``` console
foo@bar:~$ pip install yt-iframe
```

Import the module in Python.
``` python
from yt_iframe import yt
```

---

## Using the module

### yt.video()
>   Generates a YouTube embed video iFrame from a YouTube video link.

``` python
url = 'https://www.youtube.com/watch?v=UzIQOQGKeyI' # (Required)
width = '560' # (Optional)
height = '315' # (Optional)
iframe = yt.video(url, width=width, height=height)
```

**Parameters**
-   link : str _(required)_
    -   A link to a YouTube video.
-   width : str _(optional. default="560")_
    -   The width of the iFrame in pixels.
-   height : str _(optional. default="315")_
    -   The height of the iFrame in pixels.

**Returns**
- html : str
    -   The iFrame for the YouTube video.

---

### yt.channel()
>   Generates a list of YouTube video links from a YouTube channel.

``` python
url = 'https://www.youtube.com/user/ouramazingspace' # (Required)
videolist = yt.channel(url)
```

**Parameters**
-   link : str _(required)_
    -   A link to a YouTube channel.

**Returns**
-   links : list
    -   A list of links to YouTube videos.

---

### yt.channelDict()
>   Generates videos and metadata from a YouTube channel.

``` python
url = 'https://www.youtube.com/user/ouramazingspace'
videolist = yt.channelDict(url)

videolist['name'] # Name of channel
videolist['videos'] # Nested dictionary. Key = video title, Value = link
```

**Parameters**
-   link : str _(required)_
    -   A link to a YouTube channel.

**Returns**
-   channel : dict
    -   A dictionary of the YouTube channel's information.
    -   Key/value pairs:
        -   name = the name of the YouTube channel
        -   videos = List of video links

---

### yt.getFrames()
>   Generates a list of iFrames from a list of YouTube videos.

``` python
channel = yt.channel('https://www.youtube.com/user/ouramazingspace') # (Required)
width = '560' # (Optional)
height = '315' # (Optional)
responsive = True # (Optional)

# Fixed size iframes
iframes = yt.getFrames(channel, width=width, height=height)

# Responsive iframes
iframes = yt.getFrames(channel, responsive=responsive)
```

**Parameters**
-   links : list _(required)__
    -   A list of links to YouTube videos.
-   width : str _(optional. default="560")_
    -   The width of each iFrame in pixels.
-   height : str _(optional. default="315")_
    -   The height of each iFrame in pixels.
-   responsive : bool _(optional. default = False)_
    -   Determines whether each iFrame is dynamically or statically sized.

**Returns**
-   iframes : list
    -   List of iFrames.

---

### yt.linkResponsive()
>   Get link to css for styling the iFrames.
>   Alternatively, you can add this line of html in your head tag.
>   '<link rel="stylesheet" href="https://raw.githubusercontent.com/RobbyB97/yt-iframe-python/master/yt_iframe/yt_iframe.css">'

**Returns**
-   str
    -   HTML link tag to import css for iFrames

---

### yt.videoResponsive()
>   Generates a responsive iFrame video. Make sure you have the css file imported with the linkResponsive() function. You can wrap a bunch of these generated tags in a container and the iFrames will resize to fit the layout within that container.

``` python
url = 'https://www.youtube.com/watch?v=UzIQOQGKeyI' # (Required)
layout = 'singlecolumn' # (Optional)

video = yt.videoResponsive(url, layout=layout) # Get HTML
```

**Parameters**
-   link : str _(required)_
    -   A link to a YouTube video.
-   layout : str _(optional. default="onecolumn")_
    -   Soecifies the relative size of the iFrame.
    -   Acceptable values:
        -   'onecolumn' - Generates one column layout
        -   'twocolumn' - Generates two column video

**Returns**
-   iframes : list
    -   List of iFrames.

---

## Changelog

### == v1.0.5 ==
* _Fix css import link_
* _Fix argument error in videoResponsive()_
* _Fix xml parsing (the lxml dependency issue)_
* _Add docstrings for all functions_
* _Refactor functions to improve readability_

### == v1.0.4 ==
* _Add layout argument to videoResponsive() and getFrames()_
* _Add two column layout option to videoResponsive()_

### == v1.0.3 ==
* _Add responsive iframes_
* _getFrames() arguments changed from framewidth and frameheight to width and height_

### == v1.0.1 ==
* _Allow size of iframe to be specified in video() function_
* _Allow sizes of iframes to be specified in getFrames() function_

### == v1.0.0 ==
* _Initial release_
