from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋 ¦ اهلا عمࢪي  {}
 📮 ¦ في بوت 📬 {} 
━━━━━━━━━━━━━━━━━━━
🕹 ¦ يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس والبايروجرام تم انشـاء هـذا البـوت بواسطـة : @n_g_7

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")],
        [InlineKeyboardButton(text="⚜️¦ رجــوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")],
        [
            InlineKeyboardButton("⚜️¦ كيف تستخدمني", callback_data="help"),
            InlineKeyboardButton("⚜️¦ حــول", callback_data="about")
        ]
    ]

    # Help Message
    HELP = """
✨ **📬 ¦ كـيف تستخـدمني** ✨

× /about - حول البوت
× /help - لتسوي روحك كلشي متعرف
× /start - حتى تشغل البوت
× /generate - حتى تبدا بأستخراج جلسة
× /cancel - لألغاء الاستخراج
× /restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**⚜️¦حـول البـوت** 

- بـوت استخـراج كـود تيرمكـس خـاص بســورس كولدن 

كروب السورس : [كروب سورس ايــثــون](https://t.me/eithonsupport)

استخدم البوت : 

»[Pyrogram](docs.pyrogram.org)
🕹
»[Python](www.python.org)

لغة البوت : [بايثون](www.python.org)

🇸🇾 ¦ المطور  (https://t.me/n_g_7)
    """
