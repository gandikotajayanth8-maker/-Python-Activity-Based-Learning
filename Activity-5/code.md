# Case Study No. 31: String-Based Examination Answer Evaluation

## 1. Problem Statement

Develop a Python program to evaluate students' examination answers by comparing their answer strings with a predefined answer key.

The program should calculate the number of correct, incorrect, and unanswered questions. It should apply negative marking for incorrect answers and calculate the final score. Finally, it should display the student's examination result.

## 2. Algorithm

1. Start the program.
2. Enter the student's name.
3. Enter the number of questions.
4. Enter the correct answer key.
5. Enter the student's answers.
6. Initialize correct, incorrect, and unanswered counts to zero.
7. Compare each student's answer with the answer key using a loop.
8. If the answer matches, increase the correct count.
9. If the answer is blank, increase the unanswered count.
10. Otherwise, increase the incorrect count.
11. Apply negative marking for incorrect answers.
12. Calculate the final score.
13. Display correct, incorrect, unanswered answers, and final score.
14. Stop the program.

## 3. Flowchart
 ```mermaid

flowchart TD
    A([Start]) --> B[/Enter student name and number of questions/]
    B --> C[/Enter answer key and student answers/]
    C --> D[Initialize correct, incorrect and unanswered]
    D --> E[Compare student answer with answer key]
    E --> F{Is answer blank?}
    F -->|Yes| G[Increase unanswered count]
    F -->|No| H{Is answer correct?}
    H -->|Yes| I[Increase correct count]
    H -->|No| J[Increase incorrect count]
    G --> K{All questions checked?}
    I --> K
    J --> K
    K -->|No| E
    K -->|Yes| L[Calculate final score]
    L --> M[/Display examination result/]
    M --> N([Stop])
```

## 4. Python Source Code

Rules used:

- Correct answer: +1 mark.
- Incorrect answer: -0.25 mark.
- Unanswered question: 0 marks.
- Answers are compared without considering uppercase or lowercase letters.

```
name = input("Enter student name: ")n = int(input("Enter number of questions: "))answer_key = []student_answers = []print("\nEnter correct answers:")for i in range(n):    ans = input(f"Question {i+1}: ")    answer_key.append(ans.strip().upper())print("\nEnter student answers (Press Enter to skip):")for i in range(n):    ans = input(f"Question {i+1}: ")    student_answers.append(ans.strip().upper())correct = 0incorrect = 0unanswered = 0for i in range(n):    if student_answers[i] == "":        unanswered += 1    elif student_answers[i] == answer_key[i]:        correct += 1    else:        incorrect += 1score = (correct * 1) - (incorrect * 0.25)print("\n----- EXAMINATION RESULT -----")print("Student Name:", name)print("Total Questions:", n)print("Correct Answers:", correct)print("Incorrect Answers:", incorrect)print("Unanswered Questions:", unanswered)print("Negative Marks:", incorrect * 0.25)print("Final Score:", score)
```

## 5. Sample Input

```
Enter student name: Ravi
Enter number of questions: 5

Enter correct answers:
Question 1: A
Question 2: B
Question 3: C
Question 4: D
Question 5: A

Enter student answers (Press Enter to skip):
Question 1: A
Question 2: C
Question 3: C
Question 4:
Question 5: B
```

## 6. Sample Output

```
----- EXAMINATION RESULT -----
Student Name: Ravi
Total Questions: 5
Correct Answers: 2
Incorrect Answers: 2
Unanswered Questions: 1
Negative Marks: 0.5
Final Score: 1.5
```

## 7. Additional Test Cases

| Test case | Correct | Incorrect | Unanswered | Final score |
| --------- | ------- | --------- | ---------- | ----------- |
| 1         | 5       | 0         | 0          | 5.00        |
| 2         | 3       | 2         | 0          | 2.50        |
| 3         | 2       | 1         | 2          | 1.75        |
| 4         | 0       | 5         | 0          | -1.25       |
| 5         | 0       | 0         | 5          | 0.00        |

## 8. Mermaid Flowchart Code
<img width="1448" height="2382" alt="mermaid-diagram (6)" src="https://github.com/user-attachments/assets/49eadb98-c966-4fd8-afd6-ad2f3151b592" />

 
## 9. Conclusion

The String-Based Examination Answer Evaluation program compares student answers with the correct answer key. It calculates correct, incorrect, and unanswered questions and applies negative marking for incorrect answers. It also displays the final examination score. This program demonstrates Python strings, lists, loops, conditional statements, and arithmetic operators.

Python concepts used:

- Variables and data types
- Strings and string methods
- Lists
- For loops
- If-elif-else statements
- Arithmetic operators
