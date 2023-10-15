#Initialize the variables
total_rainfall = 0
total_months = 0

#Get years
num_years = int(input("Enter the number of years: "))

#Loop and branch
for year in range(1, num_years + 1):
    for month in range(1, 13):
        #Input rainfall
        rainfall = float(input(f"Enter the inches of rainfall for Year {year}, Month {month}: "))
        total_rainfall += rainfall
        total_months += 1

#Calculate average
average_rainfall = total_rainfall / total_months

#Display
print("\nNumber of months:", total_months)
print("Total inches of rainfall:", total_rainfall)
print("Average rainfall per month:", average_rainfall)
