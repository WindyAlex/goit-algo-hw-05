def boyer_moore_search(text, pattern):
    if pattern == "":
        return 0
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1

    last = {}
    for i in range(m):
        last[pattern[i]] = i

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            return i

        bad_char = text[i + j]
        shift = j - last.get(bad_char, -1)
        if shift < 1:
            shift = 1
        i += shift

    return -1


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    if pattern == "":
        return 0
    if len(pattern) > len(main_string):
        return -1

    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


def rabin_karp_search(text, pattern, base: int = 256, mod: int = 101):
    if pattern == "":
        return 0
    if len(pattern) > len(text):
        return -1

    m = len(pattern)
    n = len(text)

    high = 1
    for _ in range(m - 1):
        high = (high * base) % mod

    pat_hash = 0
    win_hash = 0

    for i in range(m):
        pat_hash = (pat_hash * base + ord(pattern[i])) % mod
        win_hash = (win_hash * base + ord(text[i])) % mod

    for i in range(n - m + 1):
        if pat_hash == win_hash:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            win_hash = (win_hash - ord(text[i]) * high) % mod
            win_hash = (win_hash * base + ord(text[i + m])) % mod
            win_hash %= mod

    return -1
