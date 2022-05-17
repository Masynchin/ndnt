"""Summary interface and its implementations."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import TextIO

from ndnt.indent import AverageIndent, RoundedAverageIndent
from ndnt.lines import LinesFromFile, LinesFromFiles, NonBlankLines
from ndnt.paths import Paths


class Summary(ABC):
    """Summary interface.

    All `Summary` subclasses must have `print()` method to display its summary.
    """

    @abstractmethod
    def print(self, out: TextIO):
        """Print itself."""


class FileSummary(Summary):
    """File summary.

    Shows file's average indent (excluding blank lines) and its path.
    """

    def __init__(self, path: Path):
        self.path = path

    def print(self, out: TextIO):
        """Print itself."""
        lines = NonBlankLines(LinesFromFile(self.path))
        indent = RoundedAverageIndent(AverageIndent(lines)).value()
        out.write(f"{indent:<5} | {self.path}\n")


class FilesSummary(Summary):
    """Files summary.

    Shows average indent of multiple files.
    """

    def __init__(self, paths: Paths):
        self.paths = paths

    def print(self, out: TextIO):
        """Print itself."""
        total_lines = NonBlankLines(LinesFromFiles(self.paths))
        total_indent = RoundedAverageIndent(AverageIndent(total_lines)).value()
        out.write(f"{total_indent:<5} | Total\n")


class DirectorySummary(Summary):
    """Directory summary.

    Shows average indent of all files separately and then
    average indent of all files combined.
    """

    def __init__(self, paths: Paths):
        self.paths = paths

    def print(self, out: TextIO):
        """Print itself."""
        for file in self.paths:
            FileSummary(file).print(out)

        out.write("-" * 13 + "\n")
        FilesSummary(self.paths).print(out)
