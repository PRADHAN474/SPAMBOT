import asyncio

from random import choice

from telethon import events

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltBots.data import RAID, REPLYRAID, OXYGEN


REPLY_RAID = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in OXYGEN:
                await e.reply("REPO OWNER HAI YE.")
            elif uid == OWNER_ID:
                await e.reply("BETA BAAP PE RAID NHI KRTE HAI...")
            elif uid in SUDO_USERS:
                await e.reply("ISPE RAID MAT MARO.. !!...")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐚𝐢𝐝\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in OXYGEN:
                await e.reply("REPO OWNER HAI YE.")
            elif user_id == OWNER_ID:
                await e.reply("BETA BAAP PE RAID NHI KRTE HAI....")
            elif user_id in SUDO_USERS:
                await e.reply("= ISPE RAID MAT MARO.. !!...")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» LAG GYA REPLY RAID.. !! ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» HAT GYA REPLY RAID !! ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
