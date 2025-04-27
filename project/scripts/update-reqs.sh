#!/bin/bash

echo 1
./scripts/clean-envs.sh
echo 2

rm -f uv.lock

echo 3
./scripts/init-envs.sh
