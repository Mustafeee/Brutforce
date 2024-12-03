# _____      _            
# |  __ \    (_)           
# | |__) |_ _ _ _ __ __  __
# |  ___/ _` | | '_ \\ \/ /
# | |  | (_| | | | | |>  < 
# |_|   \__,_|_|_| |_/_/\_\

print("============================")
print("💀 Brute Force Attack - Created By painx ☠️")
print("============================")

# Prompt for user input
target_id = input("Enter target ID: ")
username = input("Enter target username: ")
wordlist_file = input("Enter wordlist file path: ")

print("\nStarting Brute Force Attack...\n")

# Try to read and process the wordlist
try:
    with open(wordlist_file, "r") as file:
        for password in file:
            password = password.strip()  # Remove newline characters
            print(f"Trying password: {password} for username: {username}")
            # You can add your login logic here
            # Example:
            # if login(username, password):
            #     print(f"\nPassword found: {password}")
            #     break
        else:
            print("\nBrute Force Attack finished - No password found.")
except FileNotFoundError:
    print("\nError: Wordlist file not found. Please check the file path.")
except Exception as e:
    print(f"\nAn error occurred: {e}")
