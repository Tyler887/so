# from: https://github.com/pradyunsg/furo/blob/main/noxfile.py
# license: https://github.com/pradyunsg/furo/blob/main/LICENSE

"""Development automation
"""
import datetime
import glob
import os

import nox

PACKAGE_NAME = "furo"
nox.options.sessions = ["lint", "test"]

# fmt: off
assert (
    _determine_versions("2021.08.17.dev44", date=datetime.date(2021, 8, 17))
    == ("2021.08.17.44", "2021.08.17.dev45")
), "same day 1"
assert (
    _determine_versions("2021.08.17.dev1", date=datetime.date(2021, 8, 17))
    == ("2021.08.17.1", "2021.08.17.dev2")
), "same day 2"
assert (
    _determine_versions("2021.08.17.dev44", date=datetime.date(2021, 8, 18))
    == ("2021.08.18", "2021.08.18.dev1")
), "different day"
# fmt: on


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
