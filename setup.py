"""
Juice

Juice is a Flask based framework to help quickly develop web applications, by
adding structure to your views and templates.

Philosophy:

To create a framework that runs everywhere, regardless of the platform, by
providing cloud balh...

It made the following decisions for you: (of course you can change them)


It comes with pre-built components:


And it is still Flask.

http://pylot.io/
https://github.com/mardix/Juice

"""

import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

__about__ = {}
with open(os.path.join(base_dir, "juice", "__about__.py")) as f:
    exec(f.read(), __about__)

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name=__about__["name"],
    version=__about__["version"],
    license=__about__["license"],
    author=__about__["author"],
    author_email=__about__["email"],
    description=__about__["description"],
    url=__about__["uri"],
    long_description=__doc__,
    py_modules=['juice'],
    entry_points=dict(console_scripts=[
        'juice=juice.cli:cmd'
    ]),
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,
    keywords=['flask',
              'juice',
              'templates',
              'views',
              'classy',
              'framework',
              "mvc",
              "blueprint",
              "juice"],
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False
)
