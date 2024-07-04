from collections import deque

def is_palindrome(some_str: str):
    d = deque(some_str)
    msg = f"Checking {some_str}... "
    check = True
    while len(d)>1:
        if (d.pop() != d.popleft()):
            check = False
            break
    if check:
        print(f"{msg}Is palindrome")
    else:
        print(f"{msg}Not palindrome")

if __name__ == "__main__":
    while True:
        user_input = input("Type string for check or Enter to run predefined and exit:\n")
        if (user_input):
            is_palindrome(user_input.lower().strip())
        else:
            is_palindrome("312123")
            is_palindrome("321123")
            is_palindrome("321777123")
            is_palindrome("3217787123")
            break
