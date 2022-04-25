from pathlib import Path

from ndnt.arguments import CliArguments
from ndnt.cli import Cli
from ndnt.extension import AnyProgrammingExtension, ExactExtension


def test_defaults():
    arguments = CliArguments([], Cli())

    assert arguments.paths() == [Path()]
    assert isinstance(arguments.extension(), AnyProgrammingExtension)
    assert arguments.no_gitignore() == False


def test_multiple_paths():
    arguments = CliArguments(["py.py", "go.go"], Cli())

    assert arguments.paths() == [Path("py.py"), Path("go.go")]


def test_exact_extension():
    arguments = CliArguments(["-e", ".py"], Cli())

    assert isinstance(arguments.extension(), ExactExtension)


def test_no_gitignore():
    arguments = CliArguments(["--no-gitignore"], Cli())

    assert arguments.no_gitignore() == True
