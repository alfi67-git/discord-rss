import feedparser
from discord_new import DiscordNews
import time

# this is a list where you specify the link, the name and the avatar of your webhook, you also specify what feed to use
webhooks_feeds = [
    {
        "webhook": "URL of the webhook here",
        "username": "Name of your bot here",
        "avatar_url": "",
        "feed_url": "URL of the RSS feed"
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
