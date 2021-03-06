# Test Case 1
# Enter your annual salary: 120000
# Enter the percent of your salary to save, as a decimal: .10
# Enter the cost of your dream home: 1000000
# Number of months: 183
#
# Test Case 2
# Enter your annual salary: 80000
# Enter the percent of your salary to save, as a decimal: .15
# Enter the cost of your dream home: 500000
# Number of months: 105

if __name__ == '__main__':
    current_savings = 0.0
    annual_return = 0.04
    months = 0

    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    portion_saved = (annual_salary / 12.0) * portion_saved
    total_cost = int(input("Enter the cost of your dream home: "))
    portion_down_payment = total_cost * 0.25

    while current_savings < portion_down_payment:
        months += 1
        monthly = current_savings * (annual_return / 12)
        current_savings += monthly + portion_saved

    print("Number of months:", months)
