#!/usr/bin/env python3
"""
Convert a Blogger Atom export (feed.atom / feed_atom.xml) to markdown files.

Output structure:
  out/
    YYYY-MM-DD-slug/
      index.md
"""

import xml.etree.ElementTree as ET
import re
import os
import sys
import html
from pathlib import Path
from markdownify import markdownify

NS = {
    'atom': 'http://www.w3.org/2005/Atom',
    'blogger': 'http://schemas.google.com/blogger/2018',
}

INPUT  = Path('/mnt/user-data/uploads/feed_atom.xml')
OUTPUT = Path('/home/claude/out')


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:60].strip('-') or 'untitled'


def slug_from_filename(filename: str) -> str:
    """Extract slug from Blogger filename like /2013/05/shell-skeletons.html"""
    if filename:
        name = Path(filename).stem          # shell-skeletons
        return name or ''
    return ''


def html_to_md(raw_html: str) -> str:
    md = markdownify(raw_html, heading_style='ATX', code_language='')
    # Clean up excessive blank lines
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def process(input_path: Path, output_path: Path, include_drafts: bool = False):
    tree = ET.parse(input_path)
    root = tree.getroot()

    blog_title = root.findtext('atom:title', namespaces=NS) or 'Blog'
    print(f"Blog: {blog_title}")

    entries = root.findall('atom:entry', NS)
    posts = [
        e for e in entries
        if e.findtext('blogger:type', namespaces=NS) == 'POST'
        and (include_drafts or e.findtext('blogger:status', namespaces=NS) == 'LIVE')
        and (e.findtext('atom:title', namespaces=NS) or '').strip()
    ]

    print(f"Found {len(entries)} entries total → {len(posts)} posts to convert")
    output_path.mkdir(parents=True, exist_ok=True)

    for post in posts:
        title     = post.findtext('atom:title', namespaces=NS) or 'Untitled'
        title     = title.strip()
        published = (post.findtext('atom:published', namespaces=NS) or '')[:10]
        status    = post.findtext('blogger:status', namespaces=NS) or ''
        filename  = post.findtext('blogger:filename', namespaces=NS) or ''
        meta_desc = post.findtext('blogger:metaDescription', namespaces=NS) or ''
        content   = post.findtext('atom:content', namespaces=NS) or ''

        slug = slug_from_filename(filename) or slugify(title)
        folder_name = f"{published}-{slug}"
        folder = output_path / folder_name
        folder.mkdir(parents=True, exist_ok=True)

        md_content = html_to_md(content) if content else ''

        # YAML front matter
        frontmatter_lines = [
            '---',
            f'title: "{title.replace(chr(34), chr(39))}"',
            f'date: {published}',
            f'draft: {"true" if status == "DRAFT" else "false"}',
        ]
        if meta_desc:
            frontmatter_lines.append(f'description: "{meta_desc}"')
        frontmatter_lines.append('---')
        frontmatter = '\n'.join(frontmatter_lines)

        md_file = folder / 'index.md'
        md_file.write_text(
            f"{frontmatter}\n\n# {title}\n\n{md_content}\n",
            encoding='utf-8'
        )
        print(f"  ✓ {folder_name}/index.md")

    print(f"\nDone. Output in: {output_path}")


if __name__ == '__main__':
    include_drafts = '--drafts' in sys.argv
    process(INPUT, OUTPUT, include_drafts=include_drafts)
