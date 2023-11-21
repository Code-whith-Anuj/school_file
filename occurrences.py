#Write a program (WAP) to print the number of occurrences of a given alphabet in each string.

def count_occurrences(word_list, alphabet):
    for word in word_list:
        count = word.count(alphabet)
        print(f"The alphabet '{alphabet}' occurs {count} times in '{word}'")

# Test the function
words = ["hello", "world", "python", "programming"]
alphabet = 'o'
count_occurrences(words, alphabet)