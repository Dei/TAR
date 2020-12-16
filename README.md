### About
Simple Python 3.x script to make your Telegram Account auto-reply to any private message.
Works with new incoming chats, unlike other similar scripts.

### Depencies
Install Telethon latest available version.
```
pip3 install telethon
```

### Usage
In order to use this script, you need `api_id` and `api_hash`, you can obtain them here: https://my.telegram.org/auth?to=apps

1. Replace `api_id` and `api_hash` to those you obtained. (Lines 6-7)
2. Replace `session` with path to your SESSION file. (Line 9, it will be created automatically)

Run `python3 main.py` and enter your Phone Number using international format, (example: `+123456789`), then follow the displayed instructions. You'll have to authorize only once until you delete or move your SESSION file.
