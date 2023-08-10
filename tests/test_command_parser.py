import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from gvote.command_parser import Command 

good_tests = []
bad_tests = []

# no leading space between question chr
good_tests.append(Command('!!gvote how do we know?yes no maybe',
                        'how do we know ?', 
                        ['yes', 'no', 'maybe']))
# extra spaces
good_tests.append(Command('!!gvote  are   we  blasting  ?    yes  no  maybe ',
                        'are we blasting ?',
                        ['yes', 'no', 'maybe']))
# extra question marks
good_tests.append(Command('!!gvote are we blasting? yes? no? maybe?',
                        'are we blasting ?',
                        ['yes?', 'no?', 'maybe?']))

# no question marks
bad_tests.append(Command('!!gvote how do we know yes no maybe',
                       None,
                       None))

# no options
bad_tests.append(Command('!!gvote how do we know?',
                       None,
                       None))

# only question marks
bad_tests.append(Command('!!gvote ? ? ?',
                       None,
                       None))

def test_parse():
    for data in good_tests:
        prompt, opts = Command(data.command).parse()
        assert prompt == data.prompt
        assert opts == data.options

def test_bad_parse():
    pass