# Login and Registration Portal System

A simple command-line user management system built in Python that allows users to register new accounts, login to existing accounts, and optionally verify their accounts for a fee.

## 📋 Overview

This project is designed as a learning assignment to practice fundamental Python concepts including data structures, user input handling, conditional logic, and basic error handling.

## 🎯 Objective

Create a console-based application that provides:
- User registration with account creation
- User authentication and login
- Optional account verification system with fee-based verification
- Proper data validation and error handling

## ✨ Features

### Core Functionality
- **User Registration**: Create new user accounts with username, password, and initial balance
- **User Login**: Authenticate existing users with username/password validation
- **Account Verification**: Optional verification system that costs 1500 units from user balance
- **Data Persistence**: Store user data during program execution
- **Input Validation**: Handle invalid commands and duplicate usernames

### User Interface
- Clean ASCII art welcome portal
- Clear command instructions
- Formatted output for better user experience
- Case-insensitive command handling

## 🏗️ System Architecture

### Data Structure
Each user account contains:
```python
    username,
    password, 
    balance,
    is_verified (default: False),

```

### System Components
1. **Authentication System**: Login/logout functionality
2. **Registration System**: New user account creation
3. **Verification System**: Optional account verification with fee deduction
4. **Data Management**: User data storage and retrieval
5. **Error Handling**: Comprehensive error validation

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system
- Basic understanding of Python data types and control structures

### Installation
1. Clone or download the assignment files
2. Ensure you have Python installed
3. No additional dependencies required

### Usage
1. Run the Python file
2. Choose from the welcome menu:
   - Enter "login" to access existing account
   - Enter "register" to create new account
3. Follow the prompts based on your selection

## 🎮 User Flows

### Registration Flow
1. User selects "register"
2. System prompts for:
   - Username (must be unique)
   - Password
   - Initial balance
3. System creates account and displays user information
4. System offers optional verification:
   - Shows verification cost (1500)
   - User can accept or decline
   - If accepted and sufficient balance: deducts fee and marks as verified
   - If insufficient balance: shows error message
5. Displays final account status

### Login Flow
1. User selects "login"
2. System prompts for username and password
3. System validates credentials:
   - **Success**: Shows "login successful!" + user information
   - **User not found**: Shows "user {username} does not exists"
   - **Wrong password**: Shows "password mismatch for {username}"

## 🛠️ Technical Requirements

### Data Types Used
- `string`: Username, password storage
- `float`: Balance management
- `boolean`: Verification status
- `dict`: User data structure
- Your choice of data structure for `users_db`

### Key Programming Concepts
- Dictionary operations and data structures
- User input handling and validation
- Conditional logic and flow control
- String manipulation and formatting
- Basic error handling
- Program organization

## 🚨 Error Handling

The system handles various error scenarios:

| Error Type | Description | System Response |
|------------|-------------|-----------------|
| Duplicate Username | User tries to register existing username | "user {username} already exists" |
| Invalid Login | Username doesn't exist | "user {username} does not exists" |
| Wrong Password | Password mismatch during login | "password mismatch for {username}" |
| Insufficient Balance | Not enough funds for verification | Shows current balance vs required amount |
| Invalid Command | User enters command other than login/register | "invalid command" |

## 📝 Implementation Guidelines

### Starter Code Structure
```python
verification_amount = 1500
users_db = None  # Choose appropriate data type

output = """
   *---------------------------------------*
   |      Login and Register Portal        |
   |   ________________________________    |
   |  commands:                            |
   |   enter "login" to login              |
   |   enter "register" to register        |
   *---------------------------------------*
"""
```

### Key Implementation Points
1. Initialize `verification_amount` as 1500
2. Choose appropriate data type for `users_db`
3. Implement case-insensitive command handling
4. Validate user input at each step
5. Provide clear success and error messages
6. Handle all specified error cases

## 🎓 Learning Outcomes

Upon completion, students will demonstrate understanding of:
- Data structure selection and usage
- Input validation techniques
- Conditional statement implementation
- Data types operations
- Error handling best practices
- User experience design principles
- Code organization and documentation

## 📖 Example Usage

```
   *---------------------------------------*
   |      Login and Register Portal        |
   |   ________________________________    |
   |  commands:                            |
   |   enter "login" to login              |
   |   enter "register" to register        |
   *---------------------------------------*

register
create username: john_doe
create password: mypassword
enter available balance: 2000
User Created successfully!
{'username': 'john_doe', 'password': 'mypassword', 'balance': 2000.0, 'is_verified': False}
Do you wish to verify? yes or no
Verification costs: 1500
yes
verification updated successfully
Login successful!
{'username': 'john_doe', 'password': 'mypassword', 'balance': 500.0, 'is_verified': True}
```

## 🤝 Contributing

This is an educational assignment. Students should implement their own solutions based on the requirements provided.

## 📄 License

This project is for educational purposes only.

---

*Happy Coding! 🐍*