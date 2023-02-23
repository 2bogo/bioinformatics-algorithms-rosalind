"""
Find All Approximate Occurrences of a Pattern in a String
"""


def findAllPattern(string, k_len):
    dic = {}
    for i in range(len(string) - k_len + 1):
        pattern = string[i : i + k_len]
        val = dic.get(pattern, [])
        val.append(i)
        dic[pattern] = val
    return dic


def hammingDistance(p, q):
    return [True if i == j else False for i, j in zip(p, q)].count(False)


def mainFunc(pattern, string, d):
    dic_all_pattern = findAllPattern(string, len(pattern))
    result = sorted(
        sum(
            [
                val
                for key, val in dic_all_pattern.items()
                if hammingDistance(key, pattern) <= d
            ],
            [],
        )
    )

    return " ".join(list(map(str, result)))


if __name__ == "__main__":
    with open("../data/Chapter_1/rosalind_ba1h.txt", "r") as f:
        pattern = f.readline().strip()
        text = f.readline().strip()
        d = int(f.readline().strip())

        # pattern = "ATTCTGGA"
        # text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
        # d = 3

    result = mainFunc(pattern, text, d)
    print(result)
