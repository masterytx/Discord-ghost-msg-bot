ㅤㅤ  ________  ______  ___________    ____  ____  ______
   / ____/ / / / __ \/ ___/_  __/   / __ )/ __ \/_  __/
  / / __/ /_/ / / / /\__ \ / /_____/ __  / / / / / /
 / /_/ / __  / /_/ /___/ // /_____/ /_/ / /_/ / / /
\____/_/ /_/\____//____//_/     /_____/\____/ /_/

# Discord User-Installable Ghost Message Bot

A sleek, lightweight utility bot built with `discord.py` that utilizes Discord's User-Installable Application (User App) architecture. This application enables you to deploy a hidden, personal slash command (`/send`) that can be executed anywhere across the entire Discord ecosystem—including servers, Direct Messages, and Group DMs.

The application leverages interactive UI button components and asynchronous background workers to safely and seamlessly dispatch messages across different communication channels.

---

## 🚀 Features

* **Global User App Architecture:** Install the bot directly to your personal Discord profile. Execute commands across multiple servers and DMs without needing to formally invite the bot profile to every guild.
* **Ephemeral UI Control Center:** Command招invocations trigger secure, ephemeral responses (visible only to you) featuring interactive UI buttons to deploy the message stream.
* **Asynchronous Execution:** Handles message dispatching via background tasks (`asyncio.create_task`) to completely prevent gateway timeouts or freezing the application state.
* **Resilient Error Handling:** Gracefully intercepts API exceptions (such as `403 Forbidden` limits) and manages localized cooldowns automatically.

---

## 🛠️ Requirements

* Python 3.10+
* `discord.py` (v2.4.0 or higher recommended for AppCommandContext parameters)
* An active Discord Bot Token with application command scopes enabled.

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/masterytx/Discord-ghost-msg-bot.git
   cd Discord-ghost-msg-bot
   
2.  **Install the dependencies**
 `pip install discord.py`

4.  **Add Bot Token**
   `nano Ghost.py`
Then replace BOT_TOKEN_HERE whit actual bot token

6.  **Launch the bot**
`python Ghost.py`

**How to Use**

1. Ensure the application is configured as a User Installable App inside your Discord Developer Portal under the Installation tab.
2. Go to any server channel, DM, or Group DM and type /send.
3. Provide the input arguments: the text you want to transmit and the amount of times to echo it.
4. Click the interactive Send button on the ephemeral message to launch the background execution.
## ⚠️Disclaimer⚠️

This repository is created strictly for educational, testing, and self-hosting experimentation purposes. Users are expected to comply with Discord's Developer Terms of Service when deploying custom global application interactions.
