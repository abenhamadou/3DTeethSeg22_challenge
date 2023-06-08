#!/usr/bin/env bash

. ./build.sh

docker save 3dteetheg_eval | gzip -c > 3dteetheg_eval_final_testset_v0.2.tar