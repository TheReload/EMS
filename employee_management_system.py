# Employee Management System (EMS)

# Sample data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Riya', 'age': 30, 'department': 'Finance', 'salary': 60000}
}


# Function to display the main menu
def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye!")
            quit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Function to add a new employee
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
            return

        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print(f"Employee {name} added successfully.")
    except ValueError:
        print("Invalid input. Please enter correct data types.")


# Function to view all employees
def view_employees():

    try:
        print("\n{:<10} {:<15} {:<10} {:<15} {:<10}".format("Emp ID", "Name", "Age", "Department", "Salary"))
        print("-" * 60)
        for emp_id, details in employees.items():
            print("{:<10} {:<15} {:<10} {:<15} {:<10}".format(
                emp_id, details['name'], details['age'], details['department'], details['salary']
            ))
    except AttributeError:
        print("No employees available.")
    main_menu()


# Function to search for an employee
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"\nEmployee ID: {emp_id}")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric Employee ID.")


if __name__ == "__main__":
    main_menu()
