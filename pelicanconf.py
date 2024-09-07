AUTHOR = 'Cubos Team'
SITENAME = 'Cubos'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

M_LINKS_NAVBAR1 = [('Docs', 'https://docs.cubosengine.org', 'docs', [])]

M_LINKS_FOOTER1 = [('Cubos', '.'),
                   ('Getting Started', 'https://docs.cubosengine.org/getting-started.html'),
                   ('Feature Guide', 'https://docs.cubosengine.org/features.html'),
                   ('Examples', 'https://docs.cubosengine.org/examples.html'),
                   ('Contribution Guidelines', 'https://docs.cubosengine.org/contribution.html')]

M_LINKS_FOOTER2 = [('Docs', 'https://docs.cubosengine.org'),
                   ('Pages', 'https://docs.cubosengine.org/pages.html'),
                   ('Modules', 'https://docs.cubosengine.org/modules.html'),
                   ('Classes', 'https://docs.cubosengine.org/annotated.html'),
                   ('Files', 'https://docs.cubosengine.org/files.html')]

M_LINKS_FOOTER3 = [('Contact Us', 'mailto:team@cubosengine.org'),
                   ('Blog Feed', 'feeds/all.atom.xml'),
                   ('GitHub', 'https://github.com/GameDevTecnico/cubos'),
                   ('Discord', 'https://discord.gg/WjTtcNTRqD'),
                   ('E-mail', 'mailto:team@cubosengine.org')]

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               'static/m-dark.css']
M_THEME_COLOR = '#22272e'

M_FAVICON = ('images/favicon.png', 'image/png')
M_SITE_LOGO = 'images/favicon.png'
M_SITE_LOGO_TEXT = 'Cubos'

PLUGIN_PATHS = ['m.css/plugins']
PLUGINS = ['m.htmlsanity', 'm.code', 'm.images', 'm.math']
