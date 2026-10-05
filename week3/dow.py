# Constants to avoid magic numbers and improve readability
DAYS_IN_A_WEEK = 7
TWELVES_DIVISOR = 12
FOURS_DIVISOR = 4

CENTURY_1600 = 16
CENTURY_1700 = 17
CENTURY_1800 = 18
CENTURY_2000 = 20
CENTURY_2100 = 21

OFFSET_1600 = 6
OFFSET_1700 = 4
OFFSET_1800 = 2
OFFSET_2000 = 6
OFFSET_2100 = 4
OFFSET_DEFAULT = 0

LEAP_SUBTRACTION = 1
TARGET_YEAR = 2026


def isLeapYear(year):
    """Returns True if the given year is a leap year, False otherwise."""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def getMonthCode(month):
    """Returns the corresponding month code used in the day-of-the-week algorithm."""
    if month == 1:
        return 1
    elif month == 2:
        return 4
    elif month == 3:
        return 4
    elif month == 4:
        return 0
    elif month == 5:
        return 2
    elif month == 6:
        return 5
    elif month == 7:
        return 0
    elif month == 8:
        return 3
    elif month == 9:
        return 6
    elif month == 10:
        return 1
    elif month == 11:
        return 4
    elif month == 12:
        return 6
    else:
        return 0


def getDayName(day_index):
    """Converts a numerical remainder index (0-6) into the corresponding day name."""
    if day_index == 0:
        return "Saturday"
    elif day_index == 1:
        return "Sunday"
    elif day_index == 2:
        return "Monday"
    elif day_index == 3:
        return "Tuesday"
    elif day_index == 4:
        return "Wednesday"
    elif day_index == 5:
        return "Thursday"
    elif day_index == 6:
        return "Friday"
    else:
        return "Unknown"


def getCenturyOffset(year):
    """Determines and returns the century offset required for the algorithm."""
    century_prefix = year // 100
    
    if century_prefix == CENTURY_1600:
        return OFFSET_1600
    elif century_prefix == CENTURY_1700:
        return OFFSET_1700
    elif century_prefix == CENTURY_1800:
        return OFFSET_1800
    elif century_prefix == CENTURY_2000:
        return OFFSET_2000
    elif century_prefix == CENTURY_2100:
        return OFFSET_2100
    else:
        return OFFSET_DEFAULT


def getDayOfTheWeek(year, month, day):
    """Calculates and returns the day of the week string for any given date."""
    last_two_digits = year % 100
    twelves_count = last_two_digits // TWELVES_DIVISOR
    remainder_after_twelves = last_two_digits % TWELVES_DIVISOR
    fours_count = remainder_after_twelves // FOURS_DIVISOR
    
    month_code = getMonthCode(month)
    century_offset = getCenturyOffset(year)
    
    # Add all components together (Step 6)
    total_sum = (twelves_count + remainder_after_twelves + fours_count + 
                 day + month_code + century_offset)
    
    # Special offset for January and February dates in leap years
    is_jan_or_feb = (month == 1 or month == 2)
    if is_jan_or_feb and isLeapYear(year):
        total_sum = total_sum - LEAP_SUBTRACTION
        
    day_index = total_sum % DAYS_IN_A_WEEK
    return getDayName(day_index)


def getDaysInMonth(year, month):
    """Returns the total number of days in a specified month and year."""
    is_february = (month == 2)
    is_thirty_day_month = (month == 4 or month == 6 or month == 9 or month == 11)
    
    if is_february:
        if isLeapYear(year):
            return 29
        else:
            return 28
    elif is_thirty_day_month:
        return 30
    else:
        return 31


def makeCalendar():
    """Prints out the date and day of the week for every single day in 2026."""
    for month in range(1, 13):
        days_in_current_month = getDaysInMonth(TARGET_YEAR, month)
        for day in range(1, days_in_current_month + 1):
            day_name = getDayOfTheWeek(TARGET_YEAR, month, day)
            print(f"{month}-{day}-{TARGET_YEAR} is a {day_name.lower()}.")