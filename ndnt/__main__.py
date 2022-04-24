import sys

from ndnt.arguments import CliArguments
from ndnt.cli import Cli
from ndnt.ndnt import Ndnts


def main():
    Ndnts(CliArguments(sys.argv[1:], Cli())).run()
