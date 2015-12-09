#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
]

test_requirements = [
    # TODO: put package test requirements here
]


setup(
    name='python-acapela',
    version='0.2.5',
    description="Python Acapela Text-To-Speech",
    long_description=readme + '\n\n' + history,
    author='Arezqui Belaid',
    author_email='areski@gmail.com',
    keywords='tts, speech, text-to-speech, acapela',
    url='http://github.com/areski/python-acapela',
    license='MIT license',
    py_modules=['acapela'],
    namespace_packages=[],
    packages=[],
    zip_safe=False,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'tts-acapela = acapela:_main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
