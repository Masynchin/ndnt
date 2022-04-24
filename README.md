# ndnt

[![PyPI](https://img.shields.io/pypi/v/ndnt.svg?label=PyPI)](https://pypi.org/project/ndnt/)
[![Test](https://github.com/Masynchin/ndnt/workflows/Test/badge.svg?even=push&branch=main)](https://github.com/Masynchin/ndnt/actions?query=workflow%3ATest+event%3Apush+branch%3Amain)
[![Coverage](https://codecov.io/gh/Masynchin/ndnt/branch/main/graph/badge.svg?token=D7SNYW4HAQ)](https://codecov.io/gh/Masynchin/ndnt)

The tool that helps you inspect indents of your files.

## Installation

You can install it via:

~~~shell
pip install ndnt
~~~

## Usage

To get list of all available options run one of following:

~~~shell
ndnt -h
ndnt --help
~~~

### Basic

Here is how you can inspect indentation of all current directory
programming files:

~~~shell
ndnt
~~~

By default `ndnt` searches for files of any programming languages.
It includes many popular languages, but if your language doesn't supported
please, create issue.

If you want to inspect specific file or directory you can do it like this:

~~~shell
> ndnt setup.py
3.43  | setup.py

> ndnt .
5.64  | cronjobs/cronjobs.py
0     | extension/popup.js
5.99  | extension/colors.js
9.24  | extension/content.js
0.67  | frontend/babel.config.js
3.6   | frontend/vue.config.js
5.16  | frontend/src/index/App.vue
0.52  | frontend/src/index/main.js
5.24  | frontend/src/index/views/Home.vue
4.65  | frontend/src/index/views/Favorites.vue
6.84  | frontend/src/login/App.vue
0.2   | frontend/src/login/main.js
0     | gunicorn.conf.py
4.99  | app.py
8.21  | jobs/jobs.py
-------------
5.95  | Total
~~~

### Many paths

You can inspect more than one path at the same time:

~~~shell
> ndnt ndnt/paths.py tests/test_paths.py
5.76  | ndnt/paths.py
4.97  | tests/test_paths.py
~~~

Ndnt can accept output from other commands,
like [fd](https://github.com/sharkdp/fd)
or [rg](https://github.com/BurntSushi/ripgrep):

~~~shell
> fd paths | xargs ndnt
5.76  | ndnt/paths.py
4.97  | tests/test_paths.py
~~~

### Exact extension

If you want to get information about files with specific extension
you can use `-e` (or `--extension`) option:

~~~shell
ndnt -e .py 
~~~

### Ignored

By default `ndnt` reads .gitignore file but you can disable it
with `--no-gitignore` flag, for example:

~~~shell
ndnt -e .py --no-gitignore
~~~
