import feedparser
from discord_new import DiscordNews
import time

# this is a list where you specify the link, the name and the avatar of your webhook, you also specify what feed to use
webhooks_feeds = [
    {
        "webhook": "https://discordapp.com/api/webhooks/1217435713088393236/T29fAhJ-fz7Nd8fQJgLMvYiZhTXqmke-TIn7C7Oc-VK6EkhL1r0viFblaZpaovqeBsPG",
        "username": "UNISTRA News",
        "avatar_url": "",
        "feed_url": "https://www.unistra.fr/actualites-unistra?type=100"
    }
]

try:
    for webhooks_feed in webhooks_feeds:
        feed = feedparser.parse(webhooks_feed["feed_url"]) # analyse the feed

        discord = DiscordNews(webhooks_feed["webhook"], webhooks_feed["username"], webhooks_feed["avatar_url"], feed) # create a new instance of DiscordNews
        discord.prepare_and_notify() # prepare and send notification in Discord

        latest_feed = feed.entries[0]['id']

        while True:
            print("Sleeping...")

            time.sleep(60*60*24) # sleep for 24 hours (in seconds)

            print("Checking for new feed...")

            feed = feedparser.parse(webhooks_feed["feed_url"])

            new_latest_feed = feed.entries[0]['id']

            if new_latest_feed != latest_feed:
                discord.notify(new_latest_feed)
                latest_feed = new_latest_feed

except KeyboardInterrupt:
    print("Au revoir ✨")
