#!/usr/bin/python
from distutils.core import setup, Command
from unittest import TextTestRunner, TestLoader
from glob import glob
from os.path import splitext, basename, join as pjoin
import os

class TestCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        self._dir = os.getcwd()

    def finalize_options(self):
        pass

    def run(self):
        '''
        Finds all the tests modules in tests/, and runs them.
        '''
        testfiles = [ ]
        for t in glob(pjoin(self._dir, 'tests', '*.py')):
            if not t.endswith('__init__.py'):
                testfiles.append('.'.join(
                    ['tests', splitext(basename(t))[0]])
                )

        tests = TestLoader().loadTestsFromNames(testfiles)
        t = TextTestRunner(verbosity = 4)
        t.run(tests)

setup(name='pkcs1',
        version='0.1',
        license='MIT',
        description='Python implementation of the RFC3447 or PKCS #1 version 2.0',
        url='https://github.com/bdauvergne/python-pkcs1',
        author='Benjamin Dauvergne',
        author_email='bdauvergne@entrouvert.com',
        packages=['pkcs1'],
        cmdclass={'test': TestCommand})