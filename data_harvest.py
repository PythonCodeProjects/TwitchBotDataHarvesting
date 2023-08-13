import json
from twitchio.ext import commands
import os
from datetime import datetime


# Read configuration values from config.json
with open(r"configs\config_tokens.json") as config_file:
    config = json.load(config_file)


# Read channels from channels.json
with open(r"configs\config_channels.json") as channels_file:
    channels = json.load(channels_file)
print(f"[INFO] Channels: {channels}")


def get_user_memory_path(user_id):
    first_char = user_id[0].lower()
    directory = r"user_memories"

    if not first_char.isalpha():
        directory = os.path.join(directory, "other")
    else:
        directory = os.path.join(directory, first_char)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return os.path.join(directory, f"{user_id}.json")


def save_user_memory(user_id, memory):
    print(f"[INFO] Saving memory for user {user_id}")
    with open(get_user_memory_path(user_id), "w") as f:
        json.dump(memory, f)


def load_user_memory(user_id):
    path = get_user_memory_path(user_id)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []


class TwitchBot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=config["twitch"]["token"],
            prefix=config["twitch"]["prefix"],
            initial_channels=channels    
        )

    async def event_ready(self):
        # print(f"[INFO] Bot ready. Logged in as {self.nick}")
        print(f"[INFO] Bot ready. Logged in as [REDACTED]")
        print(f"[INFO] Bot initialized. Channels: {channels}")

    async def event_message(self, message):
        if message.echo:
            return

        user_memory = load_user_memory(message.author.name)
        channel_content = {
            "date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            "messages": [{"role": "user", "content": message.content}]
        }

        for channel_memory in user_memory:
            if channel_memory["channel"] == message.channel.name:
                channel_memory["content"].append(channel_content)
                break
        else:
            user_memory.append({"channel": message.channel.name, "content": [channel_content]})

        save_user_memory(message.author.name, user_memory)

# Run the Twitch bot
if __name__ == "__main__":
    bot = TwitchBot()
    bot.run()
