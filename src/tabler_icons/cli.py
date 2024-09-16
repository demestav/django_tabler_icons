from __future__ import annotations

import argparse

from tabler_icons import icon_directory
from tabler_icons.utils import download_icons


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    download_parser = subparsers.add_parser("download", help="Download icon set")
    download_parser.add_argument(
        "-y", "--yes", action="store_true", help="Download without confirmation"
    )

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        exit(0)

    if args.command == "download":
        print(f"Icon set will be downloaded to {icon_directory}")
        if not args.yes:
            confirm = input("Do you want to proceed with the installation? [y/N]: ")
            if confirm.lower() != "y":
                exit(0)
        print("Downloading...")
        download_icons(icon_directory)
