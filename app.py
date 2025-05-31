from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS  # <-- ADD THIS

app = Flask(__name__)
CORS(app)  # <-- ENABLE CORS

@app.route("/", methods=["GET"])
def get_time():
    current_time = datetime.utcnow().isoformat() + "Z"
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return jsonify({
        "timestamp": current_time,
        "ip": visitor_ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
