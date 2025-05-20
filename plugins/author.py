import re
import os
from docutils import nodes, utils
from docutils.parsers import rst
from docutils.parsers.rst.roles import set_classes
from pelican import signals, contents
from pelican.readers import BaseReader, RstReader
from pelican.utils import slugify
from m.htmlsanity import PelicanSaneRstReader

name_regexp = re.compile(r'[\w-]+')
author_regexp = re.compile(r':author(?:_dim)?:`([^`]+)`')

def init_plugin(pelican):
    global settings
    settings = pelican.settings

def author_to_url(author_name):
    # Check if the author name is in the list of aliases
    author_aliases = settings['AUTHOR_ALIASES']
    if author_name.lower() in author_aliases:
        # Replace the name with the alias
        author_name = author_aliases[author_name.lower()]
    
    # Replace slug by the author name
    return ("/" + settings['SITEURL'] + settings['AUTHOR_URL']).replace('{slug}', slugify(
        author_name,
        regex_subs=settings.get("SLUG_REGEX_SUBSTITUTIONS", []),
        preserve_case=settings.get("SLUGIFY_PRESERVE_CASE", False),
        use_unicode=settings.get("SLUGIFY_USE_UNICODE", False),
    ))
    
def author(name, rawtext, text, lineno, inliner, options={}, content=[]):
    url = author_to_url(text)
    node = nodes.reference(rawtext, "@" + text, refuri=url, **options)
    return [node], []

def author_dim(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.classifier(rawtext, "", classes=['m-text', 'm-dim', 'author-dim'])

    # While there is a match, extract it from the text
    while match := name_regexp.search(text):
        # Everything until the match is added as a text node
        if match.start() > 0:
            node.append(nodes.Text(text[:match.start()], **options))

        # Add the author to the article, if we're in an article
        author_name = match.group(0)
        text = text[match.end():]
        node.append(nodes.reference(rawtext, "@" + author_name, refuri=author_to_url(author_name), **options))
    if text:
        # Add the remaining text as a text node
        node.append(nodes.Text(text, **options))

    return [node], []

def infer_authors(article_generator):
    for article in article_generator.articles:
        for author in article.metadata.get('mentioned_authors', []):
            if author not in article_generator.authors:
                article_generator.authors[author] = []
            # Attribute the article to the mentioned authorz
            article_generator.authors[author].append(article)

class RawRstCapturingReader(PelicanSaneRstReader):
    def read(self, source_path):
        with open(source_path, 'r', encoding='utf-8') as f:
            raw_rst = f.read()
        content, metadata = super().read(source_path)

        for match in author_regexp.finditer(raw_rst):
            for author_name in name_regexp.findall(match.group(1)):
               # Check if the author name is in the list of aliases
                author_aliases = settings['AUTHOR_ALIASES']
                if author_name.lower() in author_aliases:
                    # Replace the name with the alias
                    author_name = author_aliases[author_name.lower()]
                
                # Add the author to the article metadata
                author = self.process_metadata("author", author_name)
                if 'mentioned_authors' not in metadata:
                    metadata['mentioned_authors'] = []
                if author not in metadata['mentioned_authors']:
                    metadata['mentioned_authors'].append(author)

        return content, metadata

def add_reader(readers):
    readers.reader_classes['rst'] = RawRstCapturingReader

def register(**kwargs):
    from pelican import signals
    signals.initialized.connect(init_plugin)
    signals.article_generator_pretaxonomy.connect(infer_authors)
    signals.readers_init.connect(add_reader)
    rst.roles.register_local_role('author', author)
    rst.roles.register_local_role('author_dim', author_dim)
