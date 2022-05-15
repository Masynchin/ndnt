import pytest


CODE_TEXT = """
def main(arg: int) -> int:
    if True:
        arg = 1
    return arg


if __name__ == "__main__":
    main()
""".lstrip()


@pytest.fixture
def code_text():
    return CODE_TEXT
