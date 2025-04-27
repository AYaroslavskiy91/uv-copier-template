from pathlib import Path

import copier
import pytest
from faker import Faker
from plumbum import local
from plumbum.cmd import git

from .conftest import DIR_REPO_ROOT
from .helpers import (
    build_file_tree,
    git_init,
    remove_special_chars,
    snake_case,
)


@pytest.mark.filterwarnings("ignore:Dirty template changes included automatically.")
@pytest.mark.slow
def test_no_clobber_on_introduction(
    tmp_path_factory: pytest.TempPathFactory,
    faker: Faker,
) -> None:
    project_name = remove_special_chars(faker.catch_phrase()).title()
    dst = tmp_path_factory.mktemp("dst")
    with local.cwd(dst):
        build_file_tree(
            {
                f"src/{snake_case(project_name)}/__init__.py": f'"""{project_name}"""',
                "tests/__init__.py": '"""Tests"""',
                "tests/test_something.py": "def test_this_thing(): assert True",
            }
        )
        git_init()
    answers = {
        "project_name": project_name,
        "project_description": remove_special_chars(faker.bs()).capitalize() + ".",
    }
    with copier.Worker(
        src_path=str(DIR_REPO_ROOT),
        dst_path=dst,
        vcs_ref="HEAD",
        data=answers,
        defaults=True,
        unsafe=True,
    ) as worker:
        worker.run_copy()
    assert (
        dst / f"src/{snake_case(project_name)}/__init__.py"
    ).read_text() == f'"""{project_name}"""'
    assert (dst / "tests/__init__.py").read_text() == '"""Tests"""'
    assert (
        dst / "tests/test_something.py"
    ).read_text() == "def test_this_thing(): assert True"
    assert not (dst / "test/test_placeholder.py").exists()


@pytest.mark.skip(reason="Waiting on bug fix")
@pytest.mark.filterwarnings("ignore:Dirty template changes included automatically.")
@pytest.mark.slow
def test_no_clobber_on_update(
    tmp_path_factory: pytest.TempPathFactory,
    faker: Faker,
) -> None:
    project_name = remove_special_chars(faker.catch_phrase()).title()
    answers = {
        "project_name": project_name,
        "project_description": remove_special_chars(faker.bs()).capitalize() + ".",
    }
    dst = tmp_path_factory.mktemp("dst")
    with copier.Worker(
        src_path=str(DIR_REPO_ROOT),
        dst_path=dst,
        vcs_ref="856b395c0b5530151f22fc41dc9ed42a1e5af3e9",
        data=answers,
        defaults=True,
        unsafe=True,
    ) as worker:
        worker.run_copy()
    with local.cwd(dst):
        build_file_tree(
            {
                f"src/{snake_case(project_name)}/__init__.py": f'"""{project_name}"""',
                "tests/__init__.py": '"""Tests"""',
                "tests/test_something.py": "def test_this_thing(): assert True",
            }
        )
        Path("tests/test_placeholder.py").unlink()
        git("add", ".")
        git("commit", "-m", "tests: add a test")
    with copier.Worker(
        src_path=str(DIR_REPO_ROOT),
        dst_path=dst,
        vcs_ref="HEAD",
        data=answers,
        defaults=True,
        overwrite=True,
        unsafe=True,
    ) as worker:
        worker.run_update()
    assert (
        dst / f"src/{snake_case(project_name)}/__init__.py"
    ).read_text() == f'"""{project_name}"""'
    assert (dst / "tests/__init__.py").read_text() == '"""Tests"""'
    assert (
        dst / "tests/test_something.py"
    ).read_text() == "def test_this_thing(): assert True"
    assert not (dst / "test/test_placeholder.py").exists()
