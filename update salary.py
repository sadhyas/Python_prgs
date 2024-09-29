class Employee:
    def __init__(self,di,name,dept,salary):
        self.di = di
        self.name =name
        self.dept =dept
        self.salary= salary
    def upsalary (emp_list):
        ch_dept=input('enter the dept for updating salary:').strip()
        count=0
        for j in emp_list:
            if (j.dept.strip()==ch_dept):
                print("For Employee ",j.name)
                j.salary=int(input("enter the salary to update of employee:"))
                count+=1
            else:
                if count==0:
                    print("Invalid Dept")
                    pass
        print('Emp_id\t' , 'Exp_Name\t', 'Department\t', 'Salary')
        for k in emp_list:
            print (k.di,'\t',k.name, '\t\t',k.dept, '\t\t',k.salary)

emp_list=[]

n=int(input("enter the no of employees:"))

for i in range(n):
    di=int (input("Enter Id:"))
    name = input ("Enter Name:")
    dept = input("Enter Dept: ")
    salary = int(input("Enter Salary:"))
    emp_list.append(Employee(di,name,dept,salary))
Employee.upsalary (emp_list)
