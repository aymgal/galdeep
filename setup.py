#!/usr/bin/env python

import os
import sys
from setuptools.command.test import test as TestCommand
from setuptools import find_packages
from setuptools.command.build_ext import build_ext as _build_ext

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


#readme = open('README.md').read()

#history = open('HISTORY.md').read().replace('.. :changelog:', '')

desc = open("README.md").read()
requires = ['configparser']
tests_require=['pytest>=2.3', 'mock']

PACKAGE_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


setup(
    name='galdeep',
    version='0.0.1',
    description='Regularizazion through deep neural network',
    long_description=desc,
    author='Aymeric Galan',
    author_email='aymeric.galan@gmail.com',
    url='https://github.com/aymgal/galdeep',
    download_url='https://github.com/aymgal/galdeep/archive/0.0.1.tar.gz.zip',
    packages=find_packages(PACKAGE_PATH, "test"),
    package_dir={'galdeep': 'galdeep'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    keywords='galdeep',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    tests_require=tests_require,
    python_requires='>=3.6',
    cmdclass={'test': PyTest},
)
