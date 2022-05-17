from io import StringIO
from pathlib import Path

from ndnt.summary import DirectorySummary, FileSummary, FilesSummary


def test_file_summary():
    path = Path("tests/fake_folder/fake.py")
    summary = FileSummary(path)

    printed = StringIO()
    summary.print(printed)

    printed = printed.getvalue()
    assert str(path) in printed
    assert "3.33" in printed


def test_files_summary():
    folder = Path("tests/fake_folder")
    summary = FilesSummary([folder / "fake.py", folder / "ignored.py"])

    printed = StringIO()
    summary.print(printed)

    printed = printed.getvalue()
    assert "3.33" in printed


def test_directory_summary():
    folder = Path("tests/fake_folder")
    summary = DirectorySummary([folder / "fake.py", folder / "ignored.py"])

    printed = StringIO()
    summary.print(printed)

    printed = printed.getvalue()
    assert str(folder / "fake.py") in printed
    assert str(folder / "ignored.py") in printed
    assert printed.count("3.33") == 3
