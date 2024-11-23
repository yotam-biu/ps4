def split_before_each_uppercases(formula):
    if len(formula) == 0:
       return []
    start = 0
    end = 1
    split_formula = []
    for char in formula[1:]:
        if char.isupper():
            split_formula.append(formula[start:end])
            start = end
        end += 1
    split_formula.append(formula[start:end])
    return split_formula


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
