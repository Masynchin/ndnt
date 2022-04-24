import sys
from typing import Sequence

from ndnt.arguments import CliArguments
from ndnt.cli import Cli
from ndnt.ndnt import Ndnts


def main(arguments: Sequence[str] = sys.argv[1:]):
    Ndnts(CliArguments(arguments, Cli())).run()
