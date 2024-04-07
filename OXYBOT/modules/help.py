from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"˹𝕆𝕩𝕪𝕘𝕖𝕟 ꭙ 𝕊𝕡𝕒𝕞˼🫧 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n\n» **𝐂𝐋𝐈𝐂𝐊 𝐎𝐍 𝐁𝐔𝐓𝐓𝐎𝐍 𝐅𝐎𝐑 𝐇𝐄𝐋𝐏**\n» **𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥: ˹𝕆𝕩𝕪𝕘𝕖𝕟 ꭙ 𝕊𝕡𝕒𝕞˼🫧**"

HELP_BUTTON = [
    [
      Button.inline("★𝗦𝗣𝗔𝗠★", data="spam"),
      Button.inline("★𝗥𝗔𝗜𝗗★", data="raid")
    ],
    [
      Button.inline("★𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦★", data="extra")
    ],
    [
      Button.url("★𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥★", "https://t.me/naksh_vai"),
      Button.url("★𝗦𝗨𝗣𝗣𝗢𝗥𝗧★", "https://t.me/naksh_accounts")
    ],
  [   
      Button.inline("★𝗡𝗘𝗪 𝗖𝗢𝗠𝗠𝗔𝗡𝗗★", data="naksh")
      
  ]
]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://telegra.ph/file/8b9b389d2389201ee4d6b.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**»💘 𝐄𝐗𝐓𝐑𝐀 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 💘:**

💘 𝐔𝐒𝐄𝐑 𝐁𝐎𝐓💘: **💘𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐂𝐌𝐃𝐒💘**
  1) {hl}𝐏𝐈𝐍𝐆
  2) {hl}𝐑𝐄𝐁𝐎𝐎𝐓
  3) {hl}𝐒𝐔𝐃𝐎 <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑>  --> 𝐎𝐖𝐍𝐄𝐑 𝐂𝐌𝐃
  4) {hl}𝐋𝐎𝐆𝐒--> 𝐎𝐖𝐍𝐄𝐑 𝐂𝐌𝐃

💘 𝐄𝐂𝐇𝐎: **💘𝐓𝐎 𝐀𝐂𝐓𝐈𝐕𝐄 𝐄𝐂𝐇𝐎 𝐎𝐍 𝐀𝐍𝐘 𝐔𝐒𝐄𝐑 💘**
  1) {hl}𝐄𝐂𝐇𝐎 <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >
  2) {hl}𝐑𝐌𝐄𝐂𝐇𝐎 <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

💘 𝐋𝐄𝐀𝐕𝐄: **💘𝐓𝐎 𝐋𝐄𝐀𝐕𝐄 𝐆𝐑𝐎𝐔𝐏 / 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 💘**
  1) {hl}𝐋𝐄𝐀𝐕𝐄 <𝐆𝐑𝐎𝐔𝐏/𝐂𝐇𝐀𝐓 𝐈𝐃>
  2) {hl} 𝐋𝐄𝐀𝐕𝐄 : 𝐓𝐘𝐏𝐄 𝐈𝐍 𝐓𝐇𝐄𝐈𝐑 𝐆𝐑𝐎𝐔𝐏 𝐁𝐎𝐓 𝐖𝐈𝐋𝐋 𝐀𝐔𝐓𝐎 𝐋𝐄𝐀𝐕𝐄 𝐓𝐇𝐀𝐓 𝐆𝐑𝐎𝐔𝐏 


💖 𝗔𝗯𝘂𝘀𝗲𝗦𝗽𝗮𝗺: **🌺ᴏɴᴇ ᴡᴏʀᴅ ʙɪɢ ɢᴀᴀʟɪ sᴘᴀᴍ🌺**
  1) {hl}𝚊𝚋𝚞𝚜𝚎 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  
**© ˹𝕆𝕩𝕪𝕘𝕖𝕟 ꭙ 𝕊𝕡𝕒𝕞˼🫧**
"""



yash_msg = f"""
**» ɴᴇᴡ ᴄᴏᴍᴍᴀɴᴅs:**

💘 𝗚𝗼𝗼𝗱 𝗔𝗳𝘁𝗲𝗿𝗻𝗼𝗼𝗻: **🌟ᴀғᴛᴇʀ ɴᴏᴏɴ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ🌟**
  1) {hl}𝚐𝚊 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚐𝚊 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💖 𝗘𝗺𝗼𝗷𝗶: **✨ᴇᴍᴏᴊɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ✨**
  1) {hl}𝚎𝚖𝚘𝚓𝚒 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚎𝚖𝚘𝚓𝚒 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌺 𝗚𝗼𝗼𝗱 𝗠𝗼𝗿𝗻𝗶𝗻𝗴: **🍁ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚐𝚖 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚐𝚖 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌟 𝗚𝗼𝗼𝗱 𝗡𝗶𝗴𝗵𝘁: **❤️‍🔥ɢᴏᴏᴅ ɴɪɢʜᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ❤️‍🔥**
  1) {hl}𝚐𝚗 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚐𝚗 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💖 𝗦𝗵𝗮𝘆𝗿𝗶 𝗥𝗮𝗶𝗱: **💫sʜʏʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ💫**
  1) {hl}𝚜𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <username>
  2) {hl}𝚜𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💘 𝗙𝗹𝗶𝗿𝘁𝗶𝗻𝗴: **🍁ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚏𝚕𝚒𝚛𝚝 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚏𝚕𝚒𝚛𝚝 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💘 𝗕𝗶𝗿𝘁𝗵𝗱𝗮𝘆: **🍁ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚋𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚋𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>



**© ˹𝕆𝕩𝕪𝕘𝕖𝕟 ꭙ 𝕊𝕡𝕒𝕞˼🫧**💘
"""

                 
raid_msg = f"""
**» 💘𝐑𝐀𝐈𝐃 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 💘:**

💘 𝐑𝐀𝐈𝐃: **💘𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐒 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐀𝐍𝐘 𝐈𝐍𝐃𝐈𝐕𝐈𝐃𝐔𝐀𝐋 𝐔𝐒𝐄𝐑 𝐅𝐎𝐑 𝐆𝐈𝐕𝐄𝐍 𝐑𝐀𝐍𝐆𝐄 💘**
  1) {hl}𝐑𝐀𝐈𝐃 <𝐂𝐎𝐔𝐍𝐓> <𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 >
  2) {hl}𝐑𝐀𝐈𝐃 <𝐂𝐎𝐔𝐍𝐓> <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

💘 𝐑𝐄𝐏𝐋𝐘𝐑𝐀𝐈𝐃: **💘𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐒 𝐑𝐄𝐏𝐋𝐘 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl}𝐑𝐑𝐀𝐈𝐃 <𝐑𝐄𝐏𝐋𝐘𝐈𝐍𝐆 𝐓𝐎 𝐔𝐒𝐄𝐑 >
  2) {hl}𝐑𝐑𝐀𝐈𝐃 <𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄>

💘𝐃𝐑𝐄𝐏𝐋𝐘𝐑𝐀𝐈𝐃: **💘𝐃𝐄𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐒 𝐑𝐄𝐏𝐋𝐘 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl}𝐃𝐑𝐑𝐀𝐈𝐃 <𝐑𝐄𝐏𝐋𝐘𝐈𝐍𝐆 𝐓𝐎 𝐔𝐒𝐄𝐑 >
  2) {hl}𝐃𝐑𝐑𝐑𝐀𝐈𝐃 <𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄

💘 𝐌𝐑𝐀𝐈𝐃: **💘𝐋𝐎𝐕𝐄 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl} 𝐌𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > <𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄>
  2) {hl} 𝐌𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

💘 𝐒𝐑𝐀𝐈𝐃: **💘𝐒𝐇𝐀𝐘𝐀𝐑𝐈 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl} 𝐒𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > < 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 >
  2) {hl} 𝐒𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

💘 𝐂𝐑𝐀𝐈𝐃: **💘𝐀𝐁𝐂𝐃 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl} 𝐂𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > < 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 >
  2) {hl} 𝐂𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

**© ˹𝕆𝕩𝕪𝕘𝕖𝕟 ꭙ 𝕊𝕡𝕒𝕞˼🫧**💘
"""

spam_msg = f"""
**» 💘𝐒𝐏𝐀𝐌 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 💘:**

💘 𝐒𝐏𝐀𝐌: **💘𝐒𝐏𝐀𝐌𝐒 𝐀 𝐌𝐄𝐒𝐒𝐆𝐀𝐄 💘**
  1) {hl}𝐒𝐏𝐀𝐌 < 𝐂𝐎𝐔𝐍𝐓 >  < 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐓𝐎 𝐒𝐏𝐀𝐌 >  (𝐘𝐎𝐔 𝐂𝐀𝐍 𝐑𝐄𝐏𝐋𝐘 𝐀𝐍𝐘 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐈𝐅 𝐔 𝐖𝐀𝐍𝐓 𝐓𝐎 𝐑𝐄𝐏𝐋𝐘 𝐓𝐇𝐀𝐓 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐀𝐍𝐃 𝐃𝐎 𝐒𝐏𝐀𝐌𝐌𝐈𝐍𝐆 )
  2) {hl}𝐒𝐏𝐀𝐌 < 𝐂𝐎𝐔𝐍𝐓 > < 𝐑𝐄𝐏𝐋𝐘𝐈𝐍𝐆 𝐀𝐍𝐘 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 > 

💘 𝐏𝐎𝐑𝐍𝐒𝐏𝐀𝐌: **💘𝐏𝐎𝐑𝐍𝐎𝐆𝐑𝐀𝐏𝐇𝐘 𝐒𝐏𝐀𝐌 💘**
  1) {hl}𝐏𝐒𝐏𝐀𝐌 < 𝐂𝐎𝐔𝐍𝐓 > 

💘 𝐇𝐀𝐍𝐆: **💘𝐒𝐏𝐀𝐌𝐒 𝐇𝐀𝐍𝐆 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐅𝐎𝐑 𝐆𝐈𝐕𝐄𝐍 𝐂𝐎𝐔𝐍𝐓𝐄𝐑𝐒 💘**
  1) {hl}𝐇𝐀𝐍𝐆 < 𝐂𝐎𝐔𝐍𝐓𝐄𝐑 >


** © ˹𝕆𝕩𝕪𝕘𝕖𝕟 ꭙ 𝕊𝕡𝕒𝕞˼🫧**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("★𝗦𝗣𝗔𝗠★", data="spam"),
                Button.inline("★𝗥𝗔𝗜𝗗★", data="raid"),
                Button.inline("★𝗡𝗘𝗪 𝗖𝗢𝗠𝗠𝗔𝗡𝗗★", data="yash")
              ],
              [
                Button.inline("★𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦★", data="extra")
              ],
              [
                Button.url("★𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥★", "https://t.me/naksh_vai"),
                Button.url("★𝗦𝗨𝗣𝗣𝗢𝗥𝗧★", "https://t.me/naksh_accounts")
              ]
            ]
          )
    else:
        await event.answer("★𝐏𝐋𝐄𝐀𝐒𝐄 𝐉𝐎𝐈𝐍 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐓𝐀𝐆 @naksh_accounts" , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("★𝐏𝐋𝐄𝐀𝐒𝐄 𝐉𝐎𝐈𝐍 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐓𝐀𝐆 @naksh_accounts", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("★𝐏𝐋𝐄𝐀𝐒𝐄 𝐉𝐎𝐈𝐍 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐓𝐀𝐆 @naksh_accounts", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("★𝐏𝐋𝐄𝐀𝐒𝐄 𝐉𝐎𝐈𝐍 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐓𝐀𝐆 @naksh_accounts", cache_time=0, alert=True)
        

@X1.on(events.CallbackQuery(pattern=r"yash"))
@X2.on(events.CallbackQuery(pattern=r"yash"))
@X3.on(events.CallbackQuery(pattern=r"yash"))
@X4.on(events.CallbackQuery(pattern=r"yash"))
@X5.on(events.CallbackQuery(pattern=r"yash"))
@X6.on(events.CallbackQuery(pattern=r"yash"))
@X7.on(events.CallbackQuery(pattern=r"yash"))
@X8.on(events.CallbackQuery(pattern=r"yash"))
@X9.on(events.CallbackQuery(pattern=r"yash"))
@X8.on(events.CallbackQuery(pattern=r"yash"))
async def help_yash(event):
     if event.query.user_id in SUDO_USERS:
         await event.edit(yash_msg,
             buttons=[[Button.inline("< Back", data="help_back"),],],
             )
     else:
         await event.answer("★𝐏𝐋𝐄𝐀𝐒𝐄 𝐉𝐎𝐈𝐍 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐓𝐀𝐆 @naksh_accounts", cache_time=0, alert=True)

