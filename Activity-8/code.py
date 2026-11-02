paragraph = input("Enter a paragraph: ")
 
paragraph = paragraph.lower()

 
for mark in ".,!?;:":
    paragraph = paragraph.replace(mark, "")

 
words = paragraph.split()

print("\nRepeated Words and Their Positions:")

found = False

 
for word in words:
    if words.count(word) > 1 and word not in words[:words.index(word)]:

        positions = []

           for i in range(len(words)):
            if words[i] == word:
                positions.append(i + 1)

        print(f"{word} - Count: {words.count(word)}, Positions: {positions}")
        found = True

if not found:
    print("No repeated words found.")
