import setuptools

setuptools.setup(
      name='yt_iframe',
      version='0.1',
      description='YouTube video iframe generator',
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
