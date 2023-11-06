import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://gamedevtecnico.github.io/cubos'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               'static/m-dark.compiled.css']
