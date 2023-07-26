
# example : !!gvote is jason a good person? yes no maybe

def parse(cmd: str) -> tuple:
    prompt = _get_prompt(cmd)
    opts = _get_options(cmd)
    return (prompt, opts)

def _get_prompt(cmd: str) -> str:
    # '!!gvote ' is 8 chars long so prompt index is @ 8.
    prompt_start = 8 
    # finds the last index of the ? which indicates the end of prompt
    # +1 to include the question mark.
    prompt_end = cmd.rfind('?') + 1
    return cmd[prompt_start:prompt_end]

def _get_options(cmd: str) -> list:
    # starting index after the last question mark assuming thats the prompt
    opt_string_start = cmd.rfind('?') + 1
    # a str from the last '?' chr to the end of the str
    option_string = cmd[opt_string_start::].strip(' ')
    # breaks the options up assuming they are spaced correctly
    options = option_string.split(' ')
    return options