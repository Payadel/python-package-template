# Python Package Template

[![PyPI Project Version][pypi-image]][pypi-project-url]
[![Build Status][build-image]][build-url]
[![][stars-image]][stars-url]

## Install Requirements

```shell
python -m pip install poetry
poetry install
pre-commit install
```

**Recommend**: use [Payadel README template](https://github.com/Payadel/README/).

## Upload package

### Test Repository

#### Configure the **test** repository:

1. `poetry config repositories.testpypi https://test.pypi.org/legacy/`
2. Get a key: `https://test.pypi.org/account/register/`
3. `poetry config http-basic.testpypi __token__ pypi-your-api-token-here`

#### Build and publish to the **test** repository:

1. Run tests: `tox`
2. poetry build
3. poetry publish -r testpypi

### PyPI Repository

#### Configure PyPI

1. Get a key: `https://pypi.org/`
2. `poetry config pypi-token.pypi pypi-your-token-here`

#### Build and publish

1. Run tests: `tox`
2. poetry publish --build

<!-- Badges: -->

[pypi-project-url]: https://pypi.org/project/PROJECT_NAME/

[build-url]: https://github.com/USER_NAME/REPO_NAME/actions/workflows/build.yaml

[stars-url]: https://github.com/USER_NAME/REPO_NAME