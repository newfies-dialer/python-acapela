from setuptools import setup, find_packages


def get_version():
    f = open('acapela.py')
    try:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])
    finally:
        f.close()


def get_long_description():
    descr = []
    for fname in 'README.rst', 'CHANGES.txt':   # , 'TODO.txt'
        f = open(fname)
        try:
            descr.append(f.read())
        finally:
            f.close()
    return '\n\n'.join(descr)


setup(
    name='python-acapela',
    version=get_version(),
    description="Python Acapela Text-To-Speech",
    long_description=get_long_description(),
    keywords='tts, speech, text-to-speech, acapela',
    author='Arezqui Belaid',
    author_email='areski@gmail.com',
    url='http://github.com/areski/python-acapela',
    license='MIT license',
    py_modules=['acapela'],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
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
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
