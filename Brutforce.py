from colorama import Fore, Style, init  # Import the required modules

# Initialize Colorama
init(autoreset=True)

# Print the ASCII art with color
print(Fore.RED + """
______
     .-'      `-.
    /            \\
   |,  .-.  .-.  ,|
   | )(_o/  \\o_)( |
   |/     /\\     \\|
   (_     ^^     _)
    \\__|IIIIII|__/
     | \\IIIIII/ |
     \\          /
     
      `--------`

      CODED BY PAIN AND ROHAN AND POP-SMOKE 
""")

print("============================")
print(Fore.GREEN + "💀 Brute Force Attack - Created By Pop-smoKE ☠️")
print("============================")

# Prompt for user input
target_id = input(Fore.CYAN + "Enter target ID: ")
username = input(Fore.CYAN + "Enter target username: ")
wordlist_file = input(Fore.CYAN + "Enter wordlist file path: ")

print(Fore.YELLOW + "\nStarting Brute Force Attack...\n")

# Try to read and process the wordlist
try:
    with open(wordlist_file, "r") as file:
        for password in file:
            password = password.strip()  # Remove newline characters
            print(Fore.MAGENTA + f"Trying password: {password} for username: {username}")
            # You can add your login logic here
            # Example:
            # if login(username, password):
            #     print(Fore.GREEN + f"\nPassword found: {password}")
            #     break
        else:
            print(Fore.RED + "\nBrute Force Attack finished - No password found.")
except FileNotFoundError:
    print(Fore.RED + "\nError: Wordlist file not found. Please check the file path.")
except Exception as e:
    print(Fore.RED + f"\nAn error occurred: {e}")
