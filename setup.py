import os
import re
import setuptools


def read(fname, version=False):
    text = open(os.path.join(os.path.dirname(__file__), fname), encoding="utf8").read()
    if version:
        return re.search(r'__version__ = "(.*?)"', text).group(1)
    return text


setuptools.setup(
    name="SafoneAPI",
    packages=setuptools.find_packages(),
    version=read("SafoneAPI/version.py", version=True),
    license="MIT",
    description="Asynchronous Python Wrapper For SafoneAPI",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="AsmSafone",
    author_email="asmsafone@gmail.com",
    url="https://github.com/AsmSafone/SafoneAPI",
    keywords=["API", "SafoneAPI", "Safone_API", "Safone-API"],
    install_requires=["dotmap", "aiohttp", "aiofiles", "pyrogram"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">3.6, <3.11",
)
