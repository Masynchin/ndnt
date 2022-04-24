from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from ndnt.ndnt import Ndnt
from ndnt.paths import ExcludeGitignoredPaths, ExtensionPaths, FilesPaths
from ndnt.summary import DirectorySummary, FileSummary


def test_on_file():
    path = Path("tests/fake_folder/fake.py")

    printed = StringIO()
    with redirect_stdout(printed):
        Ndnt(path, ".py", no_gitignore=False).run()

    expected = StringIO()
    with redirect_stdout(expected):
        FileSummary(path).print()

    assert printed.getvalue() == expected.getvalue()


def test_on_directory_without_gitignore_option():
    path = Path("tests/fake_folder")

    printed = StringIO()
    with redirect_stdout(printed):
        Ndnt(path, ".py", no_gitignore=True).run()

    expected = StringIO()
    with redirect_stdout(expected):
        DirectorySummary(ExtensionPaths(FilesPaths(path), ".py")).print()

    assert printed.getvalue() == expected.getvalue()


def test_on_directory_with_gitignore_option():
    path = Path("tests/fake_folder")

    printed = StringIO()
    with redirect_stdout(printed):
        Ndnt(path, ".py", no_gitignore=False).run()

    expected = StringIO()
    with redirect_stdout(expected):
        DirectorySummary(
            ExtensionPaths(
                ExcludeGitignoredPaths(path, path / ".gitignore"),
                ".py",
            )
        ).print()

    assert printed.getvalue() == expected.getvalue()


def test_on_non_exists_path():
    path = Path("no/such/path")

    printed = StringIO()
    with redirect_stdout(printed):
        Ndnt(path, ".py", no_gitignore=False).run()

    assert printed.getvalue() == "Something is wrong with provided path.\n"
