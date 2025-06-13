
import random
from lib.aun_operator import aun_operator

def generate_random_key(length=64):
    return ''.join(random.choice('01') for _ in range(length))

def generate_mirror_key(key): return key[::-1]

def generate_flip_bit_key(key):
    index = random.randint(0, len(key)-1)
    flipped = '1' if key[index] == '0' else '0'
    return key[:index] + flipped + key[index+1:]

def generate_shift_key(key, shift=3): return key[shift:] + key[:shift]

def generate_xor_pattern_key(key):
    pattern = "10101010" * (len(key) // 8)
    return ''.join(str(int(a)^int(b)) for a,b in zip(key, pattern))

def run_tests(num_keys=100, t=4, s_min=0.5):
    legit_keys = [generate_random_key() for _ in range(num_keys)]
    adversarial_keys, is_adversarial = [], []

    for k in legit_keys:
        choice = random.choice(['mirror', 'flip', 'shift', 'xor'])
        if choice == 'mirror': adversarial_keys.append(generate_mirror_key(k))
        elif choice == 'flip': adversarial_keys.append(generate_flip_bit_key(k))
        elif choice == 'shift': adversarial_keys.append(generate_shift_key(k))
        else: adversarial_keys.append(generate_xor_pattern_key(k))
        is_adversarial.append(True)

    all_keys = legit_keys + adversarial_keys
    all_labels = [False]*len(legit_keys) + is_adversarial
    tp=fp=tn=fn=0

    for i, (a, b) in enumerate(zip(all_keys, all_keys[1:] + [all_keys[0]])):
        result = aun_operator(a, b, t=t, s_min=s_min)
        collapsed = result == "⌀"
        if collapsed and all_labels[i]: tp += 1
        elif collapsed and not all_labels[i]: fp += 1
        elif not collapsed and not all_labels[i]: tn += 1
        else: fn += 1

    print(f"TP: {tp}, FP: {fp}, TN: {tn}, FN: {fn}")

if __name__ == "__main__":
    run_tests()
