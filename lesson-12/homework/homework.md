### Task 1

Scrape weather information from an HTML file and process it using Python and BeautifulSoup.

<h4>5-Day Weather Forecast</h4>
<table>
    <thead>
        <tr>
            <th>Day</th>
            <th>Temperature</th>
            <th>Condition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Monday</td>
            <td>25°C</td>
            <td>Sunny</td>
        </tr>
        <tr>
            <td>Tuesday</td>
            <td>22°C</td>
            <td>Cloudy</td>
        </tr>
        <tr>
            <td>Wednesday</td>
            <td>18°C</td>
            <td>Rainy</td>
        </tr>
        <tr>
            <td>Thursday</td>
            <td>20°C</td>
            <td>Partly Cloudy</td>
        </tr>
        <tr>
            <td>Friday</td>
            <td>30°C</td>
            <td>Sunny</td>
        </tr>
    </tbody>
</table>


Assume you are given the following HTML structure (you can save it as `weather.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>

</body>
</html>
```

1. **Parse the HTML File**:
   - Load the `weather.html` file using BeautifulSoup and extract the weather forecast details.

2. **Display Weather Data**:
   - Print the **day**, **temperature**, and **condition** for each entry in the forecast.

3. **Find Specific Data**:
   - Identify and print the day(s) with:
     - The highest temperature.
     - The "Sunny" condition.

4. **Calculate Average Temperature**:
   - Compute and print the **average temperature** for the week.

---

### Task 2

Scrape job listings from the website https://realpython.github.io/fake-jobs and store the data into an SQLite database.

1. **Scraping Requirements**:
   - Extract the following details for each job listing:
     - **Job Title**
     - **Company Name**
     - **Location**
     - **Job Description**
     - **Application Link**

2. **Data Storage**:
   - Store the scraped data into an SQLite database in a table named `jobs`.

3. **Incremental Load**:
   - Ensure that your script performs **incremental loading**:
     - Scrape the webpage and add only **new job listings** to the database.
     - Avoid duplicating entries. Use `Job Title`, `Company Name`, and `Location` as unique identifiers for comparison.

4. **Update Tracking**:
   - Add functionality to detect if an existing job listing has been updated (e.g., description or application link changes) and update the database record accordingly.

5. **Filtering and Exporting**:
   - Allow filtering job listings by **location** or **company name**.
   - Write a function to export filtered results into a CSV file.


### Task 3

You are tasked with scraping laptop data from the "Laptops" section of the [Demoblaze website](https://www.demoblaze.com/) and storing the extracted information in JSON format.

**Steps:**

1. **Navigate to the Website:**
   - Visit the [Demoblaze homepage](https://www.demoblaze.com/).
   - Click on the **Laptops** section to view the list of available laptops.

2. **Navigate to the Next Page:**
   - After reaching the Laptops section, locate and click the **Next** button to navigate to the next page of laptop listings.

3. **Data to Scrape:**
   For each laptop on the page, scrape the following details:
   - **Laptop Name**
   - **Price**
   - **Description**

4. **Data Storage:**
   - Save the extracted information in a structured **JSON format** with fields like:
     ```json
     [
       {
         "name": "Laptop Name",
         "price": "Laptop Price",
         "description": "Laptop Description"
       },
       ...
     ]
     ```

