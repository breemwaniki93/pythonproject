def is_palindrome(word):

    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    # Check if the word is the same when reversed
    return word == word[::-1]



if __name__ == "__main__":
    # Test cases
    test_words = ["Racecar", "Hello", "madam", "level", "world"]

    for word in test_words:
        if is_palindrome(word):
            print(f"'{word}' is a palindrome.")
        else:
            print(f"'{word}' is not a palindrome.")
