from ndnt.lines import LinesFromText, NonBlankLines
from ndnt.indent import AverageIndent, RoundedAverageIndent


def test_average_indent(code_text):
    average_indent = AverageIndent(NonBlankLines(LinesFromText(code_text)))
    assert average_indent.value() == 20 / 6


def test_average_indent_on_zero_lines():
    average_indent = AverageIndent([])
    assert average_indent.value() == 0.0


def test_rounded_average_indent(code_text):
    rounded_average_indent = RoundedAverageIndent(
        AverageIndent(NonBlankLines(LinesFromText(code_text)))
    )
    assert rounded_average_indent.value() == round(20 / 6, ndigits=2)
