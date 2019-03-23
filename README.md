YT iframe Generator
================
yt_iframe is a python module which can convert a youtube video link into an embeddable iframe.
In order to use this module, install it through your terminal.

``` console
foo@bar:~$ pip install yt-iframe
```
___
``` python
# Import statement
from yt_iframe import yt
```
___
## Using the module

### yt.video()
The **video()** function takes the youtube video link as a string argument.
There are _width_ and _height_ optional arguments, so the size of the iframe can be specified.
It returns the iframe as a string.

``` python
url = 'https://www.youtube.com/watch?v=UzIQOQGKeyI' # (Required)
width = '560' # (Optional)
height = '315' # (Optional)
iframe = yt.video(url, width=width, height=height)
```
___
### yt.channel()
The **channel()** function takes a youtube channel link as a string argument.
It returns a list of youtube video links.

``` python
url = 'https://www.youtube.com/user/ouramazingspace'
videolist = yt.channel(url)
```
___
### yt.channelDict()
The **channelDict()** function takes a youtube channel link as a string argument.
It returns a nested dictionary containing the name of the channel, and video titles.

``` python
url = 'https://www.youtube.com/user/ouramazingspace'
videolist = yt.channelDict(url)

videolist['name'] # Name of channel
videolist['videos'] # Nested dictionary. Key = video title, Value = link
```
___
### yt.getFrames()
The **getFrames()** function takes a list of youtube videos as a list argument.
There are _framewidth_ and _frameheight_ optional arguments, so the size of the iframes can be specified.
It returns a list of iframes.

``` python
channel = yt.channel('https://www.youtube.com/user/ouramazingspace') # (Required)
framewidth = '560' # (Optional)
frameheight = '315' # (Optional)

iframes = yt.getFrames(channel, framewidth=framewidth, frameheight=frameheight)
```
___
## Changelog

### == v1.0.1 ==
* _Allow size of iframe to be specified in video function_
* _Allow sizes of iframes to be specified in getFrames function_

### == v1.0.0 ==
* _Initial release_
