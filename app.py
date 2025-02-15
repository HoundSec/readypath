from flask import Flask, request, jsonify, redirect, render_template, abort
from utils import *
from dbm import DBM

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html",title="ReadyPath - Home",url=request.url,description="ReadyPath is a URL shortener that transforms your long, gibberish URLs into short, human-readable links that are easy to type and remember. Enjoy fast, clean, and 100% ad-free URL shortening!  It's open source, so feel free to contribute on GitHub.  We also respect your privacy—we don't sell your data for profit.  No click data is collected, no cookies are used, and no login is required.  Just come to ReadyPath, shorten your links, and use them!")

@app.route('/terms', methods=['GET'])
def terms():
    return render_template("terms.html",title="ReadyPath - Home",url=request.url,description="By accessing and using ReadyPath’s URL shortening service, you agree to comply with and be bound by these Terms and Conditions. ReadyPath is provided as a streamlined tool to convert long URLs into concise, shareable links for lawful and responsible purposes. You are solely responsible for ensuring that the URLs you submit do not violate any applicable laws, infringe on the rights of third parties, or contain content that is defamatory, harmful, or otherwise inappropriate. We reserve the right to modify, suspend, or terminate access to our service if any content is found to breach these terms. While we strive to maintain a secure and reliable service, ReadyPath assumes no liability for any loss, damage, or legal consequences arising from your use of the platform. By using our service, you acknowledge that you have read, understood, and agree to these Terms and Conditions.")

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({"error": "Invalid request. JSON format should be { 'url': 'https://example.com/path_to_page' }"}), 400
    
    url = data.get('url')
    ip_address = request.remote_addr
    host = request.host
    db = DBM()
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
    db = DBM()
    url = db.get_url(token)
    if url == None:
        return abort(404)
    return redirect(url, code=301)

if __name__ == '__main__':
    app.run(debug=True)

