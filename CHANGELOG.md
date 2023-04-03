# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## [0.2.0](https://github.com/Payadel/python-package-template/compare/v0.1.2...v0.2.0) (2023-04-03)


### ⚠ BREAKING CHANGES

* **publish:** separates publish section from release
* **precommit:** remove isort arg from .pre-commit-config.yaml

### Features

* **gitignore:** add `pyc` files to gitignore ([1062ac7](https://github.com/Payadel/python-package-template/commit/1062ac7bbcd6089633c460c65f5b4b97fcd11423))
* **publish:** add inputs to publish-test.yaml action ([8edca18](https://github.com/Payadel/python-package-template/commit/8edca18b22b9ac64cb420699cbfd335ccc9ed64d))
* **pyproject:** add `repository` and `keywords` fields to pyproject.toml ([251e597](https://github.com/Payadel/python-package-template/commit/251e597391730fdb1f44dec3c4bcc28caa04cd4c))


### Development: CI/CD, Build, etc

* **lock:** update lock.yml ([f70e463](https://github.com/Payadel/python-package-template/commit/f70e463a4ddc76709248340074d8f334e9fa8e0f))
* **makefile:** add Makefile ([947b382](https://github.com/Payadel/python-package-template/commit/947b3823ee0c771b88c29857bb3da7098333f584))


### Fixes

* **precommit:** remove isort arg from .pre-commit-config.yaml ([e9f1bd5](https://github.com/Payadel/python-package-template/commit/e9f1bd5aa640ced071fb0a1aa5bf8170c99298de))
* **precommit:** update `pre-commit-hooks` to v4.4.0 ([3f82d9b](https://github.com/Payadel/python-package-template/commit/3f82d9be7e9e6c14adf9527344ed96bf425e15e3))
* **publish:** fix `pypi_token` token name in publish-test.yaml ([94cb0c1](https://github.com/Payadel/python-package-template/commit/94cb0c1becefd55776d1a0b00b3cd4833fc8f368))
* **publish:** separates publish section from release ([cbfa7d9](https://github.com/Payadel/python-package-template/commit/cbfa7d9f91c21e39390deb30a4c70ca213202cf3))
* **release:** fix `Update poetry version` bug ([8d1d99b](https://github.com/Payadel/python-package-template/commit/8d1d99b168d3717810043c15ff41a464f053451e))

### [0.1.2](https://github.com/Payadel/python-package-template/compare/v0.1.1...v0.1.2) (2023-03-30)


### Fixes

* **codeql:** fix python-version ([fbc3efe](https://github.com/Payadel/python-package-template/commit/fbc3efedbf4b22b35f60e4fe8c0cf29aca774551))


### Development: CI/CD, Build, etc

* **codeql:** remove codeql action ([314529e](https://github.com/Payadel/python-package-template/commit/314529eca72971561db3f1339b04e43037b017f6))

### [0.1.1](https://github.com/Payadel/python-package-template/compare/v0.1.0...v0.1.1) (2023-03-29)


### Fixes

* update release.yaml. add `needs: [Release]` to `build-and-publish` job ([18740eb](https://github.com/Payadel/python-package-template/commit/18740ebd9169bf512f9f7084085b7b1243be7aab))

## [0.1.0](https://github.com/Payadel/python-package-template/compare/v0.0.4...v0.1.0) (2023-03-29)


### ⚠ BREAKING CHANGES

* **release:** remove publish.yaml

### Features

* **release:** add release.yaml that combines release and publish ([54d01d4](https://github.com/Payadel/python-package-template/commit/54d01d4cad048c9839eca467d13dfc7704e64e6e))

### [0.0.4](https://github.com/Payadel/python-package-template/compare/v0.0.3...v0.0.4) (2023-03-29)


### Features

* **ci:** add codeql.yml GitHub action ([16baece](https://github.com/Payadel/python-package-template/commit/16baece416e12cbfb743fe7f8cd68d583300dcb1))

### [0.0.3](https://github.com/Payadel/python-package-template/compare/v0.0.2...v0.0.3) (2023-03-25)

### Features

* **publish:** add publish-test.yaml action for publish to
  the `testpypi` ([2822bee](https://github.com/Payadel/python-package-template/commit/2822beea03705375051a36e6c9df77312ceceeca))
* **readme:** add
  README.md ([0826182](https://github.com/Payadel/python-package-template/commit/082618241f41234f05efc58340481e272181c669))

### Fixes

* **gitignore:** fix `.idea`
  folder ([fc750b2](https://github.com/Payadel/python-package-template/commit/fc750b279d73114a77ce7fadbcef64cffb5b3028))
* **publish:** fix `pypi` token name in
  publish.yaml ([789af44](https://github.com/Payadel/python-package-template/commit/789af44585f40dc4bcd22db74f38b67ea0335905))
* **pyproject:** add `tox` and `tox-gh-actions` to the poetry
  dependencies ([763a65f](https://github.com/Payadel/python-package-template/commit/763a65f7e528d596d21cf12766bcb219f52ff8ed))

### Development: CI/CD, Build, etc

* **release:** update Payadel/release-sv-action to
  v0.2.1 ([26cfcd9](https://github.com/Payadel/python-package-template/commit/26cfcd953cd11d59827ebe9d73ec9e5f631d1e1f))

### [0.0.2](https://github.com/Payadel/python-package-template/compare/v0.0.1...v0.0.2) (2023-03-21)

### Features

* add `tool.poetry.scripts` section to
  pyproject.toml ([3dab3ae](https://github.com/Payadel/python-package-template/commit/3dab3aeb1727c3bc65a188eb55ba00b4ab105025))

### Fixes

* add poetry.lock to
  .gitignore ([a89ded0](https://github.com/Payadel/python-package-template/commit/a89ded07e1ba3369bb015a72a093f04296916df8))
* fix coverage command in
  tox.ini ([97c49a4](https://github.com/Payadel/python-package-template/commit/97c49a4dd7120d373c22c76377ac28f785beb314))
* rename `hooks` directory
  to `.hooks` ([050dbbd](https://github.com/Payadel/python-package-template/commit/050dbbd38bf0f6d980dd2ee6f44f41582cc8ede8))

### Development: CI/CD, Build, etc

* use Payadel actions to changelog.yaml and
  release.yaml ([971ddb0](https://github.com/Payadel/python-package-template/commit/971ddb00b7c3893e966177c7b886bd1b26613fd4))

### 0.0.1 (2023-03-20)

### Features

* add base
  codes ([4781181](https://github.com/Payadel/python-package-template/commit/47811815dbef6959861b821371f6673bbe1955f8))
* add Payadel readme
  template ([88b4ae3](https://github.com/Payadel/python-package-template/commit/88b4ae3d87d6d88fd0bc8dddcc4cf28290cd8ac5)
  , [471e424](https://github.com/Payadel/python-package-template/commit/471e424e8ba44a9a8d70a078ba68639cef104c5a))