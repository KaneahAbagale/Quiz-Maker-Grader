
# Python program that stores and analyzes employees data
# total sales, average sales, highest sales, identify and display name of top performing employee 

emp1 = 10
emp2 = 4
emp3 = 7
emp4 = 9
emp5 = 12

#top_employee = "emp1", "emp2", "emp3", "emp4", "emp5"

# sum of total sales
total_sale = emp1 + emp2 + emp3 + emp4 + emp5
print(f"The total sales is {total_sale}")

# average number of sales across all employees
average_sales =  (emp1 + emp2 + emp3 + emp4 + emp5) / 5
print(f"The average number of sales {average_sales}")

# highest sales in the team
highest_sales = max(emp1, emp2, emp3, emp4, emp5)
print(f"The highest sales in the team is {highest_sales}")

#Top performing employee
if highest_sales == emp1:
    top_employee = "emp1"
elif highest_sales == emp2:
    top_employee = "emp2"
elif highest_sales == emp3:
    top_employee = "emp3"
elif highest_sales == emp4:
    top_employee = "emp4"
elif highest_sales == emp5:
    top_employee = "emp5"
    
    print("Top Performing Employee is", top_employee)
    
  


