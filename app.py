from flask import Flask, render_template, request
from datetime import datetime
from waitress import serve 

app = Flask(__name__)

@app.route('/')
def index():
    ip_address = request.remote_addr
    print(f"Received request from: {ip_address}")  # Выводим IP-адрес в консоль
    
    with open("ip_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {ip_address}\n")
    
    return render_template("index.html")

if __name__ == "__main__":
    print("Starting the server...")
    serve(app, host="0.0.0.0", port=8000)

