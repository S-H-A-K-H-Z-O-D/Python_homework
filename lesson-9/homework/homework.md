#### Task 1: Create a Library Management System with Custom Exceptions
1. Create a Python program to manage a small library system. 
2. Define custom exceptions for specific scenarios:
   - **`BookNotFoundException`**: Raised when trying to borrow a book that doesn’t exist in the library.
   - **`BookAlreadyBorrowedException`**: Raised when a book is already borrowed.
   - **`MemberLimitExceededException`**: Raised when a member tries to borrow more books than allowed.
3. Implement classes for:
   - **`Book`**: Attributes include `title`, `author`, and `is_borrowed`.
   - **`Member`**: Attributes include `name`, `borrowed_books` (limit to 3 books per member).
   - **`Library`**: Manages books and members, including borrowing and returning books.
4. Test your program with the following scenarios:
   - Adding books and members.
   - Borrowing and returning books.
   - Handling exceptions when rules are violated.

---

#### Task 2: Student Grades Management
1. Create a CSV file named `grades.csv` with the following structure:
   ```csv
   Name,Subject,Grade
   Alice,Math,85
   Bob,Science,78
   Carol,Math,92
   Dave,History,74
   ```
2. Write a Python program to:
   - Read data from `grades.csv` and store it in an appropriate data structure (e.g., a list of dictionaries).
   - Calculate the average grade for each subject.
   - Write a new CSV file named `average_grades.csv` with the following structure:
     ```csv
     Subject,Average Grade
     Math,88.5
     Science,78
     History,74
     ```
3. Use the `csv` module for reading and writing the CSV files.

---

### **Task 3: JSON Handling**

#### **Load and Save Tasks (JSON)**
1. Create a JSON file named `tasks.json` with the following structure:
   ```json
   [
       {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
       {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
       {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
   ]
   ```
2. Write a Python program to:
   - Load the tasks from `tasks.json`.
   - Display all tasks with the following fields: ID, Task Name, Completed Status, Priority.
   - Save any changes back to the `tasks.json` file (e.g., after modifying a task).

#### **Calculate Task Completion Stats**
1. Write a Python function to calculate the following statistics:
   - **Total tasks**: Count the total number of tasks.
   - **Completed tasks**: Count the number of completed tasks.
   - **Pending tasks**: Count the number of tasks that are not completed.
   - **Average priority**: Calculate the average priority level of all tasks.
   
   Display these statistics after loading the tasks.

#### **Convert JSON Data to CSV**
1. Write a function to convert the task data in `tasks.json` to a CSV file named `tasks.csv`. The CSV should have the following columns:
   - ID
   - Task Name
   - Completed Status
   - Priority

   For example:
   ```csv
   ID,Task,Completed,Priority
   1,Do laundry,False,3
   2,Buy groceries,True,2
   3,Finish homework,False,1
   ```
