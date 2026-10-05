import dow


def getDayOfTheWeekForUserDate():
    """Prompts the user for year, month, and day, then prints the resulting day of the week."""
    print("\n--- Custom Date Day of the Week Finder ---")
    
    year_input = input("Please enter the year: ")
    month_input = input("Please enter the month (1-12): ")
    day_input = input("Please enter the day (1-31): ")
    
    # Validate user inputs using string methods covered in Lesson 3
    is_valid_input = (year_input.isnumeric() and 
                      month_input.isnumeric() and 
                      day_input.isnumeric())
    
    if is_valid_input:
        year = int(year_input)
        month = int(month_input)
        day = int(day_input)
        
        day_of_week = dow.getDayOfTheWeek(year, month, day)
        print(f"The date {month}-{day}-{year} is a {day_of_week}.")
    else:
        print("Invalid input detected. Please enter numeric values only.")


def main():
    # 1. Invoke makeCalendar() to list all dates and days of the week for 2026
    print(f"Generating calendar list for {dow.TARGET_YEAR}...")
    dow.makeCalendar()
    
    # 2. Prompt user for custom date lookup
    getDayOfTheWeekForUserDate()


if __name__ == "__main__":
    main()