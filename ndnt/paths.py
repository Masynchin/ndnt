from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable

from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern


class Paths(ABC):
    """Paths inteface.

    All `Paths` subclasses should behave like `Iterable[Path]`.
    """

    @abstractmethod
    def __iter__(self) -> Iterable[Path]: ...


class FilesPaths(Paths):
    """Files paths.

    All paths that are files from given direcatory.
    """

    def __init__(self, path: Path):
        self.path = path

    def __iter__(self) -> Iterable[Path]:
        return filter(lambda path: path.is_file(), self.path.glob("**/*"))


class PythonPaths(Paths):
    """Python paths.

    Wrap `Paths` origin and return only python files paths.
    """

    def __init__(self, origin: Paths):
        self.origin = origin

    def __iter__(self) -> Iterable[Path]:
        return filter(lambda path: path.suffix == ".py", self.origin)


class ExcludeGitignoredPaths(Paths):
    """Paths exluding paths that matches gitignore.

    Optimization inspired by "black" package:
    https://github.com/psf/black/blob/fda2561f79e10826dbdeb900b6124d642766229f/src/black/files.py#L177
    """

    def __init__(self, path: Path, gitignore_path: Path):
        self.path = path
        self.gitignore_path = gitignore_path

    def __iter__(self) -> Iterable[Path]:
        gitignore = PathSpec.from_lines(
            GitWildMatchPattern, self.gitignore_path.read_text().splitlines()
        )
        yield from self._iter(self.path, gitignore)

    def _iter(self, path: Path, gitignore: PathSpec) -> Iterable[Path]:
        """Optimized gitignore paths filter.

        Do not iterate directories if they are in gitignore.
        """
        for p in path.iterdir():
            if gitignore.match_file(p):
                continue

            if p.is_file():
                yield p
            elif p.is_dir():
                yield from self._iter(p, gitignore)
