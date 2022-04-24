from ndnt.extension import AnyProgrammingExtension, ExactExtension


def test_exact_equal():
    assert ExactExtension(".py") == ".py"


def test_exact_unequal():
    assert ExactExtension(".py") != ".rb"


def test_any_equal():
    assert AnyProgrammingExtension() == ".py"
    assert AnyProgrammingExtension() == ".go"
    assert AnyProgrammingExtension() == ".ex"


def test_any_unequal():
    assert AnyProgrammingExtension() != ".txt"
    assert AnyProgrammingExtension() != ".png"
    assert AnyProgrammingExtension() != ".mp4"
