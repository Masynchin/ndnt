from pathlib import Path

from ndnt.line import Line
from ndnt.lines import (
    LinesFromFiles,
    LinesFromText,
    LinesFromFile,
    CombinedLines,
    NonBlankLines,
)


def test_lines_from_text(code_text):
    lines = LinesFromText(code_text)
    assert list(lines) == [
        Line("def main(arg: int) -> int:"),
        Line("    if True:"),
        Line("        arg = 1"),
        Line("    return arg"),
        Line(""),
        Line(""),
        Line('if __name__ == "__main__":'),
        Line("    main()"),
    ]


def test_lines_from_file():
    lines_from_file = LinesFromFile(Path("tests/fake_folder/fake.py"))
    assert list(lines_from_file) == [
        Line("def main(arg: int) -> int:"),
        Line("    if True:"),
        Line("        arg = 1"),
        Line("    return arg"),
        Line(""),
        Line(""),
        Line('if __name__ == "__main__":'),
        Line("    main()"),
    ]


def test_non_blank_lines(code_text):
    non_blank_lines = NonBlankLines(LinesFromText(code_text))
    assert list(non_blank_lines) == [
        Line("def main(arg: int) -> int:"),
        Line("    if True:"),
        Line("        arg = 1"),
        Line("    return arg"),
        Line('if __name__ == "__main__":'),
        Line("    main()"),
    ]


def test_combined_lines(code_text):
    lines = LinesFromText(code_text)
    combined_lines = CombinedLines([lines, lines])
    assert list(combined_lines) == list(lines) * 2


def test_lines_from_files():
    folder = Path("tests/fake_folder")
    lines_from_files = LinesFromFiles(
        [folder / "fake.py", folder / "ignored.py"]
    )

    assert (
        list(lines_from_files)
        == [
            Line("def main(arg: int) -> int:"),
            Line("    if True:"),
            Line("        arg = 1"),
            Line("    return arg"),
            Line(""),
            Line(""),
            Line('if __name__ == "__main__":'),
            Line("    main()"),
        ]
        * 2
    )
