def is_valid_stack(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:  # Если символ - закрывающая скобка
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)  # Если символ - открывающая скобка

    return not stack


def is_valid_recursion(s, stack=[]):
    mapping = {")": "(", "}": "{", "]": "["}

    if not s and not stack:
        return True
    elif not s and stack:
        return False

    char = s[0]
    if char in mapping:  # Если символ - закрывающая скобка
        if stack and mapping[char] == stack[-1]:
            return is_valid_recursion(s[1:], stack[:-1])
        else:
            return False
    else:  # Если символ - открывающая скобка
        return is_valid_recursion(s[1:], stack + [char])


print(is_valid_recursion('())('))