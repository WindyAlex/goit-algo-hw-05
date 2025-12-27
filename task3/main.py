import timeit

from search_algorithms import boyer_moore_search, kmp_search, rabin_karp_search


def main():
    with open("data/article1.txt", "r", encoding="utf-8") as f:
        text1 = f.read()

    with open("data/article2.txt", "r", encoding="utf-8") as f:
        text2 = f.read()

    pattern1 = text1[len(text1)//2: len(text1)//2 + 30]
    fake1 = pattern1[::-1] + "xxx"

    pattern2 = text2[len(text2)//2: len(text2)//2 + 30]
    fake2 = pattern2[::-1] + "xxx"

    print("-Article 1:")
    print("Existing substring:")
    print("Boyer-Moore:", round(timeit.timeit(
        lambda: boyer_moore_search(text1, pattern1), number=1), 6))
    print("KMP:", round(timeit.timeit(
        lambda: kmp_search(text1, pattern1), number=1), 6))
    print("Rabin-Karp:", round(timeit.timeit(
        lambda: rabin_karp_search(text1, pattern1), number=1), 6))

    print("\nFake substring:")
    print("Boyer-Moore:", round(timeit.timeit(
        lambda: boyer_moore_search(text1, fake1), number=1), 6))
    print("KMP:", round(timeit.timeit(
        lambda: kmp_search(text1, fake1), number=1), 6))
    print("Rabin-Karp:", round(timeit.timeit(
        lambda: rabin_karp_search(text1, fake1), number=1), 6))

    print("\n-Article 2:")
    print("Existing substring:")
    print("Boyer-Moore:", round(timeit.timeit(
        lambda: boyer_moore_search(text2, pattern2), number=1), 6))
    print("KMP:", round(timeit.timeit(
        lambda: kmp_search(text2, pattern2), number=1), 6))
    print("Rabin-Karp:", round(timeit.timeit(
        lambda: rabin_karp_search(text2, pattern2), number=1), 6))

    print("\nFake substring:")
    print("Boyer-Moore:", round(timeit.timeit(
        lambda: boyer_moore_search(text2, fake2), number=1), 6))
    print("KMP:", round(timeit.timeit(
        lambda: kmp_search(text2, fake2), number=1), 6))
    print("Rabin-Karp:", round(timeit.timeit(
        lambda: rabin_karp_search(text2, fake2), number=1), 6))


main()
