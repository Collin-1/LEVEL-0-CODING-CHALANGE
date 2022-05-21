def common_letters(string1, string2):
    lower_case_string1 = string1.lower()
    lower_case_string2 = string2.lower()
    common_characters = []
    delimeter = ", "

    for letter in lower_case_string2:
        if letter in lower_case_string1:
            if letter in common_characters:
                continue
            common_characters = common_characters + [letter]
    results = delimeter.join(common_characters)
    return f"Common letter: {results}"
