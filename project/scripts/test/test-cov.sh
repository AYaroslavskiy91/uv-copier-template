#!/usr/bin/env -S uv run bash

coverage run -m pytest "$@" tests
