import pytest


CODE_TEXT = """
def main(arg: int) -> int:
    return (
        arg + arg + arg
    )


if __name__ == "__main__":
    main()
""".lstrip()


@pytest.fixture
def code_text():
    return CODE_TEXT
