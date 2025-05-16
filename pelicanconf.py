AUTHOR = 'Cubos Team'
SITENAME = 'Cubos Engine'
SITEURL = ''

M_BLOG_NAME = 'Cubos Blog'
M_BLOG_URL = "/blog"
M_BLOG_DESCRIPTION = "Cubos is an open-source student-developed game engine built in modern C++ where everything is made of voxels."

M_SOCIAL_IMAGE = 'https://cubosengine.org/images/social.png'
M_SOCIAL_BLOG_SUMMARY = "An open-source student-developed game engine built in modern C++ where everything is made of voxels."

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

PATH = 'content'

ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'blog/'
ARCHIVES_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{slug}/' # category/ is part of the slug
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
DRAFT_URL = 'blog/{slug}/' # so the URL is the final one
DRAFT_SAVE_AS = 'blog/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = 'blog/author/{slug}/index.html'
CATEGORY_URL = 'blog/{slug}/'
CATEGORY_SAVE_AS = 'blog/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

M_LINKS_NAVBAR1 = [('Docs', 'https://docs.cubosengine.org', 'docs', [])]

M_LINKS_NAVBAR2 = [('Blog', M_BLOG_URL, '[blog]', []),
                   ('GitHub', 'https://github.com/GameDevTecnico/cubos', '', [])]

M_LINKS_FOOTER1 = [('Cubos', '.'),
                   ('Getting Started', 'https://docs.cubosengine.org/getting-started.html'),
                   ('Feature Guide', 'https://docs.cubosengine.org/features.html'),
                   ('Examples', 'https://docs.cubosengine.org/examples.html'),
                   ('Contribution Guidelines', 'https://docs.cubosengine.org/contribution.html'),
                   ('Brand Guidelines', '/images/brand.pdf')]

M_LINKS_FOOTER2 = [('Docs', 'https://docs.cubosengine.org'),
                   ('Pages', 'https://docs.cubosengine.org/pages.html'),
                   ('Modules', 'https://docs.cubosengine.org/modules.html'),
                   ('Classes', 'https://docs.cubosengine.org/annotated.html'),
                   ('Files', 'https://docs.cubosengine.org/files.html')]

M_LINKS_FOOTER3 = [('Contact Us', 'mailto:team@cubosengine.org'),
                   ('Blog Feed', 'feeds/all.atom.xml'),
                   ('GitHub', 'https://github.com/GameDevTecnico/cubos'),
                   ('Discord', 'https://discord.gg/WjTtcNTRqD'),
                   ('E-mail', 'mailto:team@cubosengine.org'),
                   ('itch.io', 'https://cubos-engine.itch.io/')]

M_SHOW_AUTHOR_LIST = True

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index', 'archives']

M_CSS_FILES = ['https://fonts.googleapis.com/css2?family=Russo+One&family=Roboto:wght@400&display=swap',
               'static/m-dark.css',
               'https://cdn.jsdelivr.net/npm/img-comparison-slider@8/dist/styles.css']
M_JS_FILES = ['https://cdn.jsdelivr.net/npm/img-comparison-slider@8/dist/index.js']
M_THEME_COLOR = '#22272e'

M_FAVICON = ('images/favicon.png', 'image/png')
M_SITE_LOGO = 'images/favicon.png'
M_SITE_LOGO_TEXT = 'Cubos'

PLUGIN_PATHS = ['m.css/plugins']
PLUGINS = ['m.htmlsanity', 'm.code', 'm.images', 'm.math', 'm.components', 'm.metadata']

FORMATTED_FIELDS = ['summary', 'landing', 'more_content', 'description', 'badge']

M_NEWS_ON_INDEX = ("Latest news", "More news", 3)
