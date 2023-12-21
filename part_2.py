from collections import deque


def is_palindrome(input_str):
    input_str = input_str.lower().replace(" ", "")

    char_deque = deque(input_str)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


input_string = "A man a plan a canal Panama"
result = is_palindrome(input_string)
if result:
    print(f"'{input_string}' - це паліндром.")
else:
    print(f"'{input_string}' - не є паліндромом.")
