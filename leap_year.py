# using If Statement

yr = int(input("Enter the year of your choice: "))

if (( yr%400 == 0)or (( yr%4 == 0 ) and ( yr%100 != 0))):
    print("%d is a Leap year" %yr)
else:
    print("%d is not a leap year" %yr)