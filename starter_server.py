from flask import Flask, request, jsonify
from nacl.signing import VerifyKey
import base64
import re

app = Flask(__name__)

# keyid (str) -> public_key (base64 str)
KEYSTORE = {}

@app.route('/register', methods=['POST'])
def register():
    
    # register a new public key under a given keyid
    # body json: { "keyid": "...", "public_key": "base64-encoded" }
    
    # todo: parse json data, extract 'keyid' and 'public_key'
    # todo: store in keystore
    # todo: return json response confirming registration
    # like this { "status": "registered", "keyid": "..." }
    return "todo: implement registration", 501

@app.route('/verify', methods=['GET'])
def verify():
    # verify an incoming signed GET /path HTTP/1.1 request, expects these headers:
    # signature-input: sig=("@authority");created=...;keyid="keyid"
    # signature: base64_signature

    # todo: get signature-input and signature headers
    # todo: get keyid from signature-input
    # todo: lookup public key from keystore
    # todo: base64 decode signature and public key
    # todo: verify signature matches canonical message
    # todo: return response (200 if verified, 403 if invalid)
    return "todo: implement verification", 501

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
