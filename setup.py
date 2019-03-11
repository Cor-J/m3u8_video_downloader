#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Synsis(https://github.com/synsis). All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.

from setuptools import setup, find_packages

setup(
    name='m3u8_video_downloader',
    version=1.1,
    description=(
        'Download video from m3u8 url'
    ),
    # long_description=open('README.rst').read(),
    author='Synsis',
    author_email='synsis@outlook.com',

    license='MIT',
    key_words='m3u8 video download',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/synsis/m3u8_video_downloader',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3',
    install_requires=[
        'requests',
        'fire'
    ],
)
