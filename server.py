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
    data = request.get_json(force=True)
    keyid = data.get('keyid')
    public_key = data.get('public_key')
    if not keyid or not public_key:
        return jsonify({'error': '"keyid" and "public_key" required'}), 400

    KEYSTORE[keyid] = public_key
    return jsonify({'status': 'registered', 'keyid': keyid}), 200

@app.route('/verify', methods=['GET'])
def verify():
    # verify an incoming signed GET /path HTTP/1.1 request, expects these headers:
    # signature-input: sig=("@authority");created=...;keyid="keyid"
    # signature: base64_signature
    sig_input = request.headers.get('Signature-Input')
    sig_b64   = request.headers.get('Signature')

    if not sig_input or not sig_b64:
        return 'Missing Signature-Input or Signature header', 400

    # Extract keyid from Signature-Input
    m = re.search(r'keyid="([^"]+)"', sig_input)
    if not m:
        return 'invalid format no keyid', 400
    keyid = m.group(1)

    public_key_b64 = KEYSTORE.get(keyid)
    if not public_key_b64:
        return f'unknown keyid: {keyid}', 404

    # decode the signature
    signature = base64.b64decode(sig_b64)

    message = b'GET /path HTTP/1.1'

    try:
        vk = VerifyKey(base64.b64decode(public_key_b64))
        vk.verify(message, signature)
        return 'signature verified', 200
    except Exception as e:
        return f'invalid signature: {e}', 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
