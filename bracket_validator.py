def validate_brackets(code_to_validate):
    """
    You're working with an intern that keeps coming to you with JavaScript code that won't run because
    the braces, brackets, and parentheses are off.
    To save you both some time, you decide to write a braces/brackets/parentheses validator.
    """

    if not code_to_validate:
        raise ValueError('Cannot validate an empty string')

    counter = {
        '{': 0,
        '[': 0,
        '(': 0,
        '}': 0,
        ']': 0,
        ')': 0
    }

    # What cannot be inmediately after a given symbol
    rules = {
        '{': '])',
        '[': '})',
        '(': '}]',
        '}': '',
        ']': '',
        ')': ''
    }

    i = 0
    while i < len(code_to_validate) - 1:

        if code_to_validate[i+1] in rules[code_to_validate[i]]:
            return False

        counter[code_to_validate[i]] += 1
        i += 1

    counter[code_to_validate[i]] += 1

    return counter['{'] == counter['}'] and \
        counter['['] == counter[']'] and \
        counter['('] == counter[')']


if __name__ == "__main__":

    assert validate_brackets("{[]()}") == True
    assert validate_brackets("{[(])}") == False
    assert validate_brackets("{[}") == False
    assert validate_brackets("{[])()}") == False