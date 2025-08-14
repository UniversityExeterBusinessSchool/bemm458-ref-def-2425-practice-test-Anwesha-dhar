
#######################################################################################################################################################
# 
# Name:Anwesha Dhar
# SID:740096172
# Exam Date:14-08-2025
# Module:BEMM4458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/bemm458-ref-def-2425-practice-test-Anwesha-dhar.git
#
########################################################################################################################################################
# Instruction 1. Carefully read each question before attempting the solution. Complete all tasks in the script provided.

# Instruction 2. Only ethical and minimal use of AI tools is allowed. This includes help in syntax, documentation look-up, or debugging only.
#                You must not use AI to generate the core logic or full solutions.
#                Clearly indicate where and how AI support was used.

# Instruction 3. Paste the output of each code section directly beneath it as a comment (e.g., # OUTPUT: (34, 90))

# Instruction 4. Add sufficient code comments to demonstrate your understanding of each solution.

# Instruction 5. Save your file, commit it to GitHub, and upload to ELE. GitHub commit must be done before the end of the exam session.

########################################################################################################################################################
# Question 1 - List Comprehension and String Manipulation
# You are analysing customer reviews collected from a post-service survey.
# Your SID will determine the two allocated keywords from the dictionary below. Use the **second** and **second-to-last** digits of your SID.
# For each selected keyword, identify all positions (start and end) where the word occurs in the customer_review string.
# Store each occurrence as a tuple in a list called `location_list`.

customer_review = """Thank you for giving me the opportunity to share my honest opinion. I found the packaging impressive and delivery punctual. 
However, there are several key aspects that require improvement. The installation process was somewhat confusing, and I had to refer to external 
tutorials. That said, the design aesthetics are great, and the customer support team was highly responsive. I would love to see more 
transparency in product specifications and a simpler return process. Overall, a balanced experience with clear potential for enhancement."""

# Dictionary of keywords
feedback_keywords = {
    0: 'honest',
    1: 'impressive',
    2: 'punctual',
    3: 'confusing',
    4: 'tutorials',
    5: 'responsive',
    6: 'transparent',
    7: 'return',
    8: 'enhancement',
    9: 'potential'
}

# Write your code here to populate location_list
Location_list = [
    (customer_review.find('tutorials'), customer_review.find('tutorials') + len('tutorials')),
    (customer_review.find('return'), customer_review.find('return') + len('return'))
]
print("Positions of keywords:", Location_list)

########################################################################################################################################################
# Question 2 - Metrics Function for Business Intelligence
# You work in a startup focused on digital health. Your manager wants reusable functions to calculate key performance metrics:
# Gross Profit Margin, Churn Rate, Customer Lifetime Value (CLV), and Cost Per Acquisition (CPA).
# Use the **first** and **last** digits of your student ID as sample numerical values to test your function outputs.

# Insert first digit of SID here:7
# Insert last digit of SID here:2

# Write a function for Gross Profit Margin (%) = (Revenue - COGS) / Revenue * 100
def gross_profit_margin(COGS,revenue):
    return ((revenue-COGS) / revenue) * 100

# Write a function for Churn Rate (%) = (Customers Lost / Customers at Start) * 100
def churn_rate(customers_lost, customers_start):
    return (customers_lost / customers_start) * 100

# Write a function for Customer Lifetime Value = Average Purchase Value × Purchase Frequency × Customer Lifespan
def customer_lifetime_value(avg_purchase_value, purchase_frequency, customer_lifespan):
    return avg_purchase_value * purchase_frequency * customer_lifespan


# Write a function for CPA = Marketing Cost / Number of Acquisitions
def customer_acquisition_cost(total_marketing_cost, new_customers_acquired):
    return total_marketing_cost / new_customers_acquired

# Test your functions here
print("Gross Profit Margin:", gross_profit_margin(7, 2))
print("Churn Rate:", churn_rate(7, 2))
print("Customer Lifetime Value:", customer_lifetime_value (7, 2, 6))
print("Customer Acquisition Cost:", customer_acquisition_cost(7, 2))

########################################################################################################################################################
# Question 3 - Linear Regression for Pricing Strategy
# A bakery is studying how price affects cupcake demand. Below is a table of past pricing decisions and customer responses.
# Using linear regression:
# 1. Estimate the best price that maximises demand.
# 2. Predict demand if the bakery sets price at £25.

"""
Price (£)    Demand (Units)
---------------------------
8            200
10           180
12           160
14           140
16           125
18           110
20           90
22           75
24           65
26           50
"""

# Write your linear regression solution here
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

prices = np.array([8,10,12,14,16,18,20,22,24,26]).reshape(-1, 1)
demand = np.array([200, 180, 160, 140, 125, 110, 90,75,65,50])

# Create and train model
model = LinearRegression()
model.fit(prices, demand)

# To predict the demand at price 25
predicted_demand = model.predict(np.array([[25]]))
print(f"Predicted demand at price £25: {predicted_demand[0]}")

# To plot the data points and regression line
plt.scatter(prices, demand, color='green')
plt.plot(prices, model.predict(prices), color='pink')
plt.xlabel("Price (£)")
plt.ylabel("Demand (Units)")
plt.title("Price vs Demand")
plt.show()

########################################################################################################################################################
# Question 4 - Debugging and Chart Creation
# The following code is intended to generate 100 random integers between 1 and your SID, and plot them as a scatter plot.
# However, the code contains bugs and lacks contextual annotations. Correct the code and add appropriate comments and output.

import random
import matplotlib.pyplot as plt

# Accept student ID as input
import random
import matplotlib.pyplot as plt
# Accept student ID as input
sid_input = input("740096172 ")
sid_value = int(sid_input)
# Generate 100 random values
random_values = [random.randint(1, sid_value) for _ in range(100)]
# Plotting as scatter plot
plt.figure(figsize=(10,5))
plt.scatter(range(100), random_values, color='green', marker='x', label='Random Values')
plt.title("Scatter Plot of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

########################################################################################################################################################
##I have completed and provided everything
init Commit(
    "I have completed and provided everything
)