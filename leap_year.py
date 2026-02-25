# checking which year is leap year and which isnot
year=int(input("enter ur year to determine leap year"));
if(year%4==0):
    if(year%100==0):

        if(year%400==0):
            print("ur year is leap year",year);
        else:
            print("not leap year");
    else:
        print("leap year")
else:
    print("not leap year");