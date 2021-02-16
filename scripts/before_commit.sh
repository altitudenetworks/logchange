#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

npx pyright
pytest
black logchange tests
isort logchange tests
flake8 logchange

./scripts/docs.sh
