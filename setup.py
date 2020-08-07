# -*- encoding : utf-8 -*-

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main([".", "-v"])
        sys.exit(errno)


setup(
    name="pyshor",
    version="0.0.1",
    author="Quentin Delamea",
    license="MIT",
    test_suite="tests",
    install_requires=[
        'qat-core',
        'qat-lang',
        'myqlm-simulators',
        'numpy'
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
