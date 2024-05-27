AUTHOR = 'Cubos Team'
SITENAME = 'Cubos'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

M_LINKS_NAVBAR1 = [('Docs', 'https://gamedevtecnico.github.io/cubos/docs', 'docs', [])]

M_LINKS_FOOTER1 = [('Cubos', '.'),
                   ('Getting Started', 'https://gamedevtecnico.github.io/cubos/docs/getting-started.html'),
                   ('Feature Guide', 'https://gamedevtecnico.github.io/cubos/docs/features.html'),
                   ('Examples', 'https://gamedevtecnico.github.io/cubos/docs/examples.html'),
                   ('Contribution Guidelines', 'https://gamedevtecnico.github.io/cubos/docs/contribution.html')]

M_LINKS_FOOTER2 = [('Docs', 'https://gamedevtecnico.github.io/cubos/docs'),
                   ('Pages', 'https://gamedevtecnico.github.io/cubos/docs/pages.html'),
                   ('Modules', 'https://gamedevtecnico.github.io/cubos/docs/modules.html'),
                   ('Classes', 'https://gamedevtecnico.github.io/cubos/docs/annotated.html'),
                   ('Files', 'https://gamedevtecnico.github.io/cubos/docs/files.html')]

M_LINKS_FOOTER3 = [('Contact Us', 'mailto:cubos@gamedev.tecnico.ulisboa.pt'),
                   ('Blog Feed', 'feeds/all.atom.xml'),
                   ('GitHub', 'https://github.com/GameDevTecnico/cubos'),
                   ('Discord', 'https://discord.gg/WjTtcNTRqD'),
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

M_FAVICON = ('images/favicon.png', 'image/png')
M_SITE_LOGO = 'images/favicon.png'
M_SITE_LOGO_TEXT = 'Cubos'

PLUGIN_PATHS = ['m.css/plugins']
PLUGINS = ['m.htmlsanity', 'm.code', 'm.images']
