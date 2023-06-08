#!/usr/bin/env bashchown
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

docker build -t 3dteetheg_eval "$SCRIPTPATH"
