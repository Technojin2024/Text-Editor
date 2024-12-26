
print("Welcome to the Basic Text Editor!")
print("Please enter your text:")
text = input("> ")

#Display Menu of Operations
print("Choose an Operation:")
print("1. Convert to Uppercase")
print("2. Convert to Lowercase")
print("3. Replace a Word")
print("4. Find a Substring")
print("5. Split into Words")
print("6. Join Words with a Delimiter")
print("7. Check Start and End")
print("8. Exit")
    

while True:
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        result = text.upper()
        print("Uppercase:", result)

    elif choice == '2':
        result = text.lower()
        print("Lowercase:", result)

    elif choice == '3':
        old_word = input("Enter the word to replace: ")
        new_word = input("Enter the new word: ")
        result = text.replace(old_word, new_word)
        print("Updated Text:", result)

    elif choice == '4':
        substring = input("Enter the substring to find: ")
        position = text.find(substring)
        if position != -1:
            print(f"'{substring}' found at position {position}")
        else:
            print(f"'{substring}' not found")

    elif choice == '5':
        words = text.split()
        print("Words:", words)

    elif choice == '6':
        delimiter = input("Enter the delimiter to use: ")
        result = delimiter.join(words)
        print("Joined Text:", result)

    elif choice == '7':
        start_word = input("Enter the starting substring: ")
        end_word = input("Enter the ending substring: ")
        starts = text.startswith(start_word)
        ends = text.endswith(end_word)
        print(f"Starts with '{start_word}': {starts}")
        print(f"Ends with '{end_word}': {ends}")

    elif choice == '8':
        print("Exiting the Text Editor. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
   

    