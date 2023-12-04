def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    user_input = input("Enter text (or specify file path): ")

    try:
        # Trying to open a file and read its criteria if the user entered a file path
        with open(user_input, 'r') as file:
            file_content = file.read()
            word_count = count_words(file_content)
            print(f"Number of words in file: {word_count}")

    except FileNotFoundError:
        # If the file is not found, count the words in the entered string
        word_count = count_words(user_input)
        print(f"Number of words in the text: {word_count}")
