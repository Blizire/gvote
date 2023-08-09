
# example : !!gvote is jason a good person? yes no maybe

def parse(cmd: str) -> tuple:
    prompt = _get_prompt(cmd)
    opts = _get_options(cmd)
    return (prompt, opts)

def _get_prompt(cmd: str) -> str:
    ''' Obtains the text between '!!gvote ' and the first question mark '''

    # '!!gvote ' is 8 chars long so prompt index is @ 8.
    prompt_start = 8 
    # finds the last index of the ? which indicates the end of prompt
    # +1 to include the question mark.
    prompt_end = cmd.find('?') + 1
    prompt = cmd[prompt_start:prompt_end]
    # ensure no extra spaces are in it
    prompt = prompt.split()
    prompt = ' '.join(prompt)
    # ensure space between last word and question mark
    if prompt[-2] != ' ':
        prompt = prompt[:-1] + ' ?'    
    return prompt

def _get_options(cmd: str) -> list:
    ''' recieves a 'cmd' and we parse it after the 'prompt' and get the 'options' afterwards, each
     option will be seperated by spaces '''
    
    # assumes prompt is correct and has one question mark so after the first question mark
    # will be the listed options seperated by spaces. we split the spaces and return those options.
    opt_string_start = cmd.find('?') + 1
    # a str from the last '?' chr to the end of the str
    option_string = cmd[opt_string_start::].strip()
    # breaks the options up assuming they are spaced correctly
    options = option_string.split()
    # removes any extra spaces that may have been inputed
    for i,opt in enumerate(options):
        if opt == ' ':
            options[i].remove()

    return options

if __name__ == '__main__':
    s = '!!gvote are we blasting? yes? no? maybe?'
    resp = _get_prompt(s)
    resp = _get_options(s)
    print(resp)