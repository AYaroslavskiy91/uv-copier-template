import pytest
from jinja2 import Environment
from plumbum import local
from plumbum.cmd import git

from uv_copier_template.extensions import (
    CURRENT_FEATURE_PYTHON_VERSION,
    STABLE_PYTHON_VERSIONS,
    GitExtension,
    PythonVersionExtension,
    SlugifyExtension,
    Version,
    git_user_email,
    git_user_name,
    slugify,
    to_pyver_tag,
    version_lt,
)


def test_git_user_email(tmp_path_factory: pytest.TempPathFactory) -> None:
    dst = tmp_path_factory.mktemp("dst")
    with local.cwd(dst):
        git("init")

        # Test when the key is not set
        assert git_user_email() == git("config", "user.email").strip()

        # Test when the key is set
        git("config", "--local", "user.email", "email@example.com")
        assert git_user_email() == "email@example.com"


def test_git_user_name(tmp_path_factory: pytest.TempPathFactory) -> None:
    dst = tmp_path_factory.mktemp("dst")
    with local.cwd(dst):
        git("init")

        # Test when the key is not set
        assert git_user_name() == git("config", "user.name").strip()

        # Test when the key is set
        git("config", "--local", "user.name", "John Doe")
        assert git_user_name() == "John Doe"


def test_git_extension() -> None:
    environment = Environment(autoescape=True)
    GitExtension(environment)
    assert environment.filters["git_user_name"] == git_user_name
    assert environment.filters["git_user_email"] == git_user_email


def test_python_version_extension() -> None:
    environment = Environment(autoescape=True)
    PythonVersionExtension(environment)
    assert environment.globals["stable_python_versions"] == STABLE_PYTHON_VERSIONS
    assert environment.globals["all_python_versions"] == [
        *STABLE_PYTHON_VERSIONS,
        str(CURRENT_FEATURE_PYTHON_VERSION),
        str(CURRENT_FEATURE_PYTHON_VERSION.next_major_version()),
    ]
    assert environment.filters["to_pyver_tag"] == to_pyver_tag
    assert environment.filters["versionize"] == Version
    assert environment.tests["version_lt"] == version_lt


@pytest.mark.parametrize(
    ("actual", "expected", "separator"),
    [
        ("uv copier template", "uv-copier-template", "-"),
        ("uv-copier-template", "uv_copier_template", "_"),
        ("⭐️ My GitHub Stars ⭐️", "my-github-stars", "-"),
    ],
)
def test_slugify(actual: str, expected: str, separator: str) -> None:
    assert slugify(actual, separator=separator) == expected


def test_slugify_extension() -> None:
    environment = Environment(autoescape=True)
    SlugifyExtension(environment)
    assert environment.filters["slugify"] == slugify
