#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='ngozi',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='Ngozi and Adonis tie the knot',
    # GETTING-STARTED: set author name (your name):
    author='Adonis Bovell',
    # GETTING-STARTED: set author email (your email):
    author_email='adonis.ngozi@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4',
        'django-widget-tweaks==1.4.1'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/',
        'https://pypi.python.org/simple/django-widget-tweaks/'
    ],
)
