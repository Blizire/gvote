# gvote
discord poll-bot

# usage
Inside **token.cfg** input your bot token

In root folder run the bot using this command: 

```python3 gvote```

Once the bot is running it is listening for the **!!gvote** command prefix
ex: **!!gvote What is the best flavor of ice cream? Vanilla Chocolate Strawberry**

Everything up to the first question mark is the question that will be displayed for the poll.
After the first question mark the choices for the poll are seperated by spaces.

After you type this a message will be placed onto the discord server with emojis as buttons
for users to select their choices.

# installation
```python3 -m pip install -r ./requirements.txt```

# testing
run ```pytest -v``` in the root directory.

