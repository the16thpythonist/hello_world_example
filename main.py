"""
This text will be the short description of the plugin. The short
description will for example be displayed in the plugin list view of the web interface.
Make sure to write a short and concise description of the purpose of the plugin
the details can then be viewed in the specific README.html
"""
import sys

import click

# Plugins can obviously import from ufotest itself
from ufotest.hooks import Action, Filter
from ufotest.testing import AbstractTest, MessageTestResult

# Since the whole plugin system uses a lot of python dynamic import magic, importing
# from other modules within the same plugin IS POSSIBLE but has to be done as an
# absolute import, which uses the plugin name like this:
from hello_world_example.util import print_hello_world


# HELLO WORLD BEFORE EACH TEST
# ============================

@Action('pre_test', 10)
def pre_test(test_runner, name):
    print_hello_world()


# HELLO WORLD COMMAND
# ===================

@Filter('plugin_commands', 10)
def plugin_commands(value, config, context):

    @click.command('hello_world', help='Simply prints hello world')
    def hello_world():
        print_hello_world()

    value['hello_world'] = hello_world
    return value


# HELLO WORLD TEST CASE
# =====================

class HelloWorldTest(AbstractTest):

    name = 'hello_world'
    description = 'Adds a hello world test result message'

    def run(self):
        message = 'Hello World'
        exit_code = 0
        return MessageTestResult(exit_code, message)


@Filter('load_tests', 10)
def load_tests(value, test_runner):
    # "value" is a dict, where the string key is the unique string name
    # of the test case and the value is the AbstractTest object which
    # actually implements it
    value['hello_world'] = HelloWorldTest

    return value

