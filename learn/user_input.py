
forbidden = (".", ",", "!", "?", "\"", "'", "/")
input = input("Input text:")


def reverse(input):
    return input[::-1]


def case_sensitive(input):
    return input.lower()


def space(input):
    return input.replace(" ", "")


def punctuation(input):
    for sign in forbidden:
        if input.__contains__(sign):
            print("Exists {0}".format(sign))
        input = input.replace(sign, "")
    return input


def isPolindrom(input):
    return punctuation(space(case_sensitive(input))) == reverse(punctuation(space(case_sensitive(input))))


if isPolindrom(input):
    print("This is polindrom")
else:
    print("This isn't polindrom")