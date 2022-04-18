from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from ndnt.__main__ import main_with_args
from ndnt.paths import ExcludeGitignoredPaths, ExtensionPaths, FilesPaths
from ndnt.summary import DirectorySummary, FileSummary


def test_main_on_file():
    path = Path("tests/fake_folder/fake.py")

    printed = StringIO()
    with redirect_stdout(printed):
        main_with_args(path, no_gitignore=False, extension=".py")

    expected = StringIO()
    with redirect_stdout(expected):
        FileSummary(path).print()

    assert printed.getvalue() == expected.getvalue()


def test_main_on_directory_without_gitignore_option():
    path = Path("tests/fake_folder")

    printed = StringIO()
    with redirect_stdout(printed):
        main_with_args(path, no_gitignore=True, extension=".py")

    expected = StringIO()
    with redirect_stdout(expected):
        DirectorySummary(ExtensionPaths(FilesPaths(path), ".py")).print()

    assert printed.getvalue() == expected.getvalue()


def test_main_on_directory_with_gitignore_option():
    path = Path("tests/fake_folder")

    printed = StringIO()
    with redirect_stdout(printed):
        main_with_args(path, no_gitignore=False, extension=".py")

    expected = StringIO()
    with redirect_stdout(expected):
        DirectorySummary(
            ExtensionPaths(
                ExcludeGitignoredPaths(path, path / ".gitignore"),
                ".py",
            )
        ).print()

    assert printed.getvalue() == expected.getvalue()


def test_main_on_non_exists_path():
    path = Path("no/such/path")

    printed = StringIO()
    with redirect_stdout(printed):
        main_with_args(path, no_gitignore=False, extension=".py")

    assert printed.getvalue() == "Something is wrong with provided path.\n"
