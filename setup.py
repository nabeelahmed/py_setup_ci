import os
from setuptools import setup, find_packages
# PACKAGES = find_packages()
PACKAGES = ['py_setup_ci', 'tests']


opts = dict(name="py_setup_ci",
            description="Python packaging and CI test",
            author="Nabeel",
            version="0.1.0_dev",
            packages=PACKAGES,
            requires=['pyrabbit'])


if __name__ == '__main__':
    setup(**opts)
