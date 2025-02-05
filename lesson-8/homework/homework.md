## Model a Farm

In this assignment, you’ll create a simplified model of a farm. As you work through this assignment, keep in mind that there are a number of correct answers.

The focus of this assignment is less about the Python class syntax and more about software design in general, which is highly subjective. This assignment is intentionally left open-ended to encourage you to think about how you would organize your code into classes.

Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes, attributes, and methods. Think about inheritance. How can you prevent code duplication? Take the time to work through as many iterations as you feel are
necessary.

The actual requirements are open to interpretation, but try to adhere to these guidelines:

1. You should have at least four classes: the parent `Animal` class, and then at least three child animal classes that inherit from Animal.
2. Each class should have a few attributes and at least one method that models some behavior appropriate for a specific animal or all animals—such as walking, running, eating, sleeping, and so on.
3. Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviors.

---

## Build a Bank Application

#### **Objective:**
Develop a command-line banking application that allows users to perform basic banking operations like creating an account, depositing money, and withdrawing money. This will help you practice using object-oriented programming (OOP), file handling, and error handling in Python.


### **Tasks:**

#### **Step 1: Define the Classes**
1. Create a class `Account` with attributes:
   - `account_number`
   - `name`
   - `balance`

2. Create a class `Bank` to manage all accounts. It should have:
   - A dictionary to store accounts (`accounts`).
   - Methods for each operation:
     - `create_account(name, initial_deposit)`
     - `view_account(account_number)`
     - `deposit(account_number, amount)`
     - `withdraw(account_number, amount)`
     - `save_to_file()` and `load_from_file()` (for file handling).


#### **Step 2: Implement the Methods**
1. **Account Creation**
   - Generate a unique `account_number`.
   - Create an `Account` object and store it in the dictionary.
   - Save account details to a file.

2. **View Account Details**
   - Prompt the user to input their account number.
   - Retrieve and display the account details if found; otherwise, show an error.

3. **Deposit Money**
   - Prompt the user for their account number and deposit amount.
   - Validate the amount and update the account balance.

4. **Withdraw Money**
   - Prompt the user for their account number and withdrawal amount.
   - Validate that the amount is less than or equal to the balance and update the account balance.

5. **File Handling**
   - Use `save_to_file` to write account details to `accounts.txt`.
   - Use `load_from_file` to load account details when the program starts.

---

