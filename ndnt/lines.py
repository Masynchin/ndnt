from abc import ABC, abstractmethod
from itertools import chain
from pathlib import Path
from typing import Iterable

from ndnt.line import Line


class Lines(ABC):
    """Lines interface.

    All `Lines` subclasses should behave like `Iterable[Lines]`.
    """

    @abstractmethod
    def __iter__(self) -> Iterable[Line]: ...


class LinesFromText(Lines):
    """Lines from text."""

    def __init__(self, text: str):
        self.text = text

    def __iter__(self) -> Iterable[Line]:
        return map(Line, self.text.splitlines())


class LinesFromFile(Lines):
    """Lines from file."""

    def __init__(self, path: Path):
        self.path = path

    def __iter__(self) -> Iterable[Line]:
        with self.path.open(encoding="u8") as f:
            lines = f.readlines()

        return map(lambda line: Line(line.rstrip("\n")), lines)


class NonBlankLines(Lines):
    """Non blank lines."""

    def __init__(self, origin: Lines):
        self.origin = origin

    def __iter__(self) -> Iterable[Line]:
        return filter(None, self.origin)


class CombinedLines(Lines):
    """Multiple `Lines` combined as one `Lines`."""

    def __init__(self, origins: Iterable[Lines]):
        self.origins = origins

    def __iter__(self) -> Iterable[Line]:
        return chain.from_iterable(self.origins)


class LinesFromFiles(Lines):
    """Lines from multiple files as one `Lines`."""

    def __init__(self, paths: Iterable[Path]):
        self.paths = paths

    def __iter__(self) -> Iterable[Line]:
        yield from CombinedLines(map(LinesFromFile, self.paths))
