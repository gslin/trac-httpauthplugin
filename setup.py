#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name='TracHTTPAuth',
    version='1.3',
    packages=['httpauth'],
    #package_data = { 'httpauth': ['templates/*.cs', 'htdocs/*.js', 'htdocs/*.css' ] },

    author="Noah Kantrowitz",
    author_email="noah@coderanger.net",
    maintainer="Craig A",
    maintainer_email="craiga@fonefit.com",
    description="Use the AccountManager plugin to provide HTTP authentication from Trac itself.",
    license="BSD",
    keywords="trac plugin http auth",
    url="http://trac-hacks.org/wiki/HttpAuthPlugin",
    classifiers=[
        'Framework :: Trac',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],

    install_requires=['TracAccountManager'],

    entry_points={
        'trac.plugins': [
            'httpauth.filter = httpauth.filter',
        ]
    }
)
