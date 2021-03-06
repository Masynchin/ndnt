"""Arguments interface and its implementations."""

from abc import ABC, abstractmethod
from argparse import ArgumentParser
from typing import Sequence

from ndnt.extension import Extension
from ndnt.paths import Paths


class Arguments(ABC):
    """Ndnt arguments."""

    @abstractmethod
    def paths(self) -> Paths:
        """Path to inspect."""

    @abstractmethod
    def extension(self) -> Extension:
        """Extension to check."""

    @abstractmethod
    def no_gitignore(self) -> bool:
        """Whether do not use gitignore."""


class CliArguments(Arguments):
    """Arguments from CLI."""

    def __init__(self, args: Sequence[str], cli: ArgumentParser):
        self.args = args
        self.cli = cli

    def paths(self) -> Paths:
        """Path for CLI."""
        return self.cli.parse_args(self.args).paths

    def extension(self) -> Extension:
        """Extension for CLI."""
        return self.cli.parse_args(self.args).extension

    def no_gitignore(self) -> bool:
        """No gitignore for CLI."""
        return self.cli.parse_args(self.args).no_gitignore
