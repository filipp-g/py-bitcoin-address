# bitcoin-address
Python scripts to simply and easily generate bitcoin keys and addresses

```
signing_key = generate_signing_key()
verifying_key = signing_key.get_verifying_key()

wif = make_wif(signing_key.to_string())
public_key = serialize_pk(verifying_key)
address = make_address(public_key)

print("WIF: " + wif)
print("Address: " + address)
```

Tested on Python 3.8.0

## Disclaimer
USE AT OWN RISK
