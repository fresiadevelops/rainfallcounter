def rainfall_calculator():
    # Request from user the number of years
    years = int(input("Enter the number of years: "))
    total_rainfall = 0
    total_months = years * 12

    # Each year-Outer loop
    for year in range(1, years + 1):
        print(f"Year {year}:")
        # each month-inner loop
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"  Enter the inches of rainfall for month {month}: "))
                    if rainfall < 0:
                        print("    Rainfall cannot be negative. Try again.")
                        continue
                    total_rainfall += rainfall
                    break
                except ValueError:
                    print("    Invalid input. Please enter a numeric value.")

    # average rainfall calculation
    average_rainfall = total_rainfall / total_months

    # results
    print("\nRainfall Statistics:")
    print(f"  Total months: {total_months}")
    print(f"  Total inches of rainfall: {total_rainfall:.2f}")
    print(f"  Average rainfall per month: {average_rainfall:.2f}")

rainfall_calculator()
