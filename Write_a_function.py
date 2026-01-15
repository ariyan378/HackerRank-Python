def is_leap(year):

    if year%4==0 and year%100!=0:
        return 'True'
    if year%400==0:
         return 'True'
    else:
        return 'False'
    # Write your logic here


year = int(input())

is_leap(year)