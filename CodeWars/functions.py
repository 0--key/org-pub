# [[file:../2024-03-27-code-wars-with-tdd.org::*Solution 001][Solution 001:1]]
def getCount(inputStr):
    num_vowels = 0
    # your code here
    for letter in inputStr:
        list_of_vowels = ['a', 'e', 'i', 'o', 'u']
        if letter.lower() in list_of_vowels:
            num_vowels += 1
            # print(letter)
            # print(num_vowels)
    return num_vowels


input_string = 'John the dully boy write this book'

print(getCount(input_string))
assert (getCount(input_string) == 9)
# Solution 001:1 ends here
