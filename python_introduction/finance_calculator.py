#Prompt user for their monthly income and total expenses monthly
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter total monthly expenses: "))

#Calculate monthly expenses
monthly_savings = monthly_income - total_monthly_expenses

#Calculate projected savings after one year
interest_rate = 5/100
principal = monthly_savings
number_of_times_interest_compounded = 12
annual_savings = principal  * number_of_times_interest_compounded + principal * interest_rate * number_of_times_interest_compounded

annual_savings_round = round(annual_savings)

#Result is
print(f'''Your monthly savings are {monthly_savings}.\nProjected savings after one year, with interest, is: {annual_savings_round}''')

