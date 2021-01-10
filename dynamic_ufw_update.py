from flask import Flask
from flask import request
from flask import jsonify
from settings import duu_settings
import os

app = Flask(__name__)

@app.route('/update_ufw', methods=["GET"])
def update_ufw():
    token = request.args.get('token')
    if token != duu_settings["token"]:
        return jsonify({'your_ip': "bad token"}), 403
    os.system(f'sudo ufw allow from {request.remote_addr} to any port 443')
    return jsonify({'your_ip': request.remote_addr}), 200
