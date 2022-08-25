#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

# Package meta-data.
NAME = ""
DESCRIPTION = ""
URL = ""
EMAIL = ""
AUTHOR = ""
REQUIRES_PYTHON = ">=3.9<4.0"


# Refer https://python-poetry.org/docs/dependency-specification/
def easy_versioning(pkg_ver):
    package, ver = pkg_ver.split("=")
    package = package.strip()
    ver = ver.strip()
    min_ver = None
    max_ver = None
    # Prevent major version upgrade
    if ver[0] == "^":
        splits = ver[1:].split(".")
        new_ver = []
        for s in splits:
            if int(s) != 0:
                new_ver.append(str(int(s) + 1))
                break
            new_ver.append("0")
        if new_ver.count("0") == len(new_ver):
            new_ver[len(splits) - 1] = "1"
        while len(splits) < 3:
            splits.append("0")
        while len(new_ver) < 3:
            new_ver.append("0")
        min_ver = f"{'.'.join(splits)}"
        max_ver = f"{'.'.join(new_ver)}"
    # Prevent minor version upgrade
    elif ver[0] == "~":
        splits = ver[1:].split(".")
        if len(splits) > 1:
            max_ver = f"{splits[0]}.{int(splits[1]) + 1}.0"
        else:
            max_ver = f"{int(splits[0]) + 1}.0.0"
        while len(splits) < 3:
            splits.append("0")
        min_ver = f"{'.'.join(splits)}"
    # Allow all version after start version
    elif "*" in ver:
        splits = ver.split(".")
        if len(splits) == 1:
            return f"{package}>=0.0.0"
        if len(splits) == 2:
            if splits[1] == "*":
                min_ver = f"{splits[0]}.0.0"
                max_ver = f"{int(splits[0])+1}.0.0"
            else:
                raise ValueError(f"Invalid version string for {pkg_ver}")
        elif len(splits) == 3:
            if splits[2] == "*":
                min_ver = f"{splits[0]}.{splits[1]}.0"
                max_ver = f"{splits[0]}.{int(splits[1])+1}.0"
            else:
                raise ValueError(f"Invalid version string for {pkg_ver}")
    if min_ver is None and max_ver is None:
        return pkg_ver
    return f"{package}>={min_ver}<{max_ver}"


# What packages are required for this module to be executed?
REQUIRED = []

# What packages are optional?
EXTRAS = {
    "dev": [
        easy_versioning("twine=^4.0.1"),
        easy_versioning("pre-commit=^2.20.0"),
        easy_versioning("mypy=^0.971"),
        easy_versioning("pytest=^7.1.2"),
        easy_versioning("bandit=^1.7.4"),
        easy_versioning("safety=^2.1.1"),
    ]
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that! # noqa : E051

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Refer https://semver.org/
with open("VERSION") as f:
    VERSION = f.read()
    VERSION = VERSION.strip("\n").strip()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print(f"\033[1m{s}\033[0m")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")

        self.status("Uploading the package to PyPI")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system(f"git tag v{VERSION}")
        os.system("git push --tags")

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    # $ setup.py publish support.
    cmdclass={
        "upload": UploadCommand,
    },
)
