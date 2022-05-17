from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from ndnt.arguments import Arguments
from ndnt.extension import Extension
from ndnt.ndnt import Ndnts
from ndnt.paths import Paths
from ndnt.summary import FileSummary


class FakeArguments(Arguments):
    """Fake class to mock arguments."""

    def __init__(self, paths: Paths, extension: Extension, no_gitignore: bool):
        self._paths = paths
        self._extension = extension
        self._no_gitignore = no_gitignore

    def paths(self) -> Paths:
        return self._paths

    def extension(self) -> Extension:
        return self._extension

    def no_gitignore(self) -> bool:
        return self._no_gitignore


def test_on_single_path():
    path = Path("tests/fake_folder/fake.py")
    arguments = FakeArguments(
        paths=[path],
        extension=".py",
        no_gitignore=False,
    )

    printed = StringIO()
    with redirect_stdout(printed):
        Ndnts(arguments).run()

    expected = StringIO()
    FileSummary(path).print(expected)

    assert printed.getvalue() == expected.getvalue()


def test_on_multiple_paths():
    paths = [
        Path("tests/fake_folder/fake.py"),
        Path("tests/fake_folder/fake.py"),
    ]
    arguments = FakeArguments(
        paths=paths,
        extension=".py",
        no_gitignore=False,
    )

    printed = StringIO()
    with redirect_stdout(printed):
        Ndnts(arguments).run()

    expected = StringIO()
    for path in paths:
        FileSummary(path).print(expected)

    assert printed.getvalue() == expected.getvalue()
