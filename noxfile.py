# from: https://github.com/pradyunsg/furo/blob/main/noxfile.py
# license: https://github.com/pradyunsg/furo/blob/main/LICENSE

"""Development automation
"""
import datetime
import glob
import os

import nox

#
# Development Sessions
#
@nox.session(reuse_venv=True)
def docs(session):
    session.install("-r", "docs/requirements.txt")
    session.install(".")

    # Generate documentation into `build/docs`
    session.run("sphinx-build", "-b", "dirhtml", "-v", "docs/", "build/docs")


@nox.session(name="docs-live", reuse_venv=True)
def docs_live(session):
    session.install("-r", "docs/requirements.txt")
    session.install("-e", ".", "sphinx-theme-builder[cli]")

    # Generate documentation into `build/docs`
    session.run("stb", "serve", "docs/")


@nox.session(reuse_venv=True)
def lint(session):
    session.install("pre-commit")

    args = list(session.posargs)
    args.append("--all-files")
    if "CI" in os.environ:
        args.append("--show-diff-on-failure")

    session.run("pre-commit", "run", *args)
