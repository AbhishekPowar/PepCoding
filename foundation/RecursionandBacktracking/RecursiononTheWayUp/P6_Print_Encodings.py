# 1. You are given a string str of digits. (will never start with a 0)
# 2. You are required to encode the str as per following rules
    # 1 -> a
    # 2 -> b
    # 3 -> c
    # ..
    # 25 -> y
    # 26 -> z
# 3. Complete the body of printEncodings function - without changing signature
# - to calculate and print all encodings of str.
# Use the input-output below to get more understanding on what is required
# 123 -> abc, aw, lc
# 993 -> iic
# 013 -> Invalid input. A string starting with 0 will not be passed.
# 103 -> jc
# 303 -> No output possible. But such a string maybe passed. In this case print
# nothing.

# Note -> The online judge can't force you to write the function recursively
# but that is what the spirit of question is. Write recursive and not iterative
# logic. The purpose of the question is to aid learning recursion and not test
# you.  Input Format A string str Output Format Permutations of str in order
# hinted by Sample output Question Video

# Constraints
# 0 <= str.length <= 10
# Sample Input
# 655196

# Sample Output
# feeaif
# feesf

def getChar(n):
    return chr(int(n)+96)


def printEncoding(s, temp):
    if len(s) == 0:
        print(temp)
    else:
        firstChar = s[0]
        if len(s) > 1:
            if firstChar == '1':
                printEncoding(s[2:], temp+getChar(s[:2]))
            if firstChar == '2' and s[1] in '012345':
                printEncoding(s[2:], temp+getChar(s[:2]))
        if s[0] != '0':
            printEncoding(s[1:], temp+getChar(firstChar))


if __name__ == "__main__":
    s = '1220'
    printEncoding(s, '')
