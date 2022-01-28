from itertools import takewhile
from statistics import mean, StatisticsError

from ndnt.line import Line
from ndnt.lines import Lines


class Indent:
    """Line's indent."""

    def __init__(self, origin: Line):
        self.origin = origin

    def value(self) -> str:
        """Indent itself."""
        return "".join(takewhile(str.isspace, self.origin))

    def length(self) -> int:
        """Length of indent in spaces.

        Each tab counts as 4 spaces.
        """
        return len(self.value().replace("\t", " " * 4))


class AverageIndent:
    """Average indent of lines block."""

    def __init__(self, origin: Lines):
        self.origin = origin

    def value(self) -> float:
        """Average indent itself."""
        indents = map(Indent, self.origin)
        try:
            return mean(indent.length() for indent in indents)
        except StatisticsError:
            # if origin has no lines
            return 0.0


class RoundedAverageIndent:
    """Rounded `AverageIndent`."""

    def __init__(self, origin: AverageIndent):
        self.origin = origin

    def value(self) -> float:
        """Rounded average indent itself."""
        return round(self.origin.value(), ndigits=2)
