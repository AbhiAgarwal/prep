# 1
# Extended Slice Notation
# n[::-1] reverse the number
n = 'abc'
is_palindrome = str(n) == str(n)[::-1]
print is_palindrome

# 2
test = "abcba"
is_palindrome = test == ''.join(reversed(test))
print is_palindrome