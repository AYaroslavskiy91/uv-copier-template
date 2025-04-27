#!/usr/bin/env -S uv run bash

mypy --install-types --non-interactive -p uv_copier_template -p tests -p plumbum
