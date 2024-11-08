import mysql.connector

# Function to connect to the database
def connect_db():
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host="localhost",        # MySQL server address (localhost is common if running MySQL locally)
            user="root",             # Your MySQL username (for example, 'root' is the default on many systems)
            password="Wills@0001",     # Your MySQL password (replace with the password you set)
            database="employee_db"   # Your database name (you should create this database beforehand in MySQL)
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to add a new employee
def add_employee():
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = int(input("Enter employee salary: "))
    
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Employees (name, position, salary) VALUES (%s, %s, %s)", (name, position, salary))
        connection.commit()
        print("Employee added successfully.")
        cursor.close()
        connection.close()

# Function to view all employees
def view_employees():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Employees")
        rows = cursor.fetchall()
        print("Employees List:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}")
        cursor.close()
        connection.close()

# Function to edit employee details
def edit_employee():
    employee_id = int(input("Enter employee ID to edit: "))
    name = input("Enter new name: ")
    position = input("Enter new position: ")
    salary = int(input("Enter new salary: "))
    
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE Employees
            SET name = %s, position = %s, salary = %s
            WHERE id = %s
        """, (name, position, salary, employee_id))
        connection.commit()
        print("Employee details updated successfully.")
        cursor.close()
        connection.close()

# Function to delete an employee
def delete_employee():
    employee_id = int(input("Enter employee ID to delete: "))
    
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Employees WHERE id = %s", (employee_id,))
        connection.commit()
        print("Employee deleted successfully.")
        cursor.close()
        connection.close()

# Main function to navigate between operations
def main():
    while True:
        print("\nEmployee Database Operations")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Edit Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            edit_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
