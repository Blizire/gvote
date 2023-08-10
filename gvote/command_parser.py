class Command:
    def __init__(self, command, prompt=None, options=None) -> None:
        self.command = command
        self.prompt = prompt 
        self.options = options

    def parse(self) -> tuple:
        ''' wrapper to run methods prompt and options. returns the text from users prompt 
        and the text users should be able to select'''
        if self.command is None:
            return None
        self.prompt = self._get_prompt(self.command)
        self.options = self._get_options(self.command)

        if self.prompt == None or self.options == None:
            raise CommandParseError("Could not parse one of the paramters.")

        return (self.prompt, self.options)

    def _get_prompt(self, cmd: str) -> str:
        ''' Obtains the text between '!!gvote ' and the first question mark '''

        prompt_start = 8 # '!!gvote ' is 8 chars long ( include space )

        # finds the last index of the ? which indicates the end of prompt
        # +1 to include the question mark.
        prompt_end = cmd.find('?') + 1

        # if theres no questeion mark then the end will be 0 before the start
        if prompt_end <= prompt_start:
            raise CommandParseError("Could not find the end of prompt.")
        
        # if the start and end is 1 then its just a question mark.
        if (prompt_end - prompt_start) <= 1:
            raise CommandParseError("Invalid prompt.")

        prompt = cmd[prompt_start:prompt_end]

        # ensure no extra spaces are in it
        prompt = prompt.split()
        prompt = ' '.join(prompt)

        # ensure space between last word and question mark
        if prompt[-2] != ' ':
            prompt = prompt[:-1] + ' ?'    
        return prompt

    def _get_options(self, cmd: str) -> list:
        ''' recieves a 'cmd' and we parse it after the 'prompt' and get the 'options' afterwards, each
        option will be seperated by spaces '''
        
        # first index after finding the first question mark
        opt_string_start = cmd.find('?') + 1

        # check if theres any input ( no options after )
        if opt_string_start >= len(cmd):
            raise CommandParseError("Could not find options to parse after prompt.")

        # a str from the last '?' chr to the end of the str
        option_string = cmd[opt_string_start::].strip()

        # breaks the options up assuming they are spaced correctly
        options = option_string.split()

        # removes any extra spaces that may have been inputed
        for i,opt in enumerate(options):
            if opt == ' ':
                options[i].remove()

        return options
    
class CommandParseError(Exception):
    pass

if __name__ == '__main__':
    prompt, options = Command('!!gvote ?').parse()
    print(prompt)
    print(options)