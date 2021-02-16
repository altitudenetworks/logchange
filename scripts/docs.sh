#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

handsdown --external 'https://github.com/vemel/logchange/blob/main/' -n logchange logchange --exclude '*/build/*' --cleanup --panic
