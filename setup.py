from setuptools import setup, find_packages

# with open("README.md") as f:
#     readme = f.read()

# with open("LICENSE") as f:
#     license = f.read()

setup(
    name="ldiff",
    version="0.1.0",
    description="Tool for diffing multi-file tex documents.",
    # long_description=readme,
    author="Timm Behner",
    author_email="behner@cs.uni-bonn.de",
    url="https://github.com/tbehner/ldiff",
    # license=license,
    install_requires=[
        "click",
        ],
    packages=find_packages(exclude=("tests", "docs")),
    entry_points = {
        "console_scripts": [
            "ldiff=ldiff.cli:main",
        ]
    }
)

