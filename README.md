# Django Terminal Chatbot Using ChatterBot

This project is a terminal client that lets a user chat with a bot using Django, Python, and ChatterBot.

## Setup

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
cd chatbot_project
python manage.py train_bot
python manage.py terminal_chat
```

## Usage Example

```text
Training TerminalBot. Please wait...
TerminalBot is ready.
Type 'quit', 'exit', or 'bye' to end the chat.

user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: You're welcome.
bot: Do you like hats?
user: bye
bot: Goodbye. Have a great day!
```

## Files

- `manage.py` - Django command utility.
- `settings.py` - Minimal Django settings for the terminal app.
- `bot_service.py` - Builds and trains the ChatterBot instance.
- `training_data.py` - Starter conversation data.
- `terminal_chat.py` - Interactive terminal chat command.
- `train_bot.py` - Optional training command.
- `MANIFEST.in` - Source distribution manifest.
- `requirements.txt` - Required Python dependencies.

## GitHub Submission

Create a new GitHub repository, upload these files, and paste the repository URL into the Word document before submitting.
