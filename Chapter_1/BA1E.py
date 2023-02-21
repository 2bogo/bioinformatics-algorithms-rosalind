"""
Find Patterns Forming Clumps in a String

Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval of Genome of length L in which Pattern appears at least t times.
For example, TGCA forms a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac.
"""


def findFreqInFrag(frag, k, t):
    dic = {}
    for i in range(len(frag) - k + 1):
        seq = frag[i : i + k]
        val = dic.get(seq, 0)
        val += 1
        dic[seq] = val

    return [key for key, val in dic.items() if val >= t]


def findPatterns(genome, k, L, t):
    answer_list = sum(
        [findFreqInFrag(genome[i : i + L], k, t) for i in range(len(genome) - L + 1)],
        [],
    )
    answer = " ".join(list(set(answer_list)))

    return answer


if __name__ == "__main__":
    with open("../data/Chapter_1/rosalind_ba1e.txt", "r") as f:
        genome = f.readline().strip()
        k, L, t = f.readline().strip().split()

    print(findPatterns(genome, int(k), int(L), int(t)))
