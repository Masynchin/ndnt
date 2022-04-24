from contextlib import redirect_stdout
from io import StringIO

from ndnt.__main__ import main
from ndnt.arguments import CliArguments
from ndnt.cli import Cli
from ndnt.ndnt import Ndnts


def test_main():
    printed = StringIO()
    with redirect_stdout(printed):
        main(arguments=["tests/fake_folder/fake.py"])

    expected = StringIO()
    with redirect_stdout(expected):
        Ndnts(CliArguments(["tests/fake_folder/fake.py"], Cli())).run()

    assert printed.getvalue() == expected.getvalue()
