# 📚 School Bot – Discord Academic Assistant

School Bot is a custom Discord bot designed to help Howell High School stay on top of their academic responsibilities during the pandemic. It supports automatic user registration, calendar integration, and (in-progress) homework tracking. Built using `discord.py`, the bot is ideal for educational communities and study groups.

## ✨ Features

- 📅 **Automatic User Registration**  
  New server members are automatically added to a tracking system using a CSV file.

- 🗓️ **iCalendar (.ics) Integration**  
  Reads and parses academic events from `.ics` files like `SWCal.ics`.

- 📂 **CSV-based Persistence**  
  User data is stored in `users.csv`, updated regularly via a background task.

## 🛠 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/plannerbot.git
cd plannerbot
```

### 2. Install Dependencies

Make sure you have Python 3.8+ installed. Then, install required packages:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can create one with the following:

```
discord.py
icalendar
pytz
```

### 3. Add Your Bot Token

Create a `.env` file in the root directory and add:

```env
DISCORD_TOKEN=your-bot-token-here
```

Make sure the token is valid and the bot has appropriate permissions with all required [Intents](https://discordpy.readthedocs.io/en/stable/intents.html) enabled in the Discord Developer Portal.

### 4. Run the Bot

```bash
python "Discord Bot.py"
```

## 📁 File Structure

```
📁 plannerbot/
├── Discord Bot.py         # Bot Script
├── users.csv              # User tracking data
├── SWCal.ics              # iCalendar file used for event parsing
├── requirements.txt       # Python dependencies
└── .env                   # Bot token (not committed to version control)
```

## ⚠️ Notes

- This project was depricated in favor of School Bot 2.0
- Some features like homework tracking are still under development and should not be used.
- Ensure `users.csv` and `SWCal.ics` are present in the root directory when running the bot.
- Be mindful of API rate limits and permission scopes for the bot.

## 🧠 Future Improvements

- Implement homework reminder and task querying system
- Command to list upcoming events parsed from calendar
- Integrate scheduled reminders
- Develop a web dashboard for easier admin control

---

🧠 Built with love in 2021 for students who needed just a little more help staying organized during the pandemic.
