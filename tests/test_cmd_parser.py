import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import gvote.cmd_parser

class Test_Data:
    def __init__(self, command, prompt=None, options=None) -> None:
        self.command = command
        self.prompt = prompt
        self.options = options

good_tests = []
bad_tests = []

# no leading space between question chr
good_tests.append(Test_Data('!!gvote how do we know?yes no maybe',
                        'how do we know?', 
                        ['yes', 'no', 'maybe']))
# extra spaces
good_tests.append(Test_Data('!!gvote  are   we  blasting  ?    yes  no  maybe ',
                        'are we blasting?',
                        ['yes', 'no', 'maybe']))
# extra question marks
good_tests.append(Test_Data('!!gvote are we blasting? yes? no? maybe?',
                        'are we blasting?',
                        ['yes?', 'no?', 'maybe?']))

# no question marks
bad_tests.append(Test_Data('!!gvote how do we know yes no maybe',
                       None,
                       None))

# no options
bad_tests.append(Test_Data('!!gvote how do we know?',
                       None,
                       None))

# only question marks
bad_tests.append(Test_Data('!!gvote ? ? ?',
                       None,
                       None))

def test_parse():
    for data in good_tests:
        prompt, opts = gvote.cmd_parser.parse(data.command)
        assert prompt == data.prompt
        assert opts == data.options

def test_bad_parse():
    pass