import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from gvote.command_parser import Command, CommandParseError

good_tests = []

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

# In hindsight this is actually a bad way to test. Should've been individual tests for each case.
def test_parse():
    for data in good_tests:
        prompt, opts = Command(data.command).parse()
        assert prompt == data.prompt
        assert opts == data.options


def test_no_question_marks():
        ''' test handling for no question marks '''
        with pytest.raises(CommandParseError) as e:
            prompt, opts = Command('!!gvote how do we know yes no maybe').parse()

        assert str(e.value) == "Could not find the end of prompt."

def test_prompt_with_no_options():
        ''' test handling for a prompt with no options '''
        with pytest.raises(CommandParseError) as e:
            prompt, opts = Command('!!gvote how do we know?').parse()

        assert str(e.value) == "Could not find options to parse after prompt."

def test_prompt_with_only_question_marks():
        ''' test handling for a prompt with only question marks '''
        with pytest.raises(CommandParseError) as e:
            prompt, opts = Command('!!gvote ? ? ?').parse()

        assert str(e.value) == "Invalid prompt."