## Generalized `Vector` Class  

**Objective**: Create a Python class `Vector` that represents a mathematical vector in an n-dimensional space, capable of handling any number of dimensions.

### **Task Description**

1. **Create a `Vector` class** that represents a vector in an n-dimensional space.  
   - The class should support vectors of any number of dimensions, defined by an arbitrary number of components provided during initialization.

2. The class should provide functionality to:
   - Perform vector operations such as addition, subtraction, and dot product.
   - Handle scalar multiplication.
   - Compute the magnitude (length) of the vector.
   - Normalize the vector (return the unit vector).

3. The class should have methods for:
   - Representing the vector as a string for easy display.
   - Handling operations between vectors of the same dimension and raising appropriate errors when vectors of different dimensions are involved.

### **Example Usage**
```python
# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)
```
---

## Employee Records Manager (OOP Version)
**Objective**: Create a program to manage employee records using classes and file handling.

### **Tasks and Requirements**

1. **Class Design**  
   - Create a class `Employee` to represent individual employees with the following attributes:
     - `employee_id`
     - `name`
     - `position`
     - `salary`
   - Create a class `EmployeeManager` to handle operations such as adding, viewing, searching, updating, and deleting employee records. This class will manage the file **"employees.txt"**.

2. **File Handling**  
   - All employee records should be stored in **"employees.txt"**.  
   - Each operation (add, view, update, delete) should interact with the file to ensure data persistence.

3. **Menu Options**  
   Implement a menu within the `EmployeeManager` class with the following options:
   ```
   1. Add new employee record
   2. View all employee records
   3. Search for an employee by Employee ID
   4. Update an employee's information
   5. Delete an employee record
   6. Exit
   ```

4. **Functional Requirements**  
   - **Option 1**: Add a new employee by creating an `Employee` object and appending it to **"employees.txt"**.  
   - **Option 2**: Read all records from **"employees.txt"** and display them.  
   - **Option 3**: Search for an employee by **Employee ID** and display their details.  
   - **Option 4**: Update an employee's information (name, position, or salary) based on the Employee ID.  
   - **Option 5**: Delete an employee's record from the file using the Employee ID.  
   - **Option 6**: Exit the program.


### **Example Usage**  
```plaintext
Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit

Enter your choice: 1
Enter Employee ID: 1001
Enter Name: John Doe
Enter Position: Software Engineer
Enter Salary: 75000
Employee added successfully!

Enter your choice: 2
Employee Records:
1001, John Doe, Software Engineer, 75000

Enter your choice: 3
Enter Employee ID to search: 1001
Employee Found:
1001, John Doe, Software Engineer, 75000

Enter your choice: 6
Goodbye!
```

### **Additional Instructions**
1. Use the `Employee` class to encapsulate individual employee data and functionality (e.g., a `__str__` method for displaying employee details).  
2. Use the `EmployeeManager` class for managing operations such as file handling, record searching, and updates.  
3. Ensure your code is modular, with methods for each operation (e.g., `add_employee`, `view_all_employees`).  


### **Bonus Challenge**
1. Add validation to ensure unique Employee IDs.  
2. Implement error handling for invalid inputs and file operations.  
3. Allow users to sort employee records (e.g., by salary or name) before displaying them.  


---

## To-Do Application

**Objective**: Create a flexible To-Do application to manage tasks with support for different file storage formats (e.g., CSV, JSON). The application should be designed such that adding support for a new file format requires minimal changes to the code.


### **Task Description**

#### 1. Functional Requirements:
Your To-Do application should provide the following features:
1. **Add a task**: Allow users to add tasks with the following details:
   - `Task ID`
   - `Title`
   - `Description`
   - `Due Date` (optional)
   - `Status` (e.g., Pending, In Progress, Completed)
2. **View tasks**: Display all tasks with their details.
3. **Update a task**: Allow users to modify a task's details using its Task ID.
4. **Delete a task**: Remove a task by its Task ID.
5. **Filter tasks**: Filter tasks by status (e.g., Pending or Completed).
6. **Save and load tasks**: Save tasks to a file and load them from the file on startup.

#### 2. Design Requirements:
1. **Separation of Concerns**:
2. **Support for Multiple Formats**:
3. **Minimal Code Changes**:

#### 3. Example Usage:
```plaintext
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit

Enter your choice: 1
Enter Task ID: 101
Enter Title: Finish Homework
Enter Description: Complete math and science homework.
Enter Due Date (YYYY-MM-DD): 2024-12-31
Enter Status (Pending/In Progress/Completed): Pending
Task added successfully!

Enter your choice: 2
Tasks:
101, Finish Homework, Complete math and science homework., 2024-12-31, Pending
```

### **Deliverables**
1. Python scripts with classes and methods implemented as described.
2. Clear comments and documentation.
3. A brief explanation of how you ensured minimal code changes when adding support for new file formats.
