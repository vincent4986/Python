"""
NAME: WASSWA VINCENT
STUDENT NO: 214018980
REG NO: 14/U/15890/EVE
"""

import calendar
print("This Program is intended to produce the exact date you were born")
print("................................................................")
dy = mth = yr = None
#PROGRAM ACCEPTS INTEGER TYPE VARIABLES

#while True:
while(dy == None):
    try:
        dy = int(input("Please type in your day: "))
        while(dy not in range(1, 32)):
            print("this is not a day")
            dy = int(input("Please type in your day: "))

    except:
        print("Please type in numbers only others exit if you dont know what you are doing")
        print()

while(mth == None):
    try:
        mth = int(input("Please type in your month: "))
        while(mth not in range(1, 13)):
            print("Mr or Lady, months move from Jan, To December. thats twelve, not %d or whatever you've input" % mth)
            mth = int(input("Please type in your month AGAIN: "))

    except:
        print("Please type in numbers only")
        print()

while(yr == None):
    try:
        yr = int(input("Please type in your year: "))
        while(yr not in range(1000, 2500)):
            if(yr >= 2500):
                print("PLEASE TRY AGAIN")
                yr = int(input("Please type in your year: "))
            if(yr < 1000):
                print("PLEASE TRY AGAIN")
                yr = int(input("Please type in your year: "))

    except:
        print("Please type in numbers only")
        print()

#you can try playing with the program by inputing strings

#the day in form of numbers from 0 - 6
dte = calendar.weekday(yr, mth, dy)
exact = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("You were born on ", exact[dte])


input("press Enter to exit")
input("SEE YOU AGAIN")
