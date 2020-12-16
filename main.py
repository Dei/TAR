#!/usr/bin/env python3

from telethon import TelegramClient, events

api_id = 123
api_hash = 'abc'
session = 'username'

# Customize your message
msg = '[Auto-Reply] Sorry, I am unavailable until February 15th.'

client = TelegramClient(session, api_id, api_hash, sequential_updates=True)

@client.on(events.NewMessage(incoming=True, blacklist_chats=True))
async def h_NewMessage(event):
	await client.get_dialogs(limit=2, ignore_pinned=True)
	from_ = await event.client.get_entity(event.from_id)
	if not from_.bot and not from_.is_self and event.is_private:
		await event.respond(msg)

print('Auto-replying now..')
client.start()
client.run_until_disconnected()
print('Auto-replying was stopped.')