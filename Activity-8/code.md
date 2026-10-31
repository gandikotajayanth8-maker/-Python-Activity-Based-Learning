# Case Study: Repeated Word and Phrase Detection

## 1. Problem Statement

Develop a Python program to process a paragraph and identify repeated words. The program should convert all words into lowercase, count the occurrences of each word, and display repeated words along with their positions in the paragraph.

## 2. Algorithm

1. Start the program.
2. Read a paragraph from the user.
3. Convert the paragraph into lowercase.
4. Remove common punctuation marks.
5. Split the paragraph into a list of words.
6. Create an empty list to store repeated words.
7. Check each word and count its occurrences.
8. If a word occurs more than once, display the word, its count, and its positions.
9. Stop the program.

## 3. Flowchart
 ```mermaid
flowchart TD
    A([Start]) --> B[/Enter paragraph/]
    B --> C[Convert paragraph to lowercase]
    C --> D[Remove punctuation marks]
    D --> E[Split paragraph into words]
    E --> F[Check each word]
    F --> G[Count word occurrences]
    G --> H{Count greater than 1?}
    H -- Yes --> I[Find word positions]
    I --> J[Display word, count and positions]
    H -- No --> K{More words?}
    J --> K
    K -- Yes --> F
    K -- No --> L([Stop])
```

## 4. Python Source Code

```
# Repeated Word and Phrase Detectionparagraph = input("Enter a paragraph: ")# Convert paragraph into lowercaseparagraph = paragraph.lower()# Remove punctuation marksfor mark in ".,!?;:":    paragraph = paragraph.replace(mark, "")# Split paragraph into wordswords = paragraph.split()print("\nRepeated Words and Their Positions:")found = False# Check each wordfor word in words:    if words.count(word) > 1 and word not in words[:words.index(word)]:        positions = []        # Find positions of the word        for i in range(len(words)):            if words[i] == word:                positions.append(i + 1)        print(f"{word} - Count: {words.count(word)}, Positions: {positions}")        found = Trueif not found:    print("No repeated words found.")
```

## 5. Sample Input

```
Enter a paragraph: Python is easy and Python is useful. Learning Python is fun.
```

## 6. Sample Output

```
Repeated Words and Their Positions:
python - Count: 3, Positions: [1, 5, 9]
is - Count: 3, Positions: [2, 6, 10]
```

## 7. Mermaid Flowchart Code
 
<img width="1258" height="1510" alt="mermaid-diagram (9)" src="https://github.com/user-attachments/assets/b68d49b9-cda3-422b-bec7-2c41cf9c9c6b" />

 
