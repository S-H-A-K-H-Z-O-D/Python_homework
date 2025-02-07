### Homework: Pandas Basics

#### Part 1: Reading Files  
1. **`chinook.db`**  
   - Use the `sqlite3` library to connect to the database.  
   - Read the `customers` table into a pandas DataFrame. Display the first 10 rows.  

2. **`iris.json`**  
   - Load the JSON file into a DataFrame. Show the shape of the dataset and the column names.  

3. **`titanic.xlsx`**  
   - Load the Excel file into a DataFrame. Use `head` to display the first 5 rows.  

4. **Flights parquet file**  
   - Read the Parquet file into a DataFrame and use `info` to summarize it.  

5. **`movie.csv`**  
   - Load the CSV file into a DataFrame and display a random sample of 10 rows.

---

#### Part 2: Exploring DataFrames  
1. Using the DataFrame from **`iris.json`**:  
   - Rename the columns to lowercase.  
   - Select only the `sepal_length` and `sepal_width` columns.  

2. From the **`titanic.xlsx`** DataFrame:  
   - Filter rows where the age of passengers is above 30.  
   - Count the number of male and female passengers (`value_counts`).  

3. From the **Flights parquet file**:  
   - Extract and print only the `origin`, `dest`, and `carrier` columns.  
   - Find the number of unique destinations.  

4. From the **`movie.csv`** file:  
   - Filter rows where `duration` is greater than 120 minutes.  
   - Sort the filtered DataFrame by `director_facebook_likes` in descending order.  

---

#### Part 3: Challenges and Explorations  
 
- From **`iris.json`**: Calculate the mean, median, and standard deviation for each numerical column.  
- From **`titanic.xlsx`**: Find the minimum, maximum, and sum of passenger ages.  

- From **`movie.csv`**:  
    - Identify the director with the highest total `director_facebook_likes`.  
    - Find the 5 longest movies and their respective directors.  

- From **Flights parquet file**:  
    - Check for missing values in the dataset. Fill missing values in a numerical column with the column’s mean.  