from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "81171c25e4cb9062cb10da8b7730432a")
      API_ID = int(getenv("API_ID", "16253557"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002319139311:-1002406331672").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
