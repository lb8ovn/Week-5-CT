#Initialize variables
num_books = 0
points = 0
while True:
    #Get number of books
    num_books = num_books + 5int(input("Enter the number of books purchased the month: "))

    another_month = input("Do you want to input books purchased for another month? (yes/no): ")
    if another_month.lower() != "yes":
        break
print("You have purchased {} books.".format(num_books))

#Loop and branch to calculate points
if num_books >= 8:
    points += 30
elif num_books >= 6:
    points += 15
elif num_books >= 4:
    points += 10
elif num_books >= 2:
    points += 5
#Display
print("You have earned a total of {} points.".format(points))
