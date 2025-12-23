# YuriBot
A simple bot that crawls safebooru and posts yuri to Bluesky!
Created stupidly by [@turnthefrigginfrogs.gay](https://bsky.app/profile/turnthefrigginfrogs.gay)

Help support @turnthefrigginfrogs.gay! Buy me a Strawberry: https://buymeacoffee.com/rosedabun

# Setting this up yourself!
1. Clone this repository! `git clone https://github.com/turnthefrigginfrogsgay/YuriBot.git`
2. Move to the repository! `cd YuriBot`
3. Download the dependancies! `pip install -r requirements.txt`
    1. If your OS requires you to use a venv, easily make one by running `python -m venv venv`
    2. Then run `source venv/bin/activate`
    3. Now try the command again: `pip install -r requirements.txt`
4. Copy the `secrets.example.py` to be `secrets.py`: `cp secrets.example.py secrets.py`
5. Fill in your username and password in the `secrets.py`
6. Run the bot using `python main.py`
    1. If you want to run it out of schedule, like for testing, run `python specialRun.py`

# License
YuriBot uses GNU AGPL3!
