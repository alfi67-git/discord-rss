import requests
from dateutil import parser as date_parser
import locale

class DiscordNews:

    def __init__(self, webhook, username, avatar_url, feed):
        self.webhook = webhook
        self.username = username
        self.avatar_url = avatar_url
        self.feed = feed

    def prepare_and_notify(self):
        latest_entry = self.feed.entries[0] #get the last entry
        self.__notify_to_discord_channel(latest_entry)

    def notify(self, data):
        self.__notify_to_discord_channel(data)

    # this is where you can customize the message that will be sent on you server
    def __notify_to_discord_channel(self, data):
        headers = {"Content-Type": "application/json"}
        published_date = date_parser.parse(data.published)
        locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
        format_date = published_date.strftime("%A %d %B %Y")
        content = f'''
        # 📰📢  Nouvelle publication disponible !  📢📰
        
**{data.title}** 

🗓 {format_date}

{data.link}
        
{data.description}
        '''
        payload = {
            "username": self.username,
            "content": content,
            "avatar_url": self.avatar_url
        }
        return requests.post(url=self.webhook, headers=headers, json=payload)
