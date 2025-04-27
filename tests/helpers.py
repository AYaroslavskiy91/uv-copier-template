import os
import re
import textwrap
from collections.abc import Mapping, Sequence
from pathlib import Path

from copier.types import StrOrPath
from plumbum.cmd import git


def build_file_tree(
    spec: Mapping[StrOrPath, str | bytes | Path], *, dedent: bool = True
) -> None:
    """
    Build a file tree based on the received spec.

    Parameters
    ----------
    spec
        A mapping from filesystem paths to file contents. If the content is
        a `Path` object a symlink to the path will be created instead.
    dedent
        Dedent file contents.

    Notes
    -----
    Adapted from:
    https://github.com/copier-org/copier/blob/70aa69f7df430a611a20f940b47174da96b88dfa/tests/helpers.py#L98-L122
    Copyright (c) 2011 Juan-Pablo Scaletti
    Distributed under the terms of the MIT license.
    """
    for path, contents in spec.items():
        path = Path(path)  # noqa: PLW2901
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(contents, Path):
            os.symlink(str(contents), path)
        else:
            binary = isinstance(contents, bytes)
            if not binary and dedent:
                assert isinstance(contents, str)
                contents = textwrap.dedent(contents)  # noqa: PLW2901
            mode = "wb" if binary else "w"
            with path.open(mode) as fd:
                fd.write(contents)


def check_file_contents(
    file_path: Path,
    expected_strs: Sequence[str] = (),
    unexpect_strs: Sequence[str] = (),
) -> None:
    """
    Check file contents.

    Parameters
    ----------
    file_path
        Path to file under test.
    expected_strs, optional
        Strings expected to exist somewhere in `file_path`'s target's text.
    unexpect_strs, optional
        Strings **not** expected to exist somewhere in `file_path`'s target's text.

    Notes
    -----
    Borrowed from:
    https://github.com/browniebroke/pypackage-template/blob/970407fb9ac71f42477ee2268a20b781a7a5bbcd/tests/test_generate_project.py#L32-L42
    Copyright (c) 2020 Bruno Alla
    Distributed under the terms of the MIT license.
    """
    assert file_path.exists()
    file_content = file_path.read_text()
    for content in expected_strs:
        assert content in file_content
    for content in unexpect_strs:
        assert content not in file_content


def git_init() -> None:
    """
    Initialize a Git repository with a first commit.
    """
    git("init")
    git("add", ".")
    git("commit", "-m", "chore: initial commit")


special_chars_re = re.compile(r"[^a-zA-Z0-9\s_-]+")


def remove_special_chars(string: str) -> str:
    """
    Remove characters that are not alphanumeric, a dash, an underscore, or a space.

    Parameters
    ----------
    string
        Input string to remove special characters from.

    Returns
    -------
        The string with special characters removed.
    """
    return re.sub(special_chars_re, "", string)


def snake_case(string: str) -> str:
    """
    Convert string to snake case.

    Parameters
    ----------
    string
        Input string to convert to snake case.

    Returns
    -------
        The string in snake case.
    """
    return string.lower().replace("-", "_").replace(" ", "_")
