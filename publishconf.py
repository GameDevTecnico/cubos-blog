import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://cubosengine.org'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

M_CSS_FILES = ['https://fonts.googleapis.com/css2?family=Russo+One&family=Roboto:wght@400&display=swap',
               'static/m-dark.compiled.css',
               'https://cdn.jsdelivr.net/npm/img-comparison-slider@8/dist/styles.css']
