from hashlib import sha256, new
from ecdsa import SigningKey, SECP256k1
from ecdsa.util import number_to_string
from base58 import b58encode


def generate_signing_key():
    return SigningKey.generate(curve=SECP256k1)


def serialize_pk(pubkey, compress=False):
    if compress:
        p = pubkey.pubkey
        pfx = b'\x03' if p.point.y() & 1 else b'\x02'
        serialized = pfx + number_to_string(p.point.x(), p.order)
    else:
        serialized = b'\x04' + pubkey.to_string()
    return serialized


def get_checksum(addr):
    return sha256(sha256(addr).digest()).digest()[:4]


def make_address(pubkey):
    hash160 = new("ripemd160")
    hash160.update(sha256(pubkey).digest())
    addr = b"\x00" + hash160.digest()
    addr += get_checksum(addr)
    return b58encode(addr).decode("utf-8")


def make_wif(privkey):
    wif = b"\x80" + privkey
    wif += get_checksum(wif)
    return b58encode(wif).decode("utf-8")


signing_key = generate_signing_key()
verifying_key = signing_key.get_verifying_key()

wif = make_wif(signing_key.to_string())
public_key = serialize_pk(verifying_key)
address = make_address(public_key)

print("WIF: " + wif)
print("Address: " + address)
