from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found\n')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found\n')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}\n')
    except Exception as exc:
        print(f"Error creating department: {exc}\n")


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}\n')
        except Exception as exc:
            print(f"Error updating department: {exc}\n")
    else:
        print(f'Department {id_} not found\n')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted\n')
    else:
        print(f'Department {id_} not found\n')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f'Employee {name} not found.\n'
    )


def find_employee_by_id():
    id = input("Enter the employee's ID: ")
    employee = Employee.find_by_id(id)
    print(employee) if employee else print(
        f'Employee {id} not found\n'
    )


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = int(input("Enter the employee's department ID: "))
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')
    except Exception as exc:
        print(f"Error creating employee: {exc}\n")


def update_employee():
    id = input("Enter the employee's ID: ")
    
    if employee := Employee.find_by_id(id):
        try:
            name = input(f"Enter {employee.name}'s new name: ")
            employee.name = name
            job_title = input(f"Enter {employee.name}'s new job title: ")
            employee.job_title = job_title
            department = int(input(f"Enter {employee.name}'s new department id: "))
            employee.department_id = department
            employee.update()
            print(f"Success: {employee}\n")
        except Exception as exc:
            print(f"Error updating employee: {exc}\n")
    else:
        print(f"Employee {id} not found.\n")


def delete_employee():
    id = input("Enter employee's id: ")
    if employee := Employee.find_by_id(id):
        employee.delete()
        print(f"Employee {id} deleted. \n")
    else:
        print(f"Employee {id} not found. \n")


def list_department_employees():
    department_id = input("Enter a department ID: ")
    if department := Department.find_by_id(department_id):
        for employee in department.employees():
            print(employee)
        print("\n")
    else: print(f"Department {department_id} not found.\n")