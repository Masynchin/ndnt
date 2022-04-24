from abc import ABC, abstractmethod
from argparse import ArgumentParser
from pathlib import Path
from typing import Iterable, Sequence

from ndnt.extension import Extension


class Arguments(ABC):
    """Ndnt arguments."""

    @abstractmethod
    def paths(self) -> Iterable[Path]:
        """Path to inspect."""

    @abstractmethod
    def extension(self) -> Extension:
        """Extension to check."""

    @abstractmethod
    def no_gitignore(self) -> bool:
        """Whether do not use gitignore."""


class CliArguments(Arguments):
    """Arguments for CLI."""

    def __init__(self, args: Sequence[str], cli: ArgumentParser):
        self.args = args
        self.cli = cli

    def paths(self) -> Iterable[Path]:
        """Path for CLI."""
        return self.cli.parse_args(self.args).paths

    def extension(self) -> Extension:
        """Extension for CLI."""
        return self.cli.parse_args(self.args).extension

    def no_gitignore(self) -> bool:
        """No gitignore for CLI."""
        return self.cli.parse_args(self.args).no_gitignore
