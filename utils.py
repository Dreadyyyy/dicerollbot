from random import randint


def parse_dice(s: str) -> str:
    res = ""
    tokens = [list(d.split("d")) for d in s.split(" ")]
    tokens = [l for l in tokens if len(l) == 2]

    try:
        tokens = [(int(a), int(t)) for a, t in tokens]
    except ValueError:
        return "Wront format!"

    for a, t in tokens:
        res += f"d{t}:"
        for _ in range(a):
            res += f" {randint(1, t)}"
        res += "\n"
    return res
