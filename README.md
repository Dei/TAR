### About
Simple Python 3.x script to make your Telegram Account auto-reply to any private message (it won't reply to group or bot messages).
Works with new incoming chats, unlike other similar scripts.

### Depencies
Install Telethon latest available version.
```
pip3 install telethon
```

### Usage
In order to use this script, you need `api_id` and `api_hash`, you can obtain them [here](https://my.telegram.org/auth?to=apps).

1. Replace `api_id` and `api_hash` to those you obtained. (Lines 6-7)
2. Replace `session` with your username. (Line 9, it will be created automatically)
3. Run `python3 main.py`, you'll be asked to enter your phone number. Enter it with + sign.
4. Authorize using code you'll receive either from Telegram in the Telegram App or in SMS.

You're good to go! 
Next time you'll launch the script, it will use SESSION file to login.
