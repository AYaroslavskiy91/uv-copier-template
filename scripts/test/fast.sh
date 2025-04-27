#!/usr/bin/env -S uv run bash

pytest -m "not slow" "$@" tests
