import setuptools
from os import path

dir = path.abspath(path.dirname(__file__))

with open('README.md', 'r') as f:
    desc = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setuptools.setup(
      name='yt_iframe',
      version='0.3',
      description='YouTube video iframe generator',
      long_description=desc,
      long_description_content_type='text/markdown',
      install_requires=requirements,
      url='https://github.com/RobbyB97/yt-iframe-python/tree/v0.3',
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
