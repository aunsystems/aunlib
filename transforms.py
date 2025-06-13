
def apply_transforms(bits: str) -> dict:
    return {
        'identity': bits,
        'reverse': bits[::-1],
        'xor_ff': ''.join('1' if b == '0' else '0' for b in bits),
        'left_rotate': bits[1:] + bits[0],
        'right_rotate': bits[-1] + bits[:-1],
    }
