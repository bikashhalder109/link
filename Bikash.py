# Powered By @BikashHalder

from pyrogram import Client, filters
from telegraph import upload_file
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

import os

bgt=Client(
    "Bikash",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

SUPPORT_CHAT = os.environ["SUPPORT_CHAT"]
UPDATES_CHNL = os.environ["UPDATES_CHNL"]
OWNER_USERNAME = os.environ["OWNER_USERNAME"]
BOT_USERNAME = os.environ["BOT_USERNAME"]

@bgt.on_message(filters.command('start') & filters.private)
async def start(client: client, message: message):
   await message.reply_photo(
        photo=f"https://te.legra.ph/file/f73af9a4ffe130a83d8d2.jpg",
        caption=f"""
━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐞𝐲 {message.from_user.mention},

𝐈 𝐚𝐦 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐆𝐚𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 𝐋𝐢𝐧𝐤 𝐁𝐨𝐭
𝐈'𝐦 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐘𝐨𝐮𝐫 𝐌𝐞𝐝𝐢𝐚 𝐓𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 𝐋𝐢𝐧𝐤 .

𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞 : **Simply Send Any Valid
Media File In This Chat .
𝐅𝐢𝐥𝐞 𝐓𝐲𝐩𝐞𝐬 : 'jpeg', 'jpg', 'png', 'mp4' and 'gif

┏━━━━━━━━━━━━━━━━━┓
┣★ 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 : [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{OWNER_USERNAME})
┣★ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 » : [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{UPDATES_CHNL})
┣★ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 » : [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/BikashHalder)
┗━━━━━━━━━━━━━━━━━┛

💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 &
𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐕𝐚𝐥𝐢𝐝 𝐏𝐢𝐜 𝐂𝐦𝐝 /bgt 𝐎𝐫 /tl
𝐅𝐨𝐫 𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐌𝐞𝐝𝐢𝐚 𝐓𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 𝐋𝐢𝐧𝐤
━━━━━━━━━━━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐏𝐨𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 🥀", url=f"https://t.me/BgtPromote")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/{SUPPORT_CHAT}")
            ],
            [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
                    InlineKeyboardButton(
                        "🥀 𝐁𝐠𝐭 𝐂𝐡𝐚𝐭 🥀", url=f"https://t.me/Bgt_Chat"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 🥀", url=f"https://youtube.com/@BikashGadgetsTech")
                ]
            ]
        ),
     )  

@bgt.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("♡ 𝐁𝐠𝐭 𝐁𝐨𝐭 𝐍𝐨𝐰 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐌𝐞𝐝𝐢𝐚 ...")
        async def progress(current, total):
            await text.edit_text(f"♥ 𝐁𝐠𝐭 𝐁𝐨𝐭 𝐍𝐨𝐰 📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐌𝐞𝐝𝐢𝐚 ... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("♥ 𝐁𝐠𝐭 𝐁𝐨𝐭 𝐍𝐨𝐰 📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 ...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🥀 𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 | 𝐋𝐢𝐧𝐤 = 𝐓𝐚𝐩 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐤 𝐓𝐨 𝐂𝐨𝐩𝐲**:\n\n<code>https://telegra.ph{upload_path[0]}</code>\n\n[𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_CHAT})\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHNL})\n[𝐂𝐫𝐞𝐚𝐭𝐨𝐫](https://t.me/BikashHalder)")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ 𝐅𝐢𝐥𝐞 𝐔𝐩𝐥𝐨𝐚𝐝 𝐈 𝐅𝐚𝐢𝐥𝐞𝐝**\n\n<i>**𝐑𝐞𝐚𝐬𝐨𝐧**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@bgt.on_message(filters.command('tl', 'bgt'))
async def get_link_group(client, message):
    try:
        text = await message.reply("♡ 𝐁𝐠𝐭 𝐁𝐨𝐭 𝐍𝐨𝐰 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐌𝐞𝐝𝐢𝐚....")
        async def progress(current, total):
            await text.edit_text(f"📥 ♥ 𝐁𝐠𝐭 𝐁𝐨𝐭 𝐍𝐨𝐰 📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐌𝐞𝐝𝐢𝐚 ...  {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("♥ 𝐁𝐠𝐭 𝐁𝐨𝐭 𝐍𝐨𝐰 📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🥀 𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 | 𝐋𝐢𝐧𝐤 𝐓𝐚𝐩 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐤 𝐓𝐨 𝐂𝐨𝐩𝐲**:\n\n<code>https://telegra.ph{upload_path[0]}</code>\n\n[𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_CHAT})\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHNL})\n[𝐂𝐫𝐞𝐚𝐭𝐨𝐫](https://t.me/BikashHalder)")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ 𝐅𝐢𝐥𝐞 𝐔𝐩𝐥𝐨𝐚𝐝 𝐈 𝐅𝐚𝐢𝐥𝐞𝐝**\n\n<i>**𝐑𝐞𝐚𝐬𝐨𝐧**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                           

print("Bgt Telegraph Bot Is Alive !")
bgt.run()

