# 📡 Render Ping Bot

A lightweight Flask app that keeps your **Render main project** awake by periodically pinging it.  
It also **self-pings** to prevent itself from going idle — all without any external services or paid plans.

---

## ✅ Features

- ⏱️ **Pings your main Render app every 10 minutes**
- 🔄 **Self-pings every 5 minutes** to stay alive on the free tier
- 🚫 **No external cron jobs or uptime monitors required**
- 💸 **Works on Render's free web service tier**

---

## 📁 Project Structure

```bash
ping-bot/
├── ping_bot.py           # Main Flask app with background ping loop
├── requirements.txt      # Required Python packages
└── README.md             # You're reading it!
```
## ⚙️ How It Works

Render puts free-tier web services to sleep after **15 minutes of inactivity**.  
To keep both your services awake:

- The **ping bot sends an HTTP request to itself every 5 minutes**
  - This ensures it stays active and doesn't idle
- Every other cycle (10 minutes), it also **sends a ping to your main app**
  - This keeps your main project running continuously

All of this is handled in a background thread **within the same Flask app**. No external scheduler or services are needed.

---
