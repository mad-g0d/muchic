from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Clonify import app
from config import BOT_USERNAME
from Clonify.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**ᴛ-ꜱᴇʀɪᴇꜱ** - Tʜᴇ Uʟᴛɪᴍᴀᴛᴇ Tᴇʟᴇɢʀᴀᴍ Mᴜsɪᴄ Sᴏʟᴜᴛɪᴏɴ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇs.

┏━━━━━━━━━━━━━━━━━⧫
┠ ◆ **sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ:** [Click Here](https://t.me/censored_politicss)  
┠ ◆ **ᴅᴇᴠᴇʟᴏᴘᴇʀ:** [​🇰​​🇷​​🇮​​🇸​​🇭​​🇦​​🇳​](https://t.me/censored_politicsss)
┠ ◆ **ʀᴇʟᴇᴀsᴇᴅ ʙʏ:** [​🇰​​🇷​​🇮​​🇸​​🇭​​🇦​​🇳​](https://t.me/KRISHAN_POLITICSSS)
┗━━━━━━━━━━━━━━━━━⧫

"""





@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
                InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/CUTIEE_BOT_SUPPORT"),
                InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘", url="https://t.me/KRISHAN_POLITICSSS")
        ],
        [ 
          InlineKeyboardButton("𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘", url=f"https://t.me/KRISHAN_POLITICSSS")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/sQ3.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/TeamProBots/Clonify/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/KRISHAN_POLITICSSS) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/CUTIEE_BOT_SUPPORT)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
