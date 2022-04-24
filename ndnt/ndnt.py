from pathlib import Path

from ndnt.arguments import Arguments
from ndnt.extension import Extension
from ndnt.paths import ExcludeGitignoredPaths, ExtensionPaths, FilesPaths
from ndnt.summary import DirectorySummary, FileSummary


class Ndnts:
    """Main class of this tool."""

    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def run(self):
        """Run itself."""
        paths = self.arguments.paths()
        extension = self.arguments.extension()
        no_gitignore = self.arguments.no_gitignore()

        for path in paths:
            Ndnt(path, extension, no_gitignore).run()


class Ndnt:
    """Analyze of one path."""

    def __init__(self, path: Path, extension: Extension, no_gitignore: bool):
        self.path = path
        self.extension = extension
        self.no_gitignore = no_gitignore

    def run(self):
        """Run itself."""
        no_gitignore = (
            self.no_gitignore or not (self.path / ".gitignore").exists()
        )

        if self.path.is_file():
            summary = FileSummary(self.path)
        elif self.path.is_dir() and no_gitignore:
            summary = DirectorySummary(
                ExtensionPaths(FilesPaths(self.path), self.extension)
            )
        elif self.path.is_dir():
            summary = DirectorySummary(
                ExtensionPaths(
                    ExcludeGitignoredPaths(self.path, self.path / ".gitignore"),
                    self.extension,
                )
            )
        else:
            print("Something is wrong with provided path.")
            return

        summary.print()
