def count_words(book):
    word_count = book.split()
    return len(word_count)

def count_letters(book):
    letter_counts = {}
    
    all_words = book.split()
    for word in all_words:
        for char in word:
            if not char.isalpha():
                continue
            letter = char.lower()
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    counts_list = []
    for letter, count in letter_counts.items():
        counts_list.append({"letter": letter, "count": count})

    return counts_list


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    letter_counts = count_letters(file_contents)
    letter_counts.sort(reverse=True, key=lambda x : x["count"])

    print(f"--- Begin report of frankenstein.txt ---")
    print(f"{word_count} words found in document")

    for each in letter_counts:
        print(f"The '{each["letter"]}' was found {each["count"]} times")
    print("--- End report ---")

main()