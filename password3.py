# Save the secret password in a variable
secret_password = "mySecret123"

# Prompt the user for input
user_input = input("Enter the password: ")

# Use an if statement to check if the input matches
if user_input == secret_password:
    print("Access granted! Correct password.")
else:
    print("Access denied! Incorrect password.")

