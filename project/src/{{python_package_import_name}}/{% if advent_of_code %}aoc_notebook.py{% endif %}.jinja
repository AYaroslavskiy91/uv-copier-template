import argparse
import datetime
from pathlib import Path

import nbformat


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--template",
        help="Path to template .ipynb file",
        default="notebooks/_template.ipynb",
    )

    # Optional year/day args; default to today
    today = datetime.date.today()
    parser.add_argument(
        "--year",
        type=int,
        default=today.year,
        help="Year to fill into template",
    )

    parser.add_argument(
        "--day",
        type=int,
        default=today.day,
        help="Day to fill into template",
    )

    parser.add_argument(
        "--output",
        help="Output notebook filename (defaults to YYYY_DD.ipynb)",
    )

    args = parser.parse_args()

    if args.output:
        args.output_path = args.output
    else:
        args.output_path = f"notebooks/{args.year}/day{args.day:02d}.ipynb"
    return args


def main():
    args = parse_args()
    nb = nbformat.read(
        args.template,
        as_version=4,
    )

    for cell in nb.cells:
        if cell.cell_type == "code":
            source = cell.source
            source = source.replace("year = _", f"year = {args.year}")
            source = source.replace("day = _", f"day = {args.day}")
            cell.source = source

    path = Path(args.output_path)
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    nbformat.write(nb, args.output_path)
    print(f"Created: {args.output_path}")


if __name__ == "__main__":
    main()
