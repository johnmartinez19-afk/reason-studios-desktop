"""Reason Studios Desktop — A desktop helper that finds Reason Studios project directories and archives preset and sample files locally."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='reason_studios_desktop',
        description='A desktop helper that finds Reason Studios project directories and archives preset and sample files locally.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Reason Studios Desktop')
    print('Dated copies of Reason Studios project data, nothing uploaded.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
