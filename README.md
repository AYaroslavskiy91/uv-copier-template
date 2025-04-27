# uv Copier Template

<!-- badges-begin -->

[![Copier][copier badge]](https://github.com/copier-org/copier)<br>
[![GitHub][github badge]][github page]
[![Python versions][python badge]][github page]
[![CalVer][calver badge]][calver]<br>
[![uv][uv badge]](https://github.com/astral-sh/uv)<br>
[![pre-commit enabled][pre-commit badge]][pre-commit]
[![Ruff][ruff badge]](https://github.com/astral-sh/ruff)
[![Checked with mypy][mypy badge]][mypy]
[![basedpyright - checked][basedpyright badge]][basedpyright]
[![Pytest][pytest badge]][pytest]

[basedpyright badge]: https://img.shields.io/badge/basedpyright-checked-42b983
[basedpyright]: https://docs.basedpyright.com
[calver badge]: https://img.shields.io/badge/calver-YYYY.MM.MICRO-22bfda.svg
[calver]: http://calver.org/
[copier badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json
[copier]: https://copier.readthedocs.io/en/stable/
[github badge]: https://badgen.net/badge/icon/github?icon=github&label
[github page]: https://github.com/ayaroslavskiy91/uv-copier-template
[mypy badge]: https://www.mypy-lang.org/static/mypy_badge.svg
[mypy]: https://mypy-lang.org/
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit]: https://pre-commit.com/
[pytest badge]: https://img.shields.io/static/v1?label=%E2%80%8E&message=Pytest&logo=Pytest&color=0A9EDC&logoColor=white
[pytest]: https://docs.pytest.org/en/stable/
[python badge]: https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue?logo=python&label=Python&logoColor=gold
[ruff badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff]: https://docs.astral.sh/ruff/
[uv badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json
[uv]: https://docs.astral.sh/uv/

<!-- badges-end -->

---

Opinionated [Copier] template for Python projects managed by [uv].

This template was created for personal use, but I'd be smitten if others find it
helpful (_please smash that **star** button_).

## Usage

If all the [requirements](/README.md#setup) are met:

```shell
copier copy --trust "git@github.com:ayaroslavskiy91/uv-copier-template.git" path/to/destination
```

If the [Git] & [uv] requirements are met but you don't want to install [Copier]
as a [uv] tool:

```shell
uvx --python=3.11 --python-preference=managed --with=copier-templates-extensions \
    copier copy --trust "git@github.com:ayaroslavskiy91/uv-copier-template.git" path/to/destination
```

### Updating

To update an existing project based on this template, run:

```shell
copier update --trust
```

For more information on updating a project,
[see the official instructions](https://copier.readthedocs.io/en/stable/updating/).

## Features

- Project setup and template update with [Copier]
- Centralized package, build, & tool configuration in [pyproject.toml]
- Packaging, incredibly fast dependency management, Python interpreter management, & universal lock file support with [uv]
- Style guide enforcement both locally & in CI with [pre-commit]
- Code formatting, linting, import sorting, automated Python syntax upgrades, & security auditing with [Ruff]
- Continuous integration with [GitHub Actions]
- Unit testing with [pytest]
- Code coverage measurement with [Coverage.py]
- Static type-checking with [mypy] & [basedpyright]
- [src layout]: Python package under `src` directory to avoid common errors
<!-- - Documentation with [Sphinx] using the [Furo] theme -->
<!-- - Generate API documentation with [autodoc] and [napoleon] -->

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[coverage.py]: https://coverage.readthedocs.io/
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[pyproject.toml]: https://packaging.python.org/en/latest/specifications/pyproject-toml/
[sphinx]: http://www.sphinx-doc.org/
[src layout]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/

## Setup

To use this template, you will need:

- [Git] >= 2.27
- [uv] >= 0.6.0
- [Copier] >= 9.4

### [Git]

Check the installed version of [Git] with:

```shell
git --version
```

If the version is < 2.27,
[follow the official instructions](https://git-scm.com/downloads)
to install [Git] version 2
or, alternatively, install with [Homebrew]:

```shell
brew install git
```

### [uv]

To install [uv],
[follow the official instructions](https://docs.astral.sh/uv/getting-started/installation/)
or, alternatively, install with [Homebrew]:

```shell
brew install uv
```

### [Copier]

Use [uv] to install [Copier] as a global tool, including [Jinja] extensions:

```shell
uv tool install copier --with=copier-templates-extensions
```

[git]: https://git-scm.com/
[homebrew]: https://brew.sh/
[jinja]: https://jinja.palletsprojects.com

## Testing

This template includes both an (incomplete) unit test suite and
a minimal integration test suite that uses
[copier-template-tester] to render the templates specified by the mock answers
in `ctt.toml`.

### Unit Tests

To run the [pytest] unit tests:

```shell
./scripts/test/test.sh
```

### Integration Tests

To run the [copier-template-tester]-based integration tests:

```shell
./scripts/test/ctt.sh
```

_**Info**: The location of the rendered output for each template is determined by the
name of the section in `ctt.toml` defining its parameters;
specifically by the relative path following `output.`
e.g., `[output.".ctt/defaults"]` will render to `.ctt/defaults`._

The test output can be removed with

```shell
./scripts/test/clean.sh
```

[copier-template-tester]: https://copier-template-tester.kyleking.me/

## Acknowledgements

This template stands on the shoulders of
[Claudio Jolowicz (cjolowicz)](https://github.com/cjolowicz)'s
[Hypermodern Python Cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python),
the [many](https://github.com/pawamoy/copier-uv)
[excellent](https://github.com/pawamoy/copier-pdm) Copier
[templates](https://github.com/pawamoy/copier-poetry) of
[Timothée Mazzucotelli (pawamoy)](https://github.com/pawamoy),
[Bruno Alla (browniebroke)](https://github.com/browniebroke)'s
[pypackage-template](https://github.com/browniebroke/pypackage-template),
& [Spacecoffin](https://github.com/spacecoffin)'s [copier-hatch](https://github.com/spacecoffin/copier-hatch).


_I have done my best to document all borrowed code with the appropriate copyright
notices and either the permission notices themselves or a reference to the license
under which the original code is distributed. As this project was originally developed
as a personal project (never to see the light of open source distribution), these notices
were added post-hoc. If any discrepancies are found, please file an
[issue](https://github.com/ayaroslavskiy91/uv-copier-template/issues)
so I can give proper credit._
