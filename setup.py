#! /usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="canonicalwebteam.sitemaps-parser",
    version="1.0.1",
    author="Canonical webteam",
    author_email="webteam@canonical.com",
    url="https://github.com/canonical/canonicalwebteam.sitemaps-parser",
    description=(
        "Flask extension to parse websites and extract structured data to "
        "build sitemaps."
    ),
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "Flask>=1.0.2",
        "beautifulsoup4",
        "humanize",
        "lxml",
        "requests",
        "python-dateutil",
        "validators",
        "python-slugify",
    ],
)
