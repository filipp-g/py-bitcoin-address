# py-crypto-address
Python scripts to simply and easily generate cryptocurrency addresses

```
secretkey = SigningKey.generate(curve=SECP256k1)
publickey = secretkey.get_verifying_key()

wif = make_wif(secretkey.to_string())
address = make_address(serialize_pk(publickey))

print("WIF: " + wif)
print("Address: " + address)
```

Tested on Python 3.8.0

## Disclaimer
USE AT OWN RISK
