import setuptools
from os import path

dir = path.abspath(path.dirname(__file__))

with open(path.join(dir, 'README.md'), 'r') as f:
    desc = f.read()

requirements = [
    'bs4', 'certifi', 'chardet', 
    'idna', 'requests', 'soupsieve',
    'urllib3'
]

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setuptools.setup(
      name='yt_iframe',
      version='1.0.5',
      description='YouTube video iframe generator',
      long_description=desc,
      long_description_content_type='text/markdown',
      install_requires=requirements,
      url='https://github.com/RobbyB97/yt-iframe-python',
      author='Robby Bergers',
      author_email='bergersr97@gmail.com',
      license='MIT',
      keywords='web scraper youtube iframe html generator',
      packages=setuptools.find_packages(),
      zip_safe=False
)
entry_points={
    '__init__': [
        'menu = yt_iframe.yt:gen',
    ],
},
