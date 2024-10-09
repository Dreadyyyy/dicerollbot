from random import randint


def parse_dice(s: str) -> str:
    res = ""

    try:
        tokens = [[int(v) for v in d.split("d")] for d in s.split(" ")]
    except ValueError as _:
        return "Wrong format!"

    for a, t in tokens:
        res += f"d{t}:"
        for _ in range(a):
            res += f" {randint(1, t)}"
        res += "\n"
    return res
