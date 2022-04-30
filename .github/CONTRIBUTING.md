# Contributing to Ndnt

**Thank you very much for considering to contribute to this project!**

This document will help you to create
appropriate contribution.

## What can I contribute?

This types of contributions are welcome:

- Issues
- Pull Requests

## Creating Issues

### Issue title

Issue title is capitalized, short,
and starts with either adverb if issue
is question, or verb in all other cases.
For example: "How to use with fd?"
or "Shows incorrect total indentation".

### Issue type

You can create Issues of this main types:

- Bug report
- Feature request

### Pull Requests specific

This types of Issues used only
for creating related Pull Requests:

- Code improvement
- Docs improvement

## Creating Pull Requests

You need to follow this steps to create
appropriate Pull Request.

### Related Issue

First, before creating Pull Request, you need
to create Issue. You can see related Issue
types [in this section](#creating-issues).

### Commits style

Commits' titles are capitalized, short, and starts with verb.
For example: "Add section about inspecting more than one path"
or "Pin minimal python version".

In order to require this, commits needs to be concise,
and do only one action. For example, this commit is bad:
"Add contributing guides". You need to split this commit
into separate ones:

- "Add CONTRIBUTING file"
- "Add Issue templates"
- "Add Pull Requests templates"

### Code style

This project written in OOP-style. Follow this
paradigm while writing new code or rewrite existing one.

### Code requirements

First, install [dev requirements](requirements-dev.txt).

Lint your code with:

- black (use with `-l 79` option)
- flake8

Test your code with:

- pytest
- pytest-cov (`--cov ndnt tests`)

Your code not warns any lint warning.
Coverage stays at 100% after your changes.

### Changelog update

If your changes affects version bump,
you adds summary of your changes to
[CHANGELOG](CHANGELOG.md).

### Pull Request style

Your Pull Request's title is capitalized, short,
and starts with verb. For example: "Add support for regex extensions"
or "Allow to exclude files by extension".

Your Pull Request refers related issue.

You provide quick summary of your changes
in Pull Request body. If your changes contains
any complex logic you provides it in separate
section.
