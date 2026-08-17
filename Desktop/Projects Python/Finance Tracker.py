
print("*" * 60)
print("             PERSONAL FINANCE TRACKER")
print("*" * 60)
print("Track your monthly income and expenses!")
print("Get insights into your spending habits.")
print("-" * 60)

# ==============================
# PERSONAL INFORMATION
# ==============================

print("👤 PERSONAL INFORMATION")
print("-" * 30)

name = input("Enter your full name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary ($): "))
savings_account = input("Do you have a savings account? (yes/no): ")
financial_goal = input("What's your main financial goal? ")

# ==============================
# MONTHLY INCOME DETAILS
# ==============================

print("\n💰 MONTHLY INCOME DETAILS")
print("-" * 30)

main_salary = float(input("Main job salary ($): "))
side_income = float(input("Side hustle/part-time income ($): "))
other_income = float(input("Other income (investments, gifts, etc.) ($): "))

total_income = main_salary + side_income + other_income
annual_income = total_income * 12

# ==============================
# MONTHLY EXPENSES
# ==============================

print("\n💸 MONTHLY EXPENSES")
print("-" * 30)

rent = float(input("Rent/Mortgage ($): "))
food = float(input("Food & Groceries ($): "))
transport = float(input("Transportation ($): "))
entertainment = float(input("Entertainment ($): "))
utilities = float(input("Utilities (electricity, water, internet) ($): "))
miscellaneous = float(input("Miscellaneous expenses ($): "))

total_expenses = (
    rent
    + food
    + transport
    + entertainment
    + utilities
    + miscellaneous
)

# ==============================
# FINANCIAL CALCULATIONS
# ==============================

monthly_savings = total_income - total_expenses
annual_savings = monthly_savings * 12

savings_rate = (monthly_savings / total_income) * 100
expense_ratio = (total_expenses / total_income) * 100

rent_percentage = (rent / total_expenses) * 100
food_percentage = (food / total_expenses) * 100
transport_percentage = (transport / total_expenses) * 100
entertainment_percentage = (entertainment / total_expenses) * 100
utilities_percentage = (utilities / total_expenses) * 100
miscellaneous_percentage = (miscellaneous / total_expenses) * 100

# ==============================
# FINANCIAL HEALTH CHECK
# ==============================

saving_money = monthly_savings > 0
overspending = total_expenses > total_income
has_emergency_buffer = monthly_savings >= (total_expenses * 3)
high_income_earner = total_income >= 20000
high_entertainment_spending = entertainment_percentage > 20

# ==============================
# FINANCIAL RATIOS
# ==============================

debt_to_income_ratio = (total_expenses / total_income) * 100
food_budget_ratio = (food / total_income) * 100
entertainment_budget_ratio = (entertainment / total_income) * 100

# ==============================
# FINANCIAL ANALYSIS REPORT
# ==============================

print("\n" + "=" * 60)
print("             FINANCIAL ANALYSIS REPORT")
print("=" * 60)

print("\n👤 USER PROFILE:")
print("Name:", name)
print("Age:", age, "years old")
print("Has Savings Account:", savings_account)
print("Financial Goal:", financial_goal)

print("\n💰 INCOME BREAKDOWN:")
print(f"Main Salary: ${main_salary:,.2f}")
print(f"Side Income: ${side_income:,.2f}")
print(f"Other Income: ${other_income:,.2f}")
print(f"Total Monthly Income: ${total_income:,.2f}")
print(f"Projected Annual Income: ${annual_income:,.2f}")

print("\n💸 EXPENSE BREAKDOWN:")
print(f"Rent: ${rent:,.2f} ({rent_percentage:.1f}% of total expenses)")
print(f"Food: ${food:,.2f} ({food_percentage:.1f}% of total expenses)")
print(f"Transport: ${transport:,.2f} ({transport_percentage:.1f}% of total expenses)")
print(
    f"Entertainment: ${entertainment:,.2f} "
    f"({entertainment_percentage:.1f}% of total expenses)"
)
print(f"Utilities: ${utilities:,.2f} ({utilities_percentage:.1f}% of total expenses)")
print(
    f"Miscellaneous: ${miscellaneous:,.2f} "
    f"({miscellaneous_percentage:.1f}% of total expenses)"
)
print(f"Total Monthly Expenses: ${total_expenses:,.2f}")

print("\n💰 SAVINGS ANALYSIS:")
print(f"Monthly Savings: ${monthly_savings:,.2f}")
print(f"Projected Annual Savings: ${annual_savings:,.2f}")
print(f"Savings Rate: {savings_rate:.1f}%")
print(f"Expense Ratio: {expense_ratio:.1f}%")

print("\n🩺 FINANCIAL HEALTH CHECK:")
print("Saving Money:", saving_money)
print("Overspending:", overspending)
print("Has Emergency Buffer:", has_emergency_buffer)
print("High Income Earner:", high_income_earner)
print("High Entertainment Spending:", high_entertainment_spending)

print("\n📊 FINANCIAL RATIOS:")
print(f"Debt-to-Income Ratio: {debt_to_income_ratio:.1f}%")
print(f"Food Budget Ratio: {food_budget_ratio:.1f}%")
print(f"Entertainment Budget Ratio: {entertainment_budget_ratio:.1f}%")

print("\n" + "=" * 60)
print("                 PROJECT SUMMARY")
print("=" * 60)

print(f"Dear {name}, based on your financial data:")
print(
    f"You earn ${total_income:,.2f} monthly "
    f"and spend ${total_expenses:,.2f}."
)
print(
    f"Your savings rate is {savings_rate:.1f}%, "
    f"which means you save ${monthly_savings:,.2f} per month."
)

print("=" * 60)

