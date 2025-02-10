from flask import Flask, request, jsonify, redirect
from utils import *
from dbms import DBMS

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({"error": "Invalid request. JSON format should be { 'url': 'https://example.com/path_to_page' }"}), 400
    
    url = data.get('url')
    ip_address = request.remote_addr
    host = request.host
    db = DBMS()
    shortURL = ""
    while(True):
        token = generate_token()
        if db.token_exists(token):
            continue
        else:
            db.insert_data(url=url,token=token,ip_address=ip_address)
            shortURL = f"{host}/{token}"
            break

    return jsonify({"shortURL": shortURL}), 200

@app.route('/<token>', methods=['GET'])
def redirection(token):
    db = DBMS()
    url = db.get_url(token)
    return redirect(url, code=301)

if __name__ == '__main__':
    app.run(debug=True)

