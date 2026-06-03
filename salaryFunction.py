def ShowSalary(salary):
    print("Salary: ", salary)
    # Allowance is 10% of salary
    allowance = salary * 0.1
    print("Allowance: ", allowance)
    # Total salary is salary + allowance
    total_salary = salary + allowance
    print("Total Salary: ", total_salary)   

# Example usage 
print("Example usage of ShowSalary function:")
ShowSalary(50000)