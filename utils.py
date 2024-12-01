from random import randint


def parse_dice(s: str) -> str:
    tokens = []
    try:
        for group in s.split(" "):
            amount, rest = group.split("d")
            rest = rest.replace("-", "+-")
            edges, bonus = n if len(n := rest.split("+")) == 2 else (rest, "0")
            tokens += [map(int, (amount, edges, bonus))]
    except ValueError:
        return "Wrong format!"

    res = ""
    for a, e, b in tokens:
        res += f"d{e}:"
        for _ in range(a):
            res += f" {randint(1, e) + b}"
        res += "\n"
    return res
