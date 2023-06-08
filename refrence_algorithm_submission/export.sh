#!/usr/bin/env bash

. ./build.sh

docker save 3dteethseg_processing | gzip -c > 3dteethseg_testv0.10.tar.gz