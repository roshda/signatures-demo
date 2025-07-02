from nacl.signing import SigningKey
import base64
import requests

SERVER = 'http://localhost:8000'
# step 1: generate a fresh ed25519 keypair
signing_key = SigningKey.generate()
verify_key  = signing_key.verify_key

# step 2: choose a keyid for this demo user
keyid = 'mykey'

# step 3: encode public key as base64
public_key_b64 = base64.b64encode(verify_key.encode()).decode()

# step 4: register your public key with the server
r = requests.post(f'{SERVER}/register', json={
    'keyid': keyid,
    'public_key': public_key_b64
})
print('Register response:', r.status_code, r.text)

# step 5: canonical message to sign, must match server
message = b'GET /path HTTP/1.1'

# step 6: sign the message with your private key
signed = signing_key.sign(message)
signature_b64 = base64.b64encode(signed.signature).decode()
print('signature:', signature_b64)

# step 7: build http-signature headers
sig_input = f'sig=("@authority");created=1700000000;keyid="{keyid}"'
headers = {
    'Signature-Input': sig_input,
    'Signature': signature_b64
}

# step 8: send the signed request
r2 = requests.get(f'{SERVER}/verify', headers=headers)
print('verify response:', r2.status_code, r2.text)
