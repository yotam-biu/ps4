def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
    digit_location = 1
    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1
    else:
        return formula[:digit_location], int(formula[digit_location:])
