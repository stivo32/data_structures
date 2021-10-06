def brute_force(text: str, pattern: str) -> None:
    l1 = len(text)
    l2 = len(pattern)
    i = 0
    flag = False

    while i < l1:
        j = 0
        count = 0
        while j < l2:
            if i+j < l1 and text[i+j] == pattern[j]:
                count += 1
            j += 1
        if count == l2:
            print('\nPattern occours at index', i)
            flag = True
        i += 1
    if not flag:
        print('\nPattern is not at all present in the array')


def main():
    brute_force('acbcabccababcaacbcaabacbbc', 'acbcaa')


if __name__ == '__main__':
    main()
