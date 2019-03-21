import setuptools
from os import path

dir = path.abspath(path.dirname(__file__))

with open(path.join(dir, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

with open(path.join(dir, 'requirements.txt'), 'r') as f:
    requirements = f.read().splitlines()

setuptools.setup(
      name='yt_iframe',
      version='0.2',
      description='YouTube video iframe generator',
      long_description=desc,
      long_description_content_type='text/markdown',
      install_requires=requirements,
      url='http://github.com/robbyb97/yt-iframe-python',
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
