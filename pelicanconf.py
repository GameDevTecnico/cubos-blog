AUTHOR = 'CUBOS. Team'
SITENAME = 'CUBOS.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

M_LINKS_NAVBAR1 = [('Docs', 'https://gamedevtecnico.github.io/cubos', 'docs', [])]

M_LINKS_FOOTER1 = [('Cubos', '.'),
                   ('Getting Started', 'https://gamedevtecnico.github.io/cubos/getting-started.html'),
                   ('Feature Guide', 'https://gamedevtecnico.github.io/cubos/features.html'),
                   ('Examples', 'https://gamedevtecnico.github.io/cubos/examples.html'),
                   ('Contribution Guidelines', 'https://gamedevtecnico.github.io/cubos/contribution.html')]

M_LINKS_FOOTER2 = [('Docs', 'https://gamedevtecnico.github.io/cubos'),
                   ('Pages', 'https://gamedevtecnico.github.io/cubos/pages.html'),
                   ('Modules', 'https://gamedevtecnico.github.io/cubos/modules.html'),
                   ('Classes', 'https://gamedevtecnico.github.io/cubos/annotated.html'),
                   ('Files', 'https://gamedevtecnico.github.io/cubos/files.html')]

M_LINKS_FOOTER3 = [('Contact Us', 'mailto:cubos@gamedev.tecnico.ulisboa.pt'),
                   ('Blog Feed', 'feeds/all.atom.xml'),
                   ('GitHub', 'https://github.com/GameDevTecnico/cubos'),
                   ('E-mail', 'mailto:cubos@gamedev.tecnico.ulisboa.pt')]

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

PLUGIN_PATHS = ['m.css/plugins']
PLUGINS = ['m.htmlsanity']
