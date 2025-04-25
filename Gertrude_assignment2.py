#Budget exceedance checker

monthly_budget = float(input("How much do you want to budget this month?\n"))
total_monthly_expenses = float(input("What is your total monthly expense?\n"))



if total_monthly_expenses == monthly_budget:
    print(f"You are good to go for the month, you are exactly on budget with {total_monthly_expenses}")
    
elif total_monthly_expenses < monthly_budget:
    print(f"You are good to go for the month, you are within budget with {total_monthly_expenses}")        
else:
    extra_cash = total_monthly_expenses - monthly_budget
    print(f"You're over budget, you need an extra {extra_cash}")
    
    
