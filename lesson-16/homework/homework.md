#### **Merging and Joining**
1. **Inner Join on Chinook Database**
   - Load the `chinook.db` database.
   - Perform an inner join between the `customers` and `invoices` tables on the `CustomerId` column.
   - Find the total number of invoices for each customer.

2. **Outer Join on Movie Data**
   - Load the `movie.csv` file.
   - Create two smaller DataFrames:
     - One with only `director_name` and `color`.
     - Another with `director_name` and `num_critic_for_reviews`.
   - Perform a left join and then a full outer join on `director_name`.
   - Count how many rows are in the resulting DataFrames for each join type.

---

#### **Grouping and Aggregating**
1. **Grouped Aggregations on Titanic**
   - Group passengers by `Pclass` and calculate the following:
     - Average age.
     - Total fare.
     - Count of passengers.
   - Save the results to a new DataFrame.

2. **Multi-level Grouping on Movie Data**
   - Group the movies by `color` and `director_name`.
   - Find:
     - Total `num_critic_for_reviews` for each group.
     - Average `duration` for each group.

3. **Nested Grouping on Flights**
   - Group flights by `Year` and `Month` and calculate:
     - Total number of flights.
     - Average arrival delay (`ArrDelay`).
     - Maximum departure delay (`DepDelay`).

---

#### **Applying Functions**
1. **Apply a Custom Function on Titanic**
   - Write a function to classify passengers as `Child` (age < 18) or `Adult`.
   - Use `apply` to create a new column, `Age_Group`, with these values.

2. **Normalize Employee Salaries**
   - Load the `employee.csv` file.
   - Normalize the salaries within each department.

3. **Custom Function on Movies**
   - Write a function that returns `Short`, `Medium`, or `Long` based on the duration of a movie:
     - `Short`: Less than 60 minutes.
     - `Medium`: Between 60 and 120 minutes.
     - `Long`: More than 120 minutes.
   - Apply this function to classify movies in the `movie.csv` dataset.

---

#### **Using `pipe`**
1. **Pipeline on Titanic**
   - Create a pipeline to:
     - Filter passengers who survived (`Survived == 1`).
     - Fill missing `Age` values with the mean.
     - Create a new column, `Fare_Per_Age`, by dividing `Fare` by `Age`.

2. **Pipeline on Flights**
   - Create a pipeline to:
     - Filter flights with a departure delay greater than 30 minutes.
     - Add a column `Delay_Per_Hour` by dividing the delay by the scheduled flight duration.
