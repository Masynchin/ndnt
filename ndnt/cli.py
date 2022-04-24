from argparse import ArgumentParser
from pathlib import Path

from ndnt.extension import AnyProgrammingExtension, ExactExtension


class Cli(ArgumentParser):
    """Cli of Ndnt."""

    def __init__(self):
        super().__init__(description="Inspect indents of your files.")
        super().add_argument(
            "paths",
            nargs="*",
            type=Path,
            help="Whether files or directories to get summary of.",
        )
        super().add_argument(
            "-e",
            "--extension",
            type=ExactExtension,
            default=AnyProgrammingExtension(),
            help="Filter files by extension.",
        )
        super().add_argument(
            "--no-gitignore",
            action="store_true",
            help="Do not exclude paths matches gitignore.",
        )
