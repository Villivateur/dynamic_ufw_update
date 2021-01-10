from flask import Flask
from flask import request
from flask import jsonify
import os

app = Flask(__name__)

@app.route('/update_ufw', methods=["GET"])
def update_ufw():
    os.system(f'sudo ufw allow from {request.remote_addr} to any port 443')
    return jsonify({'your_ip': request.remote_addr}), 200