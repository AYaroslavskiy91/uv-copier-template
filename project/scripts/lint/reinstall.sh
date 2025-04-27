#!/bin/bash

uvx pre-commit uninstall
uvx pre-commit clean
uvx pre-commit gc

./scripts/lint/install.sh
