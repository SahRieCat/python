'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

# investment amount
user_investment_amount = input("type in your investment amount ")
a = float(user_investment_amount)

# interest rate in percentage
user_interest_rate_in_percentage = input("type in your interest rate (in percentage) ")
b = float(user_interest_rate_in_percentage)
b_precent = b/100

# number of years to invest
user_number_of_years_to_invest = input("type in the number of years you have to invest ")
c = int(user_number_of_years_to_invest)

Future_investment_values = a*(1+b_precent)**c

#Print the future values to the console.
print("Your future investment value will be",Future_investment_values ,"Dollars")
