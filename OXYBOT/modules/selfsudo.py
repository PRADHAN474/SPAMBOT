import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from config import SUDO_USERS
from os import execl, getenv
from telethon import events
from datetime import datetime

@X1.on(events.NewMessage(pattern=r"sudo", incoming=True))
@X2.on(events.NewMessage(pattern=r"sudo", incoming=True))
@X3.on(events.NewMessage(pattern=r"sudo", incoming=True))
@X4.on(events.NewMessage(pattern=r"sudo", incoming=True))
@X5.on(events.NewMessage(pattern=r"sudo", incoming=True))
@X6.on(events.NewMessage(pattern=r"sudo", incoming=True))
@X7.on(events.NewMessage(pattern=r"sudo", incoming=True))
@X8.on(events.NewMessage(pattern=r"sudo", incoming=True))
@X9.on(events.NewMessage(pattern=r"sudo", incoming=True))
@X10.on(events.NewMessage(pattern=r"sudo", incoming=True))
async def add_sudo_user(event):
    if event.is_private:
        await event.reply("You can't use this command in private chats.")
    else:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"Adding you as a sudo user...")
        target = event.sender_id
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("Please set up your HEROKU_APP_NAME")
            return
        heroku_var = app.config()
        if event is None:
            return
        if str(target) in sudousers:
            await ok.edit("You are already a sudo user.")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit("You have been added as a sudo user. Bot is restarting...")
            heroku_var["SUDO_USERS"] = newsudo
            execl(sys.executable, sys.executable, *sys.argv)

