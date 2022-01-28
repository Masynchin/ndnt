from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable

from ndnt.indent import AverageIndent, RoundedAverageIndent
from ndnt.lines import LinesFromFile, LinesFromFiles, NonBlankLines


class Summary(ABC):
    """Summary interface.

    All `Summary` subclasses must have `print()` method to display its summary.
    """

    @abstractmethod
    def print(self): ...


class FileSummary(Summary):
    """File summary.

    Shows file's average indent (excluding blank lines) and its path.
    """

    def __init__(self, path: Path):
        self.path = path

    def print(self):
        lines = NonBlankLines(LinesFromFile(self.path))
        indent = RoundedAverageIndent(AverageIndent(lines)).value()
        print(f"{indent:<5} |", self.path)


class FilesSummary(Summary):
    """Directory summary.

    Shows average indent of multiple files.
    """

    def __init__(self, paths: Iterable[Path]):
        self.paths = paths

    def print(self):
        total_lines = NonBlankLines(LinesFromFiles(self.paths))
        total_indent = RoundedAverageIndent(AverageIndent(total_lines)).value()
        print(f"{total_indent:<5} | Total")


class DirectorySummary(Summary):
    """Directory summary.

    Shows average indent of all files separately and then
    average indent of all files combined.
    """

    def __init__(self, paths: Iterable[Path]):
        self.paths = paths

    def print(self):
        for file in self.paths:
            FileSummary(file).print()

        print("-" * 13)
        FilesSummary(self.paths).print()
