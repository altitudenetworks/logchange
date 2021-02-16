# logchange - Changelog manager

View, update and format your changelog anywhere!

## Features

- Keeps your changelog in [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) style
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

See [examples/cli.sh](https://github.com/vemel/logchange/tree/main/examples/cli.sh) folder.

```bash
# create CHANGELOG.md if it does not exist
# or reformat existing (please check changes manually)
logchange init -f

# add new release
cat NOTES_0.1.0.md | logchange add 0.1.0
# or
logchange add 0.2.0 -i `cat NOTES_0.2.0.md`

# update existing or create a new section in latest release
logchange add latest added -i 'New feature'

# set unreleased section
logchange set unreleased fixed -i 'Unreleased fix'

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

See [workflows](https://github.com/vemel/logchange/tree/main/examples/workflows) folder.

## Versioning

`logchange` version follows [PEP 440](https://www.python.org/dev/peps/pep-0440/).

## Latest changes

Full changelog can be found in [Releases](https://github.com/vemel/logchange/releases).
