import nox


@nox.session(python=["3.9", "3.8", "3.7", "3.6", "pypy3"])
def tests(session):
    session.install(".", "-r", "requirements/tests.txt")
    session.run("pytest", *session.posargs)


@nox.session()
def style(session):
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session()
def docs(session):
    session.install(".", "-r", "requirements/docs.txt")
    session.run("sphinx-build", "-M", "clean", "docs", "docs/_build")
    session.run("sphinx-build", "-M", "html", "docs", "docs/_build", "-W")
