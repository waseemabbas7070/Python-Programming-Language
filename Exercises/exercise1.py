sentence = input("Enter a sentence: ")

word1 = input("Word to replace: ")
word2 = input("Replace with: ")

if word1 in sentence:
    sentence = sentence.replace(word1, word2)
    print("Updated sentence:", sentence)
else:
    print("Word not found in sentence.")
