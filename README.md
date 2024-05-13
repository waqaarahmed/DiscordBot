#  Simple Discord Bot

This project implements a basic Discord bot using Python that interacts with users through messages.

## Features:

- Responds to greetings ("hello") with "Hello there".
- Answers "how are you" with "Good Thanks!".
- Bids farewell ("bye") with "See you".
- Rolls a virtual die upon receiving "roll dice".
- Provides generic responses for unrecognized messages.

## Installation:

### 1. Prerequisites:

- Python 3.9 or later (https://www.python.org/downloads/)
- pip package manager (https://bootstrap.pypa.io/get-pip.py)

### 2. Clone this repository:

Bash
`git clone [https://your-github-repo-url.git](https://github.com/waqaarahmed/DiscordBot.git)`

### 3. Install dependencies:

Bash
`pip install discord dotenv`

## Usage:

### 1. Create a Discord Bot Application:

- Visit the Discord Developer Portal (https://discord.com/developers/docs/intro).
- Create a new application and enable the "Bot" functionality.
- Obtain the generated bot token (keep it confidential).

### 2. Set Up Environment Variable:

- Create a file named .env in the project directory (ignore this file with Git).
- Add the following line to .env, replacing <your_bot_token> with your actual token:

`DISCORD_TOKEN=<your_bot_token>`

### 3. Run the Bot:

Bash
`python main.py`

## Customization:

- Modify the replies in replies.py to suit your bot's personality and functionality.
- Consider adding error handling for potential exceptions.
- Explore the discord.py library for more advanced bot features (https://discordpy.readthedocs.io/en/stable/api.html).

## Contributing:

- We welcome contributions to improve this project! Feel free to fork the repository and submit pull requests with enhancements or bug fixes.


