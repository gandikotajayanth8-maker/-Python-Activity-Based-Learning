 

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

start_day = int(input("Enter starting weekday (0-6): "))
total_days = int(input("Enter number of days in month: "))

 
if start_day < 0 or start_day > 6:
    print("Invalid starting weekday.")

elif total_days not in [28, 29, 30, 31]:
    print("Invalid number of days.")

else:
    print("\n      MONTHLY CALENDAR")

 
    for day in days:
        print(day, end=" ")

    print()

 
    for i in range(start_day):
        print("    ", end="")

  
    date = 1

    for week in range(6):
        for day in range(7):
            if date <= total_days:
                if week == 0 and day < start_day:
                    continue

                print(f"{date:3}", end=" ")
                date += 1
            else:
                break

        print()

        if date > total_days:
            break
