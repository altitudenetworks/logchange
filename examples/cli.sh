#!/usr/bin/env bash
set -e

# create CHANGELOG.md if it does not exist
# or reformat existing (please check changes manually)
logchange init -f

# list existing releases
logchange list
# > 1.1.0
# > 1.0.0

# get `Added` section of the latest release
logchange get latest added
# > - `set` CLI command
# > - `semver` format support

# add new entry to `Added` section of the latest release
logchange add latest added -i "Version output to CLI"

# create a new release
cat NOTES_1.2.0.md | logchange add 1.2.0
# or
# logchange add 1.2.0 -i `cat NOTES_1.2.0.md`

# set unreleased section
logchange set unreleased fixed -i 'Unreleased fix'

# list released versions
logchange list
< 1.2.0
< 1.1.0
< 1.0.0


# all commands

# create CHANGELOG.md
logchange init

# create or reformat CHANGELOG.md
logchange init -f

# get suggested version based on release notes
logchange version 1.2.3 -i `cat NOTE.md`

# get suggested version based on unreleased section in CHANGELOG.md
logchange version 1.2.3

# get release section notes from CHANGELOG.md
logchange get <version> <section>
logchange get <version>
logchange get unreleased <section>
logchange get unreleased

# add or update release section in CHANGELOG.md
logchange add <version> <section> -i "<change text>"
logchange add <version> -i "`cat NOTE.md`"
logchange add latest <section> -i "<change text>"
logchange add latest -i "`cat NOTE.md`"
logchange add unreleased <section> -i "<change text>"
logchange add unreleased -i "`cat NOTE.md`"

# add or replace release section in CHANGELOG.md
logchange set <version> <section> -i "<change text>"
logchange set <version> -i "`cat NOTE.md`"
logchange set latest <section> -i "<change text>"
logchange set latest -i "`cat NOTE.md`"
logchange set unreleased <section> -i "<change text>"
logchange set unreleased -i "`cat NOTE.md`"

# list releases from CHANGELOG.md
logchange list

# format release note and output to stdout
logchange format -i "`cat NOTE.md`"
