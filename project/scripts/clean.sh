#!/bin/bash

find . -maxdepth 3 -type d -name __pycache__ | xargs rm -rf
rm -rf .mypy_cache
rm -rf .ruff_cache

./scripts/clean-test.sh
