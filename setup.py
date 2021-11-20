"""Setup script for realpython-reader"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sfdcnotecreator",
    version="1.0.0",
    description="SFDC Note Creator Application For VSP",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/varunraghavansp/sfdcnotecreator",
    author="Varun Raghavan",
    author_email="varun.raghavan@speridian.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["sfdcnotecreator"],
    include_package_data=True,
    install_requires=["pandas", "pyodbc"],
    entry_points={"console_scripts": ["sfdcnotecreator=sfdcnotecreator.__main__:main"]},
)