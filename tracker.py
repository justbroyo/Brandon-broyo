# Initialize an empty dictionary to store expenses
expenses = {}

# Function to handle menu actions based on the user's choice
def handle_action(choice, expense_id_counter):
    # Option 1: Add a new expense
    if choice == '1':
        category = input("Enter the category: ")  # Ask for the category
        amount = float(input("Enter the amount: $"))  # Ask for the amount and convert it to float
        date = input("Enter the date (YYYY-MM-DD): ")  # Ask for the date
        
        # Add the new expense to the dictionary with a unique expense ID
        expenses[expense_id_counter] = {'category': category, 'amount': amount, 'date': date}
        print(f"Expense {expense_id_counter} added.")  # Notify the user that the expense was added
        
        return expense_id_counter + 1  # Increment the counter to ensure unique ID for the next expense
    
    # Option 2: View all expenses
    elif choice == '2':
        if expenses:  # Check if there are any expenses in the dictionary
            # Loop through each expense and print its details
            for expense_id, details in expenses.items():
                print(f"ID: {expense_id}, Category: {details['category']}, Amount: ${details['amount']}, Date: {details['date']}")
        else:
            print("No expenses found.")  # Notify the user if there are no expenses
    
    # Option 3: Filter expenses by category
    elif choice == '3':
        category = input("Enter category to filter by: ")  # Ask for the category to filter by
        
        # Filter expenses by category using a dictionary comprehension
        filtered = {eid: details for eid, details in expenses.items() if details['category'].lower() == category.lower()}
        
        if filtered:  # Check if there are any expenses for the given category
            # Loop through filtered expenses and print their details
            for expense_id, details in filtered.items():
                print(f"ID: {expense_id}, Category: {details['category']}, Amount: ${details['amount']}, Date: {details['date']}")
        else:
            print(f"No expenses found for category '{category}'.")  # Notify if no matching expenses were found
    
    # Option 4: Calculate total expenses
    elif choice == '4':
        total = sum(details['amount'] for details in expenses.values())  # Calculate the total amount of all expenses
        print(f"Total expenses: ${total:.2f}")  # Display the total expenses with two decimal points
    
    # Option 5: Delete an expense by ID
    elif choice == '5':
        expense_id = int(input("Enter expense ID to delete: "))  # Ask for the expense ID to delete
        
        if expense_id in expenses:  # Check if the expense ID exists in the dictionary
            del expenses[expense_id]  # Delete the expense from the dictionary
            print(f"Expense {expense_id} deleted.")  # Notify the user that the expense was deleted
        else:
            print(f"Expense {expense_id} not found.")  # Notify the user if the expense ID is not found
    
    # Option 6: Exit the program
    elif choice == '6':
        print("Exiting Expense Tracker. Goodbye!")  # Notify the user that the program is exiting
        return False  # Return False to break out of the loop in the main function
    
    return True  # Return True to continue the program if not exiting

# Function to show the main menu with available options
def show_menu():
    print("\nExpense Tracker Menu:")  # Display a header for the menu
    print("1. Add New Expense")  # Option 1: Add new expense
    print("2. View All Expenses")  # Option 2: View all expenses
    print("3. Filter Expenses by Category")  # Option 3: Filter expenses by category
    print("4. Calculate Total Expenses")  # Option 4: Calculate total expenses
    print("5. Delete Expense")  # Option 5: Delete an expense
    print("6. Exit")  # Option 6: Exit the program

# Main function where the program starts and the loop runs
def main():
    expense_id_counter = 1  # Initialize a counter to keep track of unique expense IDs
    
    # Infinite loop that will keep showing the menu until the user decides to exit
    while True:
        show_menu()  # Display the menu with options
        choice = input("Choose an option (1-6): ")  # Ask the user to choose an option
        
        # Handle the user's choice and update the expense ID counter
        if not handle_action(choice, expense_id_counter):
            break  # Exit the loop and end the program if the user chose option '6' (Exit)
        
        expense_id_counter += 1  # Increment the counter to ensure the next expense gets a unique ID

# Start the program by calling the main function
if __name__ == "__main__":
    main()
