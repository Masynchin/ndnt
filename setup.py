from pathlib import Path
from typing import List
from setuptools import find_packages, setup


CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
    """Get long description from README.md."""
    return (CURRENT_DIR / "README.md").read_text(encoding="u8")


def get_install_requires() -> List[str]:
    """Get duplicated requirements from requirements.txt."""
    return ["pathspec==0.9.0"]


setup(
    name="ndnt",
    version="1.2.0",
    description="Inspect indents of your files.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Masynchin/ndnt",
    author="Max Smirnov",
    author_email="masynchin@gmail.com",
    license="MIT",
    packages=find_packages(include=["ndnt"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",  # I am not sure about it
    install_requires=get_install_requires(),
    entry_points={
        "console_scripts": [
            "ndnt=ndnt.__main__:main",
        ]
    },
)
