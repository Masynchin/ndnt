from argparse import ArgumentParser
from pathlib import Path

from ndnt.paths import ExcludeGitignoredPaths, ExtensionPaths, FilesPaths
from ndnt.summary import DirectorySummary, FileSummary


def setup_parser() -> ArgumentParser:
    """Setup CLI parser."""
    parser = ArgumentParser(description="Inspect indents of your files.")
    parser.add_argument(
        "path", type=Path, help="Whether file or directory to get summary of."
    )
    parser.add_argument(
        "-e",
        "--extension",
        default=".py",
        help="Filter files by extension.",
    )
    parser.add_argument(
        "--no-gitignore",
        action="store_true",
        help="Do not exclude paths matches gitignore.",
    )
    return parser


def parse_args():
    """Parse args provided by CLI."""
    return setup_parser().parse_args()


def main():
    """Main function called with `ndnt` command."""
    main_with_args(**parse_args().__dict__)


def main_with_args(path: Path, no_gitignore: bool, extension: str):
    """Main function.

    Choose summary depends on provided arguments and print it.
    """
    no_gitignore = no_gitignore or not (path / ".gitignore").exists()

    if path.is_file():
        summary = FileSummary(path)
    elif path.is_dir() and no_gitignore:
        summary = DirectorySummary(
            ExtensionPaths(FilesPaths(path), extension)
        )
    elif path.is_dir():
        summary = DirectorySummary(
            ExtensionPaths(
                ExcludeGitignoredPaths(path, path / ".gitignore"),
                extension,
            )
        )
    else:
        print(f"Something is wrong with provided path.")
        return

    summary.print()
