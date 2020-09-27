Bot for the [University of Bayes](https://discord.gg/x7ak6gu)

Features
===
- Anonymous messages in #feedback via either "plz feedback 'your message'" or DMing your feedback. A channel can also be specified at the beginning: "plz feedback general Heyo everyone"

Todo-list
===
- Decaying bayes points
- Quadratic voting
- Make a more illustrated README

How to join as a dev
===
Come in this server: [University of Bayes' bot](https://discord.gg/f9NsZQu)
If you want me ( ^,^#3752 ) or anyone who wants to setup the bot for you and run you quickly through the instruction, feel free to ping. Otherwise, here are the instructions:

Creating your own discord bot
---
First, you need to create your own bot instance. This will insure that you're able to test it even if others are too. To create your own discord bot:

- [Go there](https://discord.com/developers/applications) and create your own application
- Then go to "bots" and click on create bot
- Copy the token under "Username", this will be important
- Then go to "OAuth2" and select bot, then administrator
- Follow the generated link, and you should be able to add the bot to the University 

Running the bot
---
- Either clone the source or download them as a zip
- Before running the bot, you need to fill .env with the following values:
    * token=[the token from last steps]
    * authorized\_ids=[your own discord id. If you don't know it, you can just type ``plz id`` in the server]
- Then cd into the source folder
- Install the dependencies with ``pip install -r requirements.txt``
- And run the bot with ``python .``

If everything goes well, you should see your bot come online on the server and your terminal should display its credential.
Congratulations! Now, you just need to start some code ;)

Coding
---
To start a new feature, create a new file with its own cog. See example.py for a very simple template.
Let your bot run as you program, and when everything seems good and you've saved them run:
```
plz load [name of your file without .py]
```
So for example.py this would be ``plz load example``

When already loaded, you can just do ``plz load`` to reload all modules, and ``plz clear`` to stop the autoreloading

To test your own commands, use
```
plz run [command]
```
Again, for example.py, this would be ``plz run hello``. You can just do ``plz run`` if you've already specified the command.
This will automatically reload your files and run the command, displaying in the discord any errors you'd have.

Guidelines
---
Please use config as often as possible, putting it in .env.default if it should be public and in .env if it should be hidden
Parsers and cogs also makes the code easier to read

Pushing
---
Once you're done, you can just either send it as a file, or make a PR.
This project is very new, so this is not yet very formalized.
