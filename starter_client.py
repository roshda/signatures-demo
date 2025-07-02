from nacl.signing import SigningKey
import base64
import requests

SERVER = 'http://localhost:8000'  

# step 1: generate a fresh ed25519 keypair
# todo: use signingkey.generate() to create signing_key and verify_key

# step 2: choose a keyid for this demo user
# todo: set keyid = 'student-key-1' or your own unique keyid

# step 3: encode public key as base64 for safe transport
# todo: use base64.b64encode and .decode() to produce public_key_b64

# step 4: register your public key with the server
# todo: send post request to server/register with json body containing keyid and public_key

# step 5: canonical message to sign, must match server
message = b'GET /path HTTP/1.1'

# step 6: sign the message with your private key
# todo: sign the message and base64 encode the signature for http transport

# step 7: build http-signature headers
# todo: build signature-input with keyid and created timestamp
# todo: build headers dict with signature-input and signature

# step 8: send the signed request
# todo: send get request to server/verify with your headers
# todo: print the response status and text
