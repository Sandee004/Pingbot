from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

# Replace with your main Render app URL
MAIN_APP_URL = "https://dcraft-backend.onrender.com/ping"
PING_BOT_URL = "https://your-ping-bot.onrender.com/ping"

@app.route('/')
def home():
    return "Ping bot is running."

@app.route('/ping')
def ping():
    return "Pong", 200

def ping_loop():
    while True:
        try:
            print("Pinging main app...")
            r1 = requests.get(MAIN_APP_URL)
            print(f"Main app response: {r1.status_code}")
        except Exception as e:
            print(f"Error pinging main app: {e}")
        
        try:
            print("Pinging self...")
            r2 = requests.get(PING_BOT_URL)
            print(f"Self response: {r2.status_code}")
        except Exception as e:
            print(f"Error pinging self: {e}")

        time.sleep(300)  # 5 minutes

# Start the background ping loop
def start_background_thread():
    thread = threading.Thread(target=ping_loop, daemon=True)
    thread.start()

start_background_thread()

if __name__ == '__main__':
    app.run(debug=True)
