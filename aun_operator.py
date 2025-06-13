
from transforms import apply_transforms

def hamming_distance(a: str, b: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(a, b))

def s_score(a: str, b: str, window_size=8) -> float:
    total = 0
    matches = 0
    weights = {
        'identity': 1.0,
        'reverse': 0.8,
        'xor_ff': 0.6,
        'left_rotate': 0.5,
        'right_rotate': 0.5,
    }
    for i in range(0, len(a) - window_size + 1):
        a_slice = a[i:i+window_size]
        b_slice = b[i:i+window_size]
        if len(a_slice) < window_size or len(b_slice) < window_size:
            continue
        transforms = apply_transforms(a_slice)
        for name, val in transforms.items():
            if val == b_slice:
                matches += weights.get(name, 0)
                break
        total += 1
    return matches / total if total else 0

def aun_operator(a: str, b: str, t=4, s_min=0.5) -> str:
    h = hamming_distance(a, b)
    s = s_score(a, b)
    if h < t and s > s_min:
        return "⌀"
    return ''.join(str(int(x)^int(y)) for x, y in zip(a, b))
