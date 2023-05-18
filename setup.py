from setuptools import setup, find_packages

setup(
    name="apnews",
    version="0.1.0",
    description="A simple web scraper for Associated Press",
    author="Spencer Churchill",
    author_email="spence@duck.com",
    url="https://github.com/splch/py-apnews",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
    ],
)
