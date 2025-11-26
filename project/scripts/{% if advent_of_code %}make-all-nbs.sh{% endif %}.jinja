#!/usr/bin/env bash
set -euo pipefail

COUNT=12
YEAR="$(date +%Y)"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --count|-c)
            COUNT="$2"
            shift 2
            ;;
        --year|-y)
            YEAR="$2"
            shift 2
            ;;
        *)
            echo "Unknown argument: $1" >&2
            exit 1
            ;;
    esac
done

for DAY in $(seq 1 "$COUNT"); do
    echo "Generating day $DAY for year $YEAR..."
    uv run ./src/advent_of_code/aoc_notebook.py --year "$YEAR" --day "$DAY"
done
