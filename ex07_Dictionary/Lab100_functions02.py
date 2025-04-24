words = ["apple", "cherry", "date", "berry", "fig"]
min_len = 6


def check_len(word):
    return len(word) > min_len
    OP = list(filter(check_len, words))


print(OP)
