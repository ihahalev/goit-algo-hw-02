def check_brackets(expression: str):
    stack = []
    openings = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    sim = True
    for char in expression:
        if char in openings.values():
            stack.append(char)
        if char in openings.keys():
            if not len(stack):
                sim = False
                break
            opening = openings[char]
            if stack.pop() != opening:
                sim = False
                break
    if len(stack):
        sim = False
    if sim:
        print("Симетрично")
    else:
        print("Несиметрично")

if __name__ == "__main__":
    while True:
        user_input = input("Type string for check or Enter to run predefined and exit:\n")
        if (user_input):
            check_brackets(user_input.lower().strip())
        else:
            check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}")
            check_brackets("( 23 ( 2 - 3);")
            check_brackets("( 11 }")
            check_brackets("( ) { [ ] ( ) ( ) { } } }")
            break
