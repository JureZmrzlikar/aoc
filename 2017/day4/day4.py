def parse_input(fname):
    data = []
    with open(fname) as handle:
        for line in handle:
            data.append(line.strip())
    return data


def sort_word(word):
    return ''.join(sorted([char for char in word]))


def is_valid(word_list, no_anagrams=False):
    if no_anagrams:
        # Sort each word to be able to detect anagrams:
        word_list = [sort_word(word) for word in word_list]
        # print(word_list)
    return len(set(word_list)) == len(word_list)


def count_valid(data, no_anagrams=False):
    valid = 0
    for passphrase in data:
        if is_valid(passphrase.split(), no_anagrams=no_anagrams):
            valid += 1
    return valid


data = parse_input('/home/jure/devel/adventofcode/day4/input.txt')
print(count_valid(data))
print(count_valid(data, no_anagrams=True))
