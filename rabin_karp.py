def rabin_karp(text: str, pattern: str):
    hash_text, hash_pattern = generate_hash(text, pattern)
    len_pattern = len(pattern)
    flag = False
    for i, _ in enumerate(hash_text):
        if hash_text[i] == hash_pattern:
            count = 0
            for j, symbol in enumerate(pattern):

                if symbol == text[i + j]:
                    count += 1
                else:
                    break
            if count == len_pattern:
                flag = True
                print('Pattern occours at index', i)
    if not flag:
        print('Pattern is not at all present in the text')


def generate_hash(text: str, pattern: str):
    ord_text = [ord(i) for i in text]
    ord_pattern = [ord(i) for i in pattern]
    len_text = len(text)
    len_pattern = len(pattern)
    hash_pattern = sum(ord_pattern)
    len_hash_array = len_text - len_pattern + 1
    hash_text = [0] * len_hash_array
    for i in range(0, len_hash_array):
        if i == 0:
            hash_text[i] = sum(ord_text[:len_pattern])
        else:
            hash_text[i] = (hash_text[i - 1] - ord_text[i - 1]) + ord_text[i + len_pattern - 1]
    return [hash_text, hash_pattern]


def main():
    rabin_karp('acbcabccababcaacbcaabacbbc', 'acbcaa')


if __name__ == '__main__':
    main()