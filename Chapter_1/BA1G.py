"""
Compute the Hamming Distance Between Two Strings
"""


def hammingDistance(p, q):
    return [True if i == j else False for i, j in zip(p, q)].count(False)


if __name__ == "__main__":
    with open("../data/Chapter_1/rosalind_ba1g.txt") as f:
        p = f.readline().strip()
        q = f.readline().strip()

    result = hammingDistance(p, q)
    print(result)
