import pathlib
import random

import pytest

DIR_TESTS_ROOT = pathlib.Path(__file__).parent.resolve()
DIR_REPO_ROOT = DIR_TESTS_ROOT.parent.resolve()


@pytest.fixture(scope="session", autouse=True)
def faker_seed() -> float:
    return random.random()  # noqa: S311
