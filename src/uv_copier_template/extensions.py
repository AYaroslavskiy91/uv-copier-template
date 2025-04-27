"""
Custom extensions made for this template.
"""

import re
import subprocess
import unicodedata
from typing import Any, Self

from copier_templates_extensions import ContextHook
from jinja2.environment import Environment
from jinja2.ext import Extension
from packaging.version import Version as PkgVersion


def git_user_name(default: str = "") -> str:
    """
    Retrieve the Git user name from the local configuration, or return a default.

    Parameters
    ----------
    default : str
        The value to return if no Git user name is found.

    Returns
    -------
    str
        The Git user name, or the default.
    """
    return (
        subprocess.run(  # noqa: S603
            ["git", "config", "user.name"],  # noqa: S607
            capture_output=True,
            check=True,
            text=True,
        ).stdout.strip()
        or default
    )


def git_user_email(default: str = "") -> str:
    """
    Retrieve the Git user email from the local configuration, or return a default.

    Parameters
    ----------
    default : str
        The default email to return if no Git user email is configured.

    Returns
    -------
    str
        The Git user email if configured, otherwise the default email.
    """
    return (
        subprocess.run(  # noqa: S603
            ["git", "config", "user.email"],  # noqa: S607
            capture_output=True,
            check=True,
            text=True,
        ).stdout.strip()
        or default
    )


class GitExtension(Extension):
    """
    Extension that adds Git configuration filters to the environment.

    Parameters
    ----------
    environment
        Jinja environment.

    Notes
    -----
    Adapted from:
    https://github.com/pawamoy/copier-pdm/blob/82233b6824c67557a5e753270e190b95a8e390d1/extensions.py#L23-L27
    Copyright (c) 2019, Timothée Mazzucotelli
    Distributed under the terms of the ISC license.
    """

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email


def slugify(value: str, separator: str = "-"):
    """
    Slugify a string with a given separator.

    Parameters
    ----------
    value
        The string to slugify.
    separator
        The string to use as a separator. Defaults to "-".

    Returns
    -------
    str
        The slugified string.

    Notes
    -----
    Adapted from:
    https://github.com/pawamoy/copier-pdm/blob/82233b6824c67557a5e753270e190b95a8e390d1/extensions.py#L17-L20
    Copyright (c) 2019, Timothée Mazzucotelli
    Distributed under the terms of the ISC license.
    """
    value = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-_\s]+", separator, value).strip("-_")


class SlugifyExtension(Extension):
    """
    Extension that adds string slugification filters to the environment.

    Parameters
    ----------
    environment
        Jinja environment.

    Notes
    -----
    Borrowed from:
    https://github.com/pawamoy/copier-pdm/blob/82233b6824c67557a5e753270e190b95a8e390d1/extensions.py#L30-L33
    Copyright (c) 2019, Timothée Mazzucotelli
    Distributed under the terms of the ISC license.
    """

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["slugify"] = slugify


class Version(PkgVersion):
    """
    Comparison aware version identifier abstraction.

    Parameters
    ----------
    version
        The string representation of a version which will be parsed and normalized
        before use.

    Raises
    ------
    InvalidVersion
        If the ``version`` does not conform to PEP 440 in any way then this
        exception will be raised.
    """

    def next_major_version(self: Self) -> Self:
        """
        Get a new instance of ``Version`` that represents the next major version.

        Returns
        -------
        Version
        """
        return type(self)(f"{self.major + 1}.0")

    def next_minor_version(self: Self) -> Self:
        """
        Get a new instance of ``Version`` that represents the next minor version.

        Returns
        -------
        Version
        """
        return type(self)(f"{self.major}.{self.minor + 1}")


# https://devguide.python.org/versions/#supported-versions
CURRENT_FEATURE_PYTHON_VERSION = Version("3.14")
# "Stable" extends the "bugfix"-only definition to include "security" versions
STABLE_PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12", "3.13"]


def parse_version(version: str) -> Version:
    """
    Parse the given data as a version identifier.

    Parameters
    ----------
    version
        Version string to parse.

    Returns
    -------
    Version

    Raises
    ------
    InvalidVersion
        When the version string is not a valid version.
    """
    return Version(version)


def to_pyver_tag(version: str | Version) -> str:
    """
    Parse a `"{major}.{minor}"` version identifier & output `"py{major}{minor}"`.

    Parameters
    ----------
    version
        `"{major}.{minor}"` version identifier

    Returns
    -------
    `"py{major}{minor}"` version identifier
    """
    if isinstance(version, Version):
        version = str(version)
    return f"py{version.replace('.', '')}"


def version_btw(ver: str, min_ver: str, max_ver: str) -> bool:
    """
    Return whether a `"{major}.{minor}"` version identifier is between two others.

    Parameters
    ----------
    ver
        `"{major}.{minor}"` version identifier to test.
    min_ver
        Lower bound [inclusive] `"{major}.{minor}"` version identifier.
    max_ver
        Upper bound [inclusive] `"{major}.{minor}"` version identifier.

    Returns
    -------
    bool

    Raises
    ------
    ValueError
        If `min_ver` > `max_ver`.
    """
    parsed_ver = parse_version(ver)
    parsed_min = parse_version(min_ver)
    parsed_max = parse_version(max_ver)
    if parsed_min > parsed_max:
        msg = f"`min_ver` ({min_ver!r}) must be <= `max_ver` ({max_ver!r})"
        raise ValueError(msg)
    return parsed_min <= parsed_ver <= parsed_max


def version_lt(lhs: str, rhs: str) -> bool:
    """
    Return whether a `"{major}.{minor}"` version identifier is less than another.

    Parameters
    ----------
    lhs
        `"{major}.{minor}"` version identifier to test.
    rhs
        `"{major}.{minor}"` version identifier to test ``lhs`` against.

    Returns
    -------
    bool
    """
    return parse_version(lhs) < parse_version(rhs)


class PythonVersionExtension(Extension):
    """
    Extension that adds version-related globals, filters, & tests to the Jinja environment.

    Parameters
    ----------
    environment
        Jinja environment.
    """

    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)
        environment.globals["stable_python_versions"] = STABLE_PYTHON_VERSIONS
        environment.globals["all_python_versions"] = [
            *STABLE_PYTHON_VERSIONS,
            str(CURRENT_FEATURE_PYTHON_VERSION),
            str(CURRENT_FEATURE_PYTHON_VERSION.next_major_version()),
        ]
        environment.filters["to_pyver_tag"] = to_pyver_tag
        environment.filters["versionize"] = Version
        environment.tests["version_lt"] = version_lt


class ContextUpdater(ContextHook):
    """
    In-place updater of the Jinja Context.

    Notes
    -----
    https://copier.readthedocs.io/en/stable/faq/#how-can-i-alter-the-context-before-rendering-the-project
    """

    update = False

    # FIXME(RR): Copier 9.4 introduces a change that causes hook to be called with
    #   a context that contains none of the answers provided either by data or
    #   defaults. As a workaround, all `__getitem__` are changed to `.get` with
    #   validly typed default values.
    # FIXME(RR): fn below returns None but mypy sticks to Copier Templates Extension's
    #   incomplete signature (which should have an @overload).
    #   basedpyright is just fine with returning None.
    def hook(self, context: dict[str, Any]) -> Any:
        """
        Update the Jinja Context in-place.

        Parameters
        ----------
        context
            The Context to modify in-place (meaning it contains the current context).

        Returns
        -------
        None
            The current return type hint of ``Any`` above is there to satisfy mypy,
            which hues literally to Copier Templates Extensions'.
        """
        context["minimum_python_version"] = str(
            parse_version(
                context.get("minimum_python_version", STABLE_PYTHON_VERSIONS[0])
            )
        )
        context["python_versions"] = [
            v
            for v in STABLE_PYTHON_VERSIONS
            if version_btw(
                v,
                context.get("minimum_python_version", STABLE_PYTHON_VERSIONS[0]),
                context.get("maximum_python_version", STABLE_PYTHON_VERSIONS[-1]),
            )
        ]
        context["repository_url"] = "https://" + "/".join(
            [
                context.get("repository_provider", ""),
                context.get("repository_namespace", ""),
                context.get("repository_name", ""),
            ]
        )
