import re
def isOptionHasCorrectLengthTo_25(option):
    if len(option) < 25 and len(option) != 0:
        return True


def isOptionHasCorrectLengthTo_20(option):
    if len(option) < 20 and len(option) != 0:
        return True

def isContainsOnlyLetters(value):
    return bool(re.match("^[a-zA-Z]+$", value))