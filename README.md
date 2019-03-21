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
The video() function takes the youtube video link as a string argument.
It returns the iframe as a string.
___
``` python
url = 'https://www.youtube.com/watch?v=UzIQOQGKeyI'
iframe = yt.video(url)
```
___
### yt.channel()
The channel() function takes a youtube channel link as a string argument.
It returns a list of iframe strings.
``` python
url = 'https://www.youtube.com/user/ouramazingspace'
iframelist = yt.channel(url)
```
