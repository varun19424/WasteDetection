from setuptools import setup, find_packages

setup(
    name = 'WasteDetection',
    version = '1.0',
    author = 'Varun',
    author_email = 'varun19424@gmail.com',
    packages=find_packages(include=['WasteDetection', 'WasteDetection.*']),
    install_requires = []
)