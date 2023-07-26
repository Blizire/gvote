import pytest
from gvote import cmd_parser

class Test_Data:
    def __init__(self, command, prompt=None, options=None) -> None:
        self.command = command
        self.prompt = prompt
        self.options = options

good_tests = []
bad_tests = []

# no leading space between question chr
good_tests += Test_Data('!!gvote how do we know?yes no maybe',
                        'how do we know?', 
                        ['yes', 'no', 'maybe'])
# extra spaces
good_tests += Test_Data('!!gvote  are   we  blasting  ?    yes  no  maybe ',
                        'are we blasting?',
                        ['yes', 'no', 'maybe'])
# extra question marks
good_tests += Test_Data('!!gvote are we blasting? yes? no? maybe?',
                        'are we blasting?',
                        ['yes?', 'no?', 'maybe?'])

# no question marks
bad_tests += Test_Data('!!gvote how do we know yes no maybe',
                       None,
                       None)

# no options
bad_tests += Test_Data('!!gvote how do we know?',
                       None,
                       None)

# only question marks
bad_tests += Test_Data('!!gvote ? ? ?',
                       None,
                       None)

def test_get_prompt():
    pass

def test_get_options():
    pass

def test_parse():
    pass