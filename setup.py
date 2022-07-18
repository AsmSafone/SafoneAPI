import re
import setuptools

with open("README.md", encoding="utf8") as readme, open(
    "requirements.txt", encoding="utf8") as requirements, open(
    "version.py", encoding="utf8") as version:
    long_description = readme.read()
    requirements = requirements.read().splitlines(keepends=False)
    version = re.search(r'__version__ = "(.*?)"', version.read())[1]

setuptools.setup(
    name="SafoneAPI",
    packages=setuptools.find_packages(),
    version=version,
    license="MIT",
    description="Asynchronous Python Wrapper For SafoneAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="AsmSafone",
    author_email="asmsafone@gmail.com",
    url="https://github.com/AsmSafone/SafoneAPI",
    keywords=["API", "SafoneAPI", "Safone_API", "Safone-API"],
    install_requires=requirements,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
