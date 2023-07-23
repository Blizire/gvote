
# example : !!gvote is jason gay? yes no maybe

def parse(cmd: str) -> tuple:
    ''' 
    Gets the command the user puts in and returns the prompt and a 
    list of options to vote on.

    This function takes one str, 'cmd'. Returns a tuple (str, list(str)).

    Parameters:
        cmd (str): discord message prompting the bot

    Returns:
        tuple: (str, list(str))
    '''
    prompt = _get_prompt(cmd)
    opts = _get_options(cmd)
    return (prompt, opts)

def _get_prompt(cmd: str) -> str:
    ''' 
    Gets the command the user puts in and returns the question they asked.

    This function takes one str, 'cmd'. Returns a str of the prompt.

    Parameters:
        cmd (str): discord message prompting the bot

    Returns:
        str: The str of the prompt
    '''

    # '!!gvote ' is 8 chars long so prompt index is @ 8.
    prompt_start = 8 
    # finds the last index of the ? which indicates the end of prompt
    # +1 to include the question mark.
    prompt_end = cmd.rfind('?') + 1
    return cmd[prompt_start:prompt_end]

def _get_options(cmd: str) -> list:
    ''' 
    Gets the command the user puts in and returns the options a user can vote on.

    This function takes one str, 'cmd'. Returns a list of str.

    Parameters:
        cmd (str): discord message prompting the bot

    Returns:
        list: The list of str a user will vote on
    '''

    # starting index after the last question mark assuming thats the prompt
    opt_string_start = cmd.rfind('?') + 1
    # a str from the last '?' chr to the end of the str
    option_string = cmd[opt_string_start::].strip(' ')
    # breaks the options up assuming they are spaced correctly
    options = option_string.split(' ')
    return options