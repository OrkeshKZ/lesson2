# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def is_year_leap(year):
    year = int(input())
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True
print(is_year_leap(2000))
