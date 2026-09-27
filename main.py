print("Program starting.\n")
word = input("Insert a closed compound word: ")

reversed_word = word[::-1]
word_length = len(word)
last_char = word[-1]

print(f"The word you inserted is '{word}' and in reverse it is '{reversed_word}'.")
print(f"The inserted word length is {word_length}")
print(f"Last character is '{last_char}'\n")
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

substring = word[start:end:step]
print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")
print("Program ending.")
```[cite: 3]

* **String Reversal**: Uses slice notation `[::-1]` to reverse the input word[cite: 3].
* **Length & Character Retrieval**: Uses `len()` to get the word length and indexing (`[-1]`) to grab the last character[cite: 3].
* **Dynamic Slicing**: Prompts the user for integers representing the starting point, ending point, and step size to slice the substring dynamically[cite: 3].
