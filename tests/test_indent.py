from ndnt.line import Line
from ndnt.lines import LinesFromText, NonBlankLines
from ndnt.indent import AverageIndent, Indent, RoundedAverageIndent


def test_indent_spaces():
    indent = " " * 4
    assert Indent(Line(f"{indent}1 + 2")).value() == indent


def test_indent_tabs():
    indent = "\t\t"
    assert Indent(Line(f"{indent}1 + 2")).value() == indent


def test_indent_length_spaces():
    indent = " " * 4
    assert Indent(Line(f"{indent}1 + 2")).length() == 4


def test_indent_length_tabs():
    indent = "\t\t"
    assert Indent(Line(f"{indent}1 + 2")).length() == 8


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
