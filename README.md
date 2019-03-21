YT iFrame Generator
================
yt_iframe is a python module which can convert a youtube video link into an embeddable iframe.
In order to use this module, install it through your terminal.

``` console
foo@bar:~$ pip install yt_iframe
```

``` python
# Import statement
from yt_iframe import yt
```
___
### Using the module
The gen() function takes the youtube video link as a string argument. It returns the iframe as a string.
``` python
url = 'https://www.youtube.com/watch?v=UzIQOQGKeyI'
iframe = yt.gen(url)
```
