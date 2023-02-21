"""
Compute the Number of Times a Pattern Appears in a Text

A k-mer is a string of length k. We define Count(Text, Pattern) as the number of times that a k-mer Pattern appears as a substring of Text.
To compute Count(Text, Pattern), our plan is to “slide a window” down Text, checking whether each k-mer substring of Text matches Pattern. We will therefore refer to the k-mer starting at position i of Text as Text(i, k). Throughout this book, we will often use 0-based indexing, meaning that we count starting at 0 instead of 1. In this case, Text begins at position 0 and ends at position |Text| − 1 (|Text| denotes the number of symbols in Text). For example, if Text = GACCATACTG, then Text(4, 3) = ATA. Note that the last k-mer of Text begins at position |Text| − k, e.g., the last 3-mer of GACCATACTG starts at position 10 − 3 = 7. This discussion results in the following pseudocode for computing Count(Text, Pattern).
"""


def pattern_count(seq, pattern):
    count = 0
    for i in range(0, len(seq) - len(pattern) + 1):
        if seq[i : i + len(pattern)] == pattern:
            count += 1
    return count


seq = "CCTGTCTTATATTTTATATTCCTTTATATTAGTAGCACCTTTTTATATTGCATTTTTATATTATCTCTTGATTATATTGTTATATTAGCAAGTTTATATTGGTTGTTATATTATCTATTTATATTTTATATTTTCTTATATTTTTTATATTATTTATATTATTTATATTGTTATATTTTATATTTTATATTTCTTATATTTTATATTGATATTATATTGGCGTTATATTGCTTATATTGAGGCACTTTATATTGTTTATATTTTTTATATTTTATATTCTAACATCTTATATTTGGCGTTTCTTATATTGGTTATATTATTTTATATTCATTATATTGTTATATTGAGAGTTATATTTTATATTTTATATTTTATATTGATTATATTAGGATTATATTACTTATATTCTTATATTGTTATATTGATTTATATTATTATATTTTATATTTTATATTTTATATTCTTTATATTACCATTATATTTTTTATATTACTTTATGTTATATTTTATATTCTTATATTTATATTATATTGCCCTTTATATTTTATATTCTTATATTTTATATTGGCACTTTATATTCTTATATTCCCCTCGTTATATTGCCGTTATATTCACTTATATTTCGTTATATTTTATATTATCACATTATATTCTTATATTACAGTGGCGCTTATATTTCTCTTATATTCCGAGAATTATATTAGTTTACATTTTATATTAGTTATATTTTATATTCTAGTCTTATATTAGTGTTATATTGTTGGGACTTTATATTGACTGGTTATATTGTTATATTCTTATATTTTATATTCTTTGAATTATATTTTTATATTACTTATATTTCTTTTTATATTTGCGCATCTTATATTTTATATTTACTTATATTCCCATTATATTCGTGTCCTACCTTATATTCTTATATTGCGTTTATATTTTTATATTCTTATATTGCGGTTATTTATATTGGCGATAACATAGTTATATTAATAAATTATATTT"
pattern = "TTATATTTT"

print(pattern_count(seq, pattern))
