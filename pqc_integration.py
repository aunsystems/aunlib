
from aun_operator import aun_operator
import hashlib
import random

def simulate_pqc_keypair():
    private_key = ''.join(random.choice('01') for _ in range(64))
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    binary_pub = ''.join(format(int(c, 16), '04b') for c in public_key)
    return private_key, binary_pub

def collapse_safe_keypair(private_key, known_keys, t=6, s_min=0.4):
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    binary_pub = ''.join(format(int(c, 16), '04b') for c in public_key)

    for known_key in known_keys:
        if aun_operator(binary_pub, known_key, t, s_min) == "⌀":
            return "Keypair rejected due to symbolic collapse condition"

    return "Keypair accepted"

if __name__ == "__main__":
    known_pub_keys = [
        ''.join(random.choice('01') for _ in range(256)) for _ in range(10)
    ]
    priv, _ = simulate_pqc_keypair()
    result = collapse_safe_keypair(priv, known_pub_keys)
    print(result)
