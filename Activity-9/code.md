# Case Study: Nested Loop Calendar Generator

## 1. Problem Statement

Develop a Python program to generate a formatted monthly calendar using the starting weekday and the number of days in a month supplied by the user. The program should correctly align the dates under the weekdays and display the calendar in a table format. It should also validate the starting weekday and the number of days.

## 2. Algorithm

1. Start the program.
2. Display the days of the week.
3. Read the starting weekday (0–6) from the user.
4. Read the number of days in the month.
5. Check whether the starting weekday and month length are valid.
6. Print the weekday headings.
7. Use a nested loop to generate the calendar.
8. Print blank spaces before the first date.
9. Display the dates in the correct weekday columns.
10. Move to a new line after Saturday.
11. Stop the program.

Weekday numbers:

- 0 – Sunday
- 1 – Monday
- 2 – Tuesday
- 3 – Wednesday
- 4 – Thursday
- 5 – Friday
- 6 – Saturday

## 3. Flowchart

 ```mermaid
flowchart TD
    A([Start]) --> B[/Enter starting weekday and total days/]
    B --> C{Is weekday between 0 and 6?}
    C -- No --> D[Display invalid weekday]
    C -- Yes --> E{Are days 28, 29, 30 or 31?}
    E -- No --> F[Display invalid month length]
    E -- Yes --> G[Print weekday headings]
    G --> H[Print blank spaces before first date]
    H --> I[Set date = 1]
    I --> J[Start outer loop for weeks]
    J --> K[Start inner loop for weekdays]
    K --> L{Date less than or equal to total days?}
    L -- Yes --> M[Print date]
    M --> N[Increment date]
    N --> O{More weekdays?}
    O -- Yes --> K
    O -- No --> P[Move to next line]
    P --> Q{All dates printed?}
    Q -- No --> J
    Q -- Yes --> R([Stop])
    L -- No --> R
    D --> R
    F --> R
```
## 4. Python Source Code

```
# Nested Loop Calendar Generatordays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]start_day = int(input("Enter starting weekday (0-6): "))total_days = int(input("Enter number of days in month: "))# Validate inputif start_day < 0 or start_day > 6:    print("Invalid starting weekday.")elif total_days not in [28, 29, 30, 31]:    print("Invalid number of days.")else:    print("\n      MONTHLY CALENDAR")    # Print weekday headings    for day in days:        print(day, end=" ")    print()    # Print empty spaces before first date    for i in range(start_day):        print("    ", end="")    # Print dates using nested loops    date = 1    for week in range(6):        for day in range(7):            if date <= total_days:                if week == 0 and day < start_day:                    continue
```

## 5. Sample Input

```
Enter starting weekday (0-6): 3
Enter number of days in month: 31
```

Here, `3` represents Wednesday.

## 6. Sample Output

```
      MONTHLY CALENDAR
Sun Mon Tue Wed Thu Fri Sat
              1   2   3   4
  5   6   7   8   9  10  11
 12  13  14  15  16  17  18
 19  20  21  22  23  24  25
 26  27  28  29  30  31
```

## 7. Mermaid Flowchart Code

<img width="2096" height="2776" alt="mermaid-diagram (10)" src="https://github.com/user-attachments/assets/ac4300d2-ec30-4f74-9db6-fe604e2e5447" />

 
Conclusion: This program uses nested `for` loops to generate a monthly calendar. It aligns dates according to the starting weekday and validates the number of days in the month.
