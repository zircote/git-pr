# -*- coding: utf-8 -*-
from __future__ import absolute_import
from setuptools import setup, find_packages
requirements = []

with open('requirements.txt') as req_file:
    for req in req_file.readlines():
        requirements.append(req.strip())

setup(
    name='git-pr',
    version='0.0.1',
    packages=['git_pr'],
    package_dir={'': 'src/python'},
    url='https://github.com/zircote/git-pr',
    license='APACHE-2.0',
    author='Robert Allen',
    author_email='zircote@gmail.com',
    description='A tool for cli opening of the github pull requests for a given project',
    entry_points={
        'console_scripts': ['git-pr=git_pr:main'],
    },
    setup_requires=requirements,
    install_requires=requirements,
    long_description=open('readme.md').read(),
)
