from os import environ
import aiohttp
from pyrogram import Client, filters

bot = Client('Linkshortner',
             api_id=os.environ["API_ID"],
             api_hash=os.environ["API_HASH"],
             bot_token=os.environ["BOT_TOKEN"]
)

BITLY_KEY=os.environ["BITLY_KEY"]

@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def url(bot, update):
    link = update.matches[0].group(0)
    shortened_url, Err = get_shortlink(link)
    if shortened_url is None:
        message = f"Something went wrong \n{Err}"
        await update.reply(message, quote=True)
        return
    message = f"Here is your shortlink\n {shortened_url}"
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("Link 🔗", url=shortened_url)]])
    # i don't think this bot with get sending message error so no need of exceptions
    await update.reply_text(text=message, reply_markup=markup, quote=True)

def get_shortlink(url):
    shortened_url = None
    Err = None
    try:
       if BITLY_KEY:
           ''' Bittly Shorten'''
           s = Shortener(api_key=BITLY_KEY)
           shortened_url = s.bitly.short(url)
       else:
           ''' Da.gd : I prefer this '''
           s = Shortener()
           shortened_url = s.dagd.short(url)
    except Exception as error:
        Err = f"#ERROR: {error}"
        log.info(Err)
    return shortened_url,Err


bot.run()
