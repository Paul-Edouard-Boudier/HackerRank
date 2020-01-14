def merge_the_tools(string, k):
    """
    1 - split string into chunks
    2 - delete all superfluous occurrences of sub string
        2.1 - count occurrences of letters
        2.2 - delete all other occurrences of the letter
    """
    list = [string[i:i+k] for i in range(0, len(string), k)]

    for sub in list:
        temp = []
        [temp.append(c) for c in sub if c not in temp]
        print("".join(temp))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
