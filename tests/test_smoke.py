"""Smoke test: proves the package is installed and the test tooling works."""

import manpage_rag


def test_package_imports() -> None:
    assert manpage_rag.__doc__ is not None
