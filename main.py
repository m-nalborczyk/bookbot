def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        words = file_contents.split()
        num_words = len(words)
        print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in document\n")

        file_contents_lowercase = file_contents.lower()
        
        char_count = count_chars(file_contents_lowercase)
        
        # Convert dictionary to a list of dictionaries
        char_list = [{"char" : char, "count" : count} for char, count in char_count.items() if char.isalpha()]
        # Sort the list by character (key) in alphabetical order
        char_list.sort(key=sort_on)
        # Print formatted output
        for item in char_list:
            print(f"The '{item["char"]}' character was found {item["count"]} times")
        print("--- End report ---")
        # print(count_chars(file_contents_lowercase))

def count_chars(book):
    char_count = {}
    for char in book:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(item):
    return item["char"]

main()