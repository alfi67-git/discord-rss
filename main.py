import feedparser
from discord_new import DiscordNews
import time

# this is a list where you specify the link, the name and the avatar of your webhook, you also specify what feed to use
webhooks_feeds = [
    {
        "webhook": "link of your server webhook here",
        "username": "username of you webhook (the one you specify on your server will not be used",
        "avatar_url": "the url of the avatar",
        "feed_url": "link of the feed you wanna use"
    }
]

for webhooks_feed in webhooks_feeds:
    feed = feedparser.parse(webhooks_feed["feed_url"]) # analyse the feed
    discord = DiscordNews(webhooks_feed["webhook"], webhooks_feed["username"], webhooks_feed["avatar_url"], feed) # create a new instance of DiscordNews
    discord.prepare_and_notify() # prepare and send notification in Discord
