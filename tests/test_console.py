#!/usr/bin/python3
''' Unittest Console '''
import os
import unittest
import sys
import pep8
from console import HBNBCommand
from unittest.mock import create_autospec


class TestConsole(unittest.TestCase):
    ''' testing console '''

    @classmethod
    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def create(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['./console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        ''' test all method '''
        cli = self.create()
        self.assertFalse(cli.onecmd("all"))
        self.assertFalse(cli.onecmd("all User"))
        self.mock_stdout.reset_mock()

    def test_show(self):
        ''' test show method '''
        cli = self.create()
        self.assertFalse(cli.onecmd("show"))
        self.assertFalse(cli.onecmd("show User"))
        self.mock_stdout.reset_mock()

    def test_help(self):
        ''' test show method '''
        cli = self.create()
        self.assertFalse(cli.onecmd("help"))
        self.assertFalse(cli.onecmd("help show"))
        self.mock_stdout.reset_mock()

    def test_quit(self):
        ''' test quit command '''
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))
