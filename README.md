# ndnt

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

Here is how you inspect indentation of all current directory programming files:

~~~shell
ndnt
~~~

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

### Exact extension

If you want to get information about files with specific extension
you can use `-e` (or `--extension`) option:

~~~shell
ndnt . -e .py 
~~~

### Ignored

By default it includes .gitignore file but you can disable it
via `--no-gitignore` flag, for example:

~~~shell
ndnt . -e .py --no-gitignore
~~~
