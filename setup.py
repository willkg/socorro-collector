#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from setuptools import setup


def get_file(fn):
    with open(fn) as fp:
        return fp.read()


# FIXME: This requires the requirements in requirements.txt, but we need to
# pull that in without the hashes.

setup(
    name='collector',
    version='0.1.0',
    description='Prototype Socorro breakpd collector',
    long_description=get_file('README.rst'),
    author='Mozilla',
    author_email='socorro-dev@mozilla.com',
    url='https://github.com/mozilla/socorro-collector',
    packages=[
        'collector',
    ],
    package_dir={
        'collector': 'collector'
    },
    entry_points={
        'console_scripts': [
            'socorro=collector.app.socorro_app:SocorroWelcomeApp.run'
        ],
    },
    include_package_data=True,
    license="MPLv2",
    zip_safe=False,
    keywords='breakpad crash',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
)
