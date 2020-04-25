#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import re

from setuptools import setup, find_packages


PKG_NAME = 'bioframe'
README_PATH = 'README.md'
INSTALL_DEPS_PATH = 'requirements.txt'
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]


def _read(*parts, **kwargs):
    filepath = os.path.join(os.path.dirname(__file__), *parts)
    encoding = kwargs.pop('encoding', 'utf-8')
    with io.open(filepath, encoding=encoding) as fh:
        text = fh.read()
    return text


def get_version(pkg_name):
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        _read('{}/_version.py'.format(pkg_name)),
        re.MULTILINE).group(1)
    return version


def get_long_description(readme_path):
    return _read(readme_path)


def get_requirements(path):
    content = _read(path)
    return [
        req
        for req in content.split("\n")
        if req != '' and not req.startswith('#')
    ]


# extras_require = {
#     'docs': [
#         'Sphinx>=1.1',
#         'numpydoc>=0.5'
#     ]
# }


setup(
    name=PKG_NAME,
    author='Nezar Abdennur',
    author_email='nezar@mit.edu',
    version=get_version(PKG_NAME),
    license='MIT',
    description='Pandas utilities for tab-delimited and other genomic files',
    long_description=get_long_description(README_PATH),
    long_description_content_type="text/markdown",
    url='https://github.com/mirnylab/bioframe',
    keywords=['pandas', 'dataframe', 'genomics', 'epigenomics', 'bioinformatics'],
    packages=find_packages(),
    package_data={
        'bioframe': ['data/*']
    },
    zip_safe=False,
    classifiers=CLASSIFIERS,
    install_requires=get_requirements(INSTALL_DEPS_PATH),
    tests_require=['pytest'],
    # extras_require=extras_require,
    # entry_points={
    # }
)
