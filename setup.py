from setuptools import setup, find_packages

with open("README.md", "r" , encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="statuto",
    version="0.0.1",
    author="Al3jandr0 L0p3z",
    author_email="pedrolop15@hotmail.com",
    description="A package to read configuration files",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Al3jandr032/statuto",
    keywords='configuration development json xml',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        'License :: OSI Approved :: MIT License'
    ],
)