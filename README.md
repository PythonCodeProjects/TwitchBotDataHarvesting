# Twitch Bot Data Harvesting

This project consists of three files: `data_harvest.py`, `config_channels.json`, and `config_tokens.json`. The purpose of the project is to create a Twitch bot that can harvest data, such as messages, from specified channels. The harvested data is stored in user-specific memory files.

## Project Files

### data_harvest.py

This file contains the main code for the Twitch bot. It performs the following actions:

1. Imports the necessary modules (`json`, `twitchio.ext.commands`, `os`, `datetime`).
2. Reads the configuration values from `config_tokens.json`.
3. Reads the channels from `config_channels.json`.
4. Defines functions for accessing and storing user memories.
5. Implements the `TwitchBot` class, which is a subclass of `commands.Bot`.
6. Specifies the bot's behavior when it is ready and handles incoming messages.
7. Runs the Twitch bot.

### config_channels.json

This file is a JSON array that contains the names of the channels from which data will be harvested. Currently, it only contains one channel named "RocketLeague". New channels can be added to the array by simply appending their names.

### config_tokens.json

This file is a JSON object that contains the Twitch token and prefix for the bot. The token is a secret authentication key that grants access to the Twitch API. The prefix is a character or string that denotes a command for the bot. The example file, `config_tokens_example.json`, needs to be renamed to `config_tokens.json`, and the correct credentials should be added to the file.

## How the Twitch Bot Works

1. The Twitch bot is initialized with the bot's Twitch authentication token, command prefix, and the initial channels specified in `config_channels.json`.

2. When the bot is ready, it prints a ready message and the list of channels it is connected to.

3. When a new message is received, the bot loads the user's memory file if it exists or creates an empty memory list.

4. The bot creates a `channel_content` object containing the current date and time and the message content. This object is appended to the user's memory list for the respective channel.

5. If the user already has memory for the current channel, the new `channel_content` object is added to the existing memory. If the user does not have memory for the channel, a new memory object is created.

6. After updating the user's memory, it is saved to the respective user's memory file.

7. The bot continues processing messages, updating user memories as needed.

## Instruction for Running the Project

1. Ensure that you have the required Python dependencies installed. You can install the dependencies by running the following command:

   ```
   pip install twitchio
   ```

   If you are using a virtual environment, make sure it is activated before running the command.

2. Rename `config_tokens_example.json` to `config_tokens.json`.

3. Open `config_tokens.json` and replace the example token (`oauth:hudfh74ExampleToken54hj3f7sdf3`) with your Twitch bot's authentication token. Additionally, modify the prefix if desired.

4. Modify `config_channels.json` to include the names of the channels from which you want to harvest data. You can add or remove channels from the JSON array.

5. Run the `data_harvest.py` file using the following command:

   ```
   python data_harvest.py
   ```

   This will start the Twitch bot and connect it to the specified channels.

6. The bot will print status messages to the console, such as when it is ready, initialized, and saving user memory. It will also print any errors encountered during runtime.

7. As users send messages in the subscribed channels, the bot will harvest and store the data in user-specific memory files located in the `user_memories` directory.

8. To stop the bot, press `Ctrl + C` in the console.
