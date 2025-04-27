#!/usr/bin/env -S uv run

"""
Return non-zero exit status if version specs are not aligned.
"""

import sys

# TODO: migrate to standard tomllib if requiring pythong >=3.11
import toml

from uv_copier_template import __version__ as package_version

PACKAGE_NAME = "uv-copier-template"


def get_pyproject_version():
    """
    Extract version from [project] block in pyproject.toml.
    """
    with open("pyproject.toml") as file:  # noqa: PTH123
        pyproject = toml.load(file)

    return pyproject["project"]["version"]


def get_uvlock_version():
    """
    Extract version from [project] block in uv.lock.
    """
    with open("uv.lock") as file:  # noqa: PTH123
        pyproject = toml.load(file)

    return pyproject["project"]["version"]


pyproject_version = get_pyproject_version()
uvlock_version = get_uvlock_version()

if len({package_version, pyproject_version, uvlock_version}) != 1:
    print("Unaligned versions.")
    print(f"{package_version = }")
    print(f"{pyproject_version = }")
    print(f"{uvlock_version = }")
    sys.exit(1)
