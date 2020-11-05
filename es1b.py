# Test Case 1
# Enter your starting annual salary: 120000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 500000
# Enter the semi­annual raise, as a decimal: .03
# Number of months: 142
#
# Test Case 2
# Enter your starting annual salary: 80000
# Enter the percent of your salary to save, as a decimal: .1
# Enter the cost of your dream home: 800000
# Enter the semi­annual raise, as a decimal: .03
# Number of months: 159
#
# Test Case 3
# Enter your starting annual salary: 75000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 1500000
# Enter the semi­annual raise, as a decimal: .05
# Number of months: 261


if __name__ == '__main__':
    annual_salary = int(input("Enter your starting annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))
    semi_annual_rise = float(input("Enter the semi-annual raise, as a decimal: "))

    monthly = (annual_salary / 12.0) * portion_saved
    portion_down_payment = total_cost * 0.25

    current_savings = 0.0
    r = 0.04
    months = 0

    while current_savings < portion_down_payment:
        months += 1
        monthly_inc = current_savings * (r / 12)
        current_savings += monthly_inc + monthly

        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_rise
            monthly = (annual_salary / 12.0) * portion_saved
    print("Number of months:", months)
