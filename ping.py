import time
import requests

def ping_main():
    while True:
        try:
            requests.get("https://dcraft-backend.onrender.com/ping")
            print("Ping sent")
        except Exception as e:
            print(f"Failed: {e}")
        time.sleep(600)

ping_main()
