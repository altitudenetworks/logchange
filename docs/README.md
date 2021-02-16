# logchange - Changelog manager

> Auto-generated documentation index.

View, update and format your changelog anywhere!

Full logchange project documentation can be found in [Modules](MODULES.md#logchange-modules)

- [logchange - Changelog manager](#logchange---changelog-manager)
    - [Features](#features)
    - [Installation](#installation)
    - [Usage](#usage)
        - [CLI](#cli)
        - [GitHub Actions](#github-actions)
    - [Versioning](#versioning)
    - [Latest changes](#latest-changes)
  - [logchange Modules](MODULES.md#logchange-modules)

## Features

- Kepp your changelog in [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) style
- Supports version bumping from [semver](https://pypi.org/project/semver/)
- Comes with a CLI tool `logchange`
- Respects MarkDown
- Created for CI and scripts

## Installation

```bash
python -m pip install logchange
```

## Usage

### CLI

```bash
# create CHANGELOG.md if it does not exist
# or reformat existing (please check changes manually)
logchange init -f

# add new release
cat NOTES_0.1.0.md | logchange add 0.1.0
# or
logchange add 0.2.0 -i `cat NOTES_0.2.0.md`

# list released versions
logchange list
< 0.1.0
< 0.2.0

# check release notes sections
logchange get 0.1.0 added
< - New awesome feature
< - Another feature
```

### GitHub Actions

See `workflows` folder.

## Versioning

`logchange` version follows [PEP 440](https://www.python.org/dev/peps/pep-0440/).

## Latest changes

Full changelog can be found in [Releases](https://github.com/vemel/logchange/releases).
