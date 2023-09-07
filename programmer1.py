from inheritancedemo import Employee

emp = Employee()
emp.setid(101)
emp.setName("Poonam")
emp.setAddress("Pune")
emp.setSalary(55000.23)

print("ID:",emp.getid())
print("Name:",emp.getName())
print("Address",emp.getAddress())
print("Salary:",emp.getSalary())