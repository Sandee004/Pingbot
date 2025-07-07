from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

# Replace with your main Render app URL
MAIN_APP_URL = "https://dcraft-backend.onrender.com/ping"
PING_BOT_URL = "https://pingbot-sey2.onrender.com/ping"

@app.route('/')
def home():
    return "Ping bot is running."

@app.route('/ping')
def ping():
    return "Pong", 200

def ping_loop():
    main_ping_timer = 0

    while True:
        # Self-ping every 5 minutes
        try:
            print("Pinging self...")
            r_self = requests.get(PING_BOT_URL)
            print(f"Self ping status: {r_self.status_code}")
        except Exception as e:
            print(f"Self ping failed: {e}")

        # Ping main app every 10 minutes
        if main_ping_timer >= 10:
            try:
                print("Pinging main app...")
                r_main = requests.get(MAIN_APP_URL)
                print(f"Main app ping status: {r_main.status_code}")
            except Exception as e:
                print(f"Main app ping failed: {e}")
            main_ping_timer = 0
        else:
            main_ping_timer += 5  # Increment timer

        time.sleep(300)  # Sleep for 5 minutes (300 seconds)

# Start the background thread
def start_background_thread():
    thread = threading.Thread(target=ping_loop, daemon=True)
    thread.start()

start_background_thread()

if __name__ == '__main__':
    app.run(debug=True)
