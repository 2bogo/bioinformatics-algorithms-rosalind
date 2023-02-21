"""
Find a Position in a Genome Minimizing the Skew
"""


def skew(genome):
    state = 0
    dic = {}
    for i in range(len(genome)):
        dic[i] = state
        if genome[i] == "C":
            state -= 1
        elif genome[i] == "G":
            state += 1
        else:
            pass

    return dic


def findMinimumSkew(dic):
    min_value = min(dic.values())
    return " ".join([str(key) for key, val in dic.items() if val == min_value])


if __name__ == "__main__":
    with open("../data/Chapter_1/rosalind_ba1f.txt", "r") as f:
        genome = f.readline().strip()

    # genome = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"

    result = findMinimumSkew(skew(genome))
    print(result)
