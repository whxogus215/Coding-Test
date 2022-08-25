def generateParenthesis(n: int):
    if ( n == 1 or n == 0):
        print("()")
    else:
        generateParenthesis(n-1) + generateParenthesis(n-2)

generateParenthesis(3)

    