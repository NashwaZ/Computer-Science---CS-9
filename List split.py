

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

n = int(input('Enter a number: '))

split = [letters[i::n] for i in range(n)]
print(split)