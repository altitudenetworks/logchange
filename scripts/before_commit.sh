#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

npx pyright
pytest
isort .
black .
flake8 logchange

./scripts/docs.sh
