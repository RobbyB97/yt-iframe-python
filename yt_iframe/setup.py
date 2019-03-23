import setuptools
from os import path

dir = path.abspath(path.dirname(__file__))

with open(path.join(dir, 'README.md'), 'r') as f:
    desc = f.read()

requirements = ['beautifulsoup4', 'lxml', 'requests']

setuptools.setup(
      name='yt_iframe',
      version='1.0.1',
      description='YouTube video iframe generator',
      long_description=desc,
      long_description_content_type='text/markdown',
      install_requires=requirements,
      url='https://github.com/RobbyB97/yt-iframe-python/tree/v1.0.1',
      author='Robby Bergers',
      author_email='bergersr@my.easternct.edu',
      license='MIT',
      packages=setuptools.find_packages(),
      zip_safe=False
)
entry_points={
    '__init__': [
        'menu = yt_iframe.yt:gen',
    ],
},
