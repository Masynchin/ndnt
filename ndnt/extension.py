from abc import ABC, abstractmethod


class Extension(ABC):
    """Extension interface.

    Extension of file that can be compared with string.
    """

    @abstractmethod
    def __eq__(self, other: str) -> bool: ...


class AnyProgrammingExtension(Extension):
    """Extension of any programming languages."""

    def __init__(self):
        self.extensions = {
            ".adb",
            ".agda",
            ".bal",
            ".c",
            ".cc",
            ".ceylon",
            ".cpp",
            ".dart",
            ".elm",
            ".ex",
            ".fs",
            ".go",
            ".hs",
            ".idr",
            ".java",
            ".js",
            ".jsx",
            ".kt",
            ".lua",
            ".ma",
            ".ml",
            ".nim",
            ".opa",
            ".py",
            ".purs",
            ".qs",
            ".rb",
            ".rs",
            ".swift",
            ".svelte",
            ".ts",
            ".tsx",
            ".uc",
            ".uno",
            ".v",
            ".vue",
            ".wl",
            ".xm",
            ".y",
            ".zig",
        }

    def __eq__(self, other: str) -> bool:
        return other in self.extensions


class ExactExtension(Extension):
    """Exact extension."""

    def __init__(self, extension: str):
        self.extension = extension

    def __eq__(self, other: str) -> bool:
        return other == self.extension
