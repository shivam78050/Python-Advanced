def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

input_sentence = "Hello World"
reversed_sentence = reverse_words(input_sentence)
print(reversed_sentence)  # Output: "olleH dlroW"