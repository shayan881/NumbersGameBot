from pyrogram import Client

plugins = dict(
    root='plugins'
)

app = Client("BotNumber",
api_id=None,   # Example 2227374
api_hash=None, # Example 'ec3bd8784ba9471 .....'
bot_token=None,# Example '808501:AAFFCVww9E .....'
plugins=plugins)

if __name__ == '__main__':
    app.run()
