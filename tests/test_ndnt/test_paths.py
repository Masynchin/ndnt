from pathlib import Path
from ndnt.paths import ExcludeGitignoredPaths, FilesPaths, PythonPaths


def test_files_paths():
    folder = Path("tests/fake_folder")
    files_paths = FilesPaths(folder)
    assert set(files_paths) == {
        folder / "fake.py",
        folder / "ignored.py",
        folder / ".gitignore",
    }


def test_python_paths():
    folder = Path("tests/fake_folder")
    python_paths = PythonPaths(FilesPaths(folder))
    assert set(python_paths) == {folder / "fake.py", folder / "ignored.py"}


def test_exclude_gitignored_paths():
    folder = Path("tests/fake_folder")
    paths = ExcludeGitignoredPaths(folder, folder / ".gitignore")
    assert set(paths) == {folder / "fake.py", folder / ".gitignore"}
