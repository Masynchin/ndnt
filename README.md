# ndnt

The tool that helps you inspect indents of your files.

## Installation

You can install it via:

~~~bash
pip install ndnt
~~~

## Usage

Main command is:

~~~bash
ndnt <path>
~~~

You can get help about its arguments and options with:

~~~bash

ndnt -h
~~~

Examples of usage:

~~~bash
# ndnt setup.py
3.43  | setup.py

# ndnt .
5.6   | ndnt\indent.py
3     | ndnt\line.py
4.19  | ndnt\lines.py
5.65  | ndnt\paths.py
4.47  | ndnt\summary.py
0.0   | ndnt\__init__.py
4.41  | ndnt\__main__.py
3.43  | setup.py
2     | tests\conftest.py
3.33  | tests\fake_folder\fake.py
3.33  | tests\fake_folder\ignored.py
4     | tests\test_main.py
2.77  | tests\test_ndnt\test_indent.py
6.06  | tests\test_ndnt\test_lines.py
3.56  | tests\test_ndnt\test_paths.py
3.48  | tests\test_ndnt\test_summary.py
0.0   | tests\__init__.py
-------------
4.52  | Total
~~~

By default it includes .gitignore file but you can disable it
via `--no-gitignore` flag.
