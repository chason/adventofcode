import fileinput
from collections import defaultdict


def process_claim(claim):
    claim_id, _, loc, size = claim.split()
    loc = [int(d) for d in loc[:-1].split(",")]
    size = [int(d) for d in size.split("x")]
    return claim_id, loc, size


if __name__ == "__main__":
    fabric = defaultdict(list)
    claims = []
    for line in fileinput.input():
        claim = process_claim(line.strip())
        claims.append(claim[0])
        for x in range(claim[1][0], claim[1][0] + claim[2][0]):
            for y in range(claim[1][1], claim[1][1] + claim[2][1]):
                square_id = f"{x},{y}"
                fabric[square_id].append(claim[0])
                if len(fabric[square_id]) > 1:
                    for bad_claim in fabric[square_id]:
                        try:
                            claims.remove(bad_claim)
                        except ValueError:
                            continue
    print(
        "Squares with multiple claims: {}".format(
            len(list(filter(lambda sq: len(sq) > 1, fabric.values())))
        )
    )
    print("Claims with no overlap: {}".format(claims))
