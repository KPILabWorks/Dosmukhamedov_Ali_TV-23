def get_top_words():
    with open("pr1/killme.txt", 'r') as file:
        text = file.read().lower()

    current_word = ""
    words = []

    for char in text:
        # check is character is a letter and append to current word
        if char.isalpha():
            current_word += char
        elif current_word:
            # if the character is not a letter, put the word into the list
            words.append(current_word)
            current_word = ""

    # if the file ends abruptly, adds the last word
    if current_word:
        words.append(current_word)

    word_counts = {}
    for word in words:
        
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=lambda word_and_count: word_and_count[1], reverse=True)

    return sorted_words[:5]


print(get_top_words())


