from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('linkedin_scraper/__init__.py').read(),
    re.M
    ).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup( 
    name = 'linkedin-scraper', 
    packages = ['linkedin-scraper'], # this must be the same as the name above 
    version = version, 
    description = 'Scrapes user data from Linkedin', 
    long_description = long_description,
    long_description_content_type='text/markdown',
    author = 'Hadeed Sarfaraz', 
    author_email = 'hadeed.sarfaraz@gmail.com', 
    url = 'https://gitlab.com/hadeedsarfaraz/linkedin_scraper', # use the URL to the github repo 
    download_url = 'https://github.com/hadeedsarfaraz/linkedin_scraper/dist/' + version + '.tar.gz', 
    keywords = ['linkedin', 'scraping', 'scraper'],
    classifiers = [], 
    install_requires=[package.split("\n")[0] for package in open("requirements.txt", "r").readlines()]
)

