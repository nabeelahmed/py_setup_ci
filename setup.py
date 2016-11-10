import os
from setuptools import setup, find_packages
# PACKAGES = find_packages()
PACKAGES = ['py_setup_ci', 'py_setup_ci/tests']

# Get version and release info, which is all stored in shablona/version.py
ver_file = os.path.join('shablona', 'version.py')
with open(ver_file) as f:
    exec(f.read())

opts = dict(name="py_setup_ci",
            description="Python packaging and CI test",
            author="Nabeel",
            version="0.1.0",
            packages=PACKAGES,
            requires=['pyrabbit==1.1.0'])


if __name__ == '__main__':
    setup(**opts)
