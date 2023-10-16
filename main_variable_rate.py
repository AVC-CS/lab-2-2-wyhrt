def main():
    workhours = float(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = float(input('Enter your hourly pay: '))
    ov_rate = reg_rate*1.5

   ##################################################
   # Code your program here
   ##################################################
    overtime = workhours - reg_hours
    overtime_wage = overtime * ov_rate
    regular_wage = reg_hours * reg_rate
    total_wage = regular_wage + overtime_wage

    print(f"Regular hours: {reg_hours} Regular Pay: {regular_wage}")
    if(overtime>0):
        print(f"Overtime hours: {overtime} Overtime Pay: {overtime_wage:.2f}")
        print(f"Week's Wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
