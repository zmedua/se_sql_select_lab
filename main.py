# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd 
# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")
# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
    FROM employees;             
 """, conn)
print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
    FROM employees;                           
""", conn)
print(df_five_reverse)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID
    FROM employees

""", conn)
print(df_alias)
# STEP 5
# Replace None with your code
df_executive = pd.read_sql( """
SELECT lastName, employeeNumber, jobTitle,
CASE
WHEN jobTitle = 'President' THEN 'Executive'
WHEN jobTitle = 'VP Sales' THEN 'Executive'
WHEN jobTitle = 'VP Marketing' THEN 'Executive'
ELSE 'Not Executive'
END AS role 
FROM employees                            
                           
""", conn)
print(df_executive)
# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""
SELECT length(lastName) AS name_length
FROM employees

""", conn)
print(df_name_length)
# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""
SELECT substr(jobTitle, 1, 2) AS short_title
FROM employees
                             """, conn)
print(df_short_title)

order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""
SELECT CAST(round(priceEach * quantityOrdered) AS INTEGER)AS total_amount
FROM orderDetails                              
""", conn).sum()

print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
SELECT
orderDate,
substr(orderDate, 9, 2) AS day,
substr(orderDate, 6, 2) AS month,                               
substr(orderDate, 1, 4) AS year
FROM orders                                                                
""", conn)
print(df_day_month_year)

conn.close()