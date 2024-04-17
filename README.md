
# Discord Server Info Bot V1 📊

> `NOTE 📝:` This bot provides detailed information about a Discord server.

# Table of Contents
- [Features](#features)
- [Bot Usage](#bot-usage)
- [Commands](#commands)
  - [Sync Command](#sync-command)
  - [Server Info Command](#server-info-command)
- [Installation](#installation)
- [Configuration](#configuration)
- [Images](#images)

## Features

- **Server Info Command:** Fetches and displays various details about the server, including member count, channel count, creation date, and more.

## Bot Usage
To use this bot, follow these steps: 
+ Set up a bot on [Discord Developer Portal](https://discord.com/developers/applications)
+ Get your bot token and place it in the `config.json` file.
+ Invite the bot to your Discord server.
+ Run the bot by executing the script, ensuring your bot token is correctly placed in `config.json`.

## Commands

### Sync Command

- **Description:** Sync slash commands globally or in specific guilds.
- **Usage:** `.sync [guilds] [spec]` 
  - `guilds`: Optional list of guild IDs to sync commands to.
  - `spec`: Optional argument to specify syncing method: `"guild"`, `"global"`, or `"clear"`.
- **Permissions Required:** Bot owner

### Server Info Command

- **Description:** Fetch and display detailed information about the server.
- **Usage:** `/serverinfo`
- **Permissions Required:** None

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/TrapstarJannik/Discord-Server-Info.git
    ```
   ```sh
   cd Discord-Server-Info
   ```

3. Run the bot:
   ```sh
   python main.py
   ```

> [!IMPORTANT]
> Ensure your bot token is placed in the `config.json` file or you will encounter an error!

## Configuration

- The bot's default prefix is set to `.`. You can modify it in the `config.json` file.
- Replace the first line in `config.json` with your Discord bot token.

## Images

![Screenshot_64](https://github.com/TrapstarJannik/Discord-Server-Info/assets/166982775/98be55e1-5992-4002-b7e9-ab2acd58eb44)
