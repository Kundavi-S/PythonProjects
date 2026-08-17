# ATM Management System

A simple **Python ATM Management System** that demonstrates basic programming concepts such as loops, conditional statements, user input, lists, and balance management.

## Features

* 🔐 **PIN Authentication**

  * User gets a maximum of 3 attempts to enter the correct 4-digit PIN.
  * Account is blocked after 3 incorrect attempts.

* 💰 **Check Balance**

  * Displays the current account balance.

* 💵 **Deposit Money**

  * Allows the user to deposit money.
  * Updates the account balance.
  * Records the transaction.

* 🏧 **Withdraw Money**

  * Allows withdrawals in multiples of 100.
  * Checks for insufficient balance.
  * Rejects invalid amounts.
  * Updates the account balance.
  * Records successful withdrawals.

* 📜 **Mini Statement**

  * Displays transaction history using a `for` loop.

* 🚪 **Exit**

  * Exits the ATM menu and displays a thank-you message.

## Concepts Used

This project demonstrates:

* `while` loops
* `for` loops
* `if / elif / else`
* `break`
* Lists
* User input with `input()`
* Type conversion using `int()` and `float()`
* String formatting and concatenation
* Basic arithmetic operations
* Conditional validation

## Default Credentials

```text
PIN: 1234
Initial Balance: ₹10,000
```

> These credentials are hard-coded for learning purposes only and should not be used in a real banking application.

## How It Works

1. The program asks the user to enter a 4-digit PIN.
2. The user has up to 3 attempts.
3. After successful authentication, the ATM menu is displayed.
4. The user can:

   * Check balance
   * Deposit money
   * Withdraw money
   * View mini statement
   * Exit
5. The menu continues to display until the user selects **Exit**.

## Validation

The program handles:

* Incorrect PIN
* Maximum login attempts
* Invalid withdrawal amounts
* Withdrawal amounts that are not multiples of 100
* Insufficient account balance
* Invalid menu choices

## Example Menu

```text
========================================
ATM Menu
1.Check Balance
2.Deposit Money
3.Withdraw Money
4.Mini Statement
5.Exit
========================================
Enter Your Choice :
```

## Future Improvements

Some possible improvements for this project:

* Add multiple bank accounts/users.
* Hide PIN input using `getpass`.
* Add transaction dates and times.
* Limit the number of transactions shown in the mini statement.
* Add PIN change functionality.
* Store account information in a file or database.
* Improve input validation to prevent crashes from non-numeric input.

## Author

**Python ATM Management System**

A beginner-friendly Python project created to practice programming fundamentals.
