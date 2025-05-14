# First project: ID MAKER ✨

# Importing libraries
import os
import time
import random
import colorama

# Rainbow Text
from colorama import Fore, Style

colorama.init(autoreset=True)

def print_rainbow(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, char in enumerate(text):
        print(colors[i % len(colors)] + char, end='')
    print(Style.RESET_ALL)

from colorama import Fore, Style

def print_purple(text, variation="normal"):
    if variation == "bright":
        style = Style.BRIGHT
    elif variation == "dim":
        style = Style.DIM
    else:
        style = Style.NORMAL
    print(style + Fore.MAGENTA + text + Style.RESET_ALL)    


# Init
print_purple("Welcome to ID MAKER. Made by Flownit✨")
time.sleep(2)
print("This program will help you create a random ID for your project.")
print_purple("Opening the GUI...")
time.sleep(0.5)
# GUI
os.system('cls')
print_purple("""
    ______ __                        _  __     ____ ____     ______ ______ _   __
   / ____// /____  _      __ ____   (_)/ /_   /  _// __ \   / ____// ____// | / /
  / /_   / // __ \| | /| / // __ \ / // __/   / / / / / /  / / __ / __/  /  |/ / 
 / __/  / // /_/ /| |/ |/ // / / // // /_   _/ / / /_/ /  / /_/ // /___ / /|  /  
/_/    /_/ \____/ |__/|__//_/ /_//_/ \__/  /___//_____/   \____//_____//_/ |_/ 
""")
print_purple("Select an option:")
print("[1.] Random ID")
print("[2.] About")
print("[3.] Exit")
# Get user input
choice = input("Enter your choice: ")
# Check user input
if choice == "1":
    # Random ID
    print_purple("Generating random ID.")
    time.sleep(0.5)
    os.system('cls')
    print_purple("Generating random ID..")
    time.sleep(0.5)
    os.system('cls')
    print_purple("Generating random ID...")
    time.sleep(0.5)
    os.system('cls')
    print_purple("Generating random ID....")
    os.system('cls')
    # Random Name
    # Generate a random name
    first_names = ["Nathan", "Alice", "Bob", "Charlie", "Daisy", "Eve", "Frank", "Grace", "Hannah"]
    last_names = ["Villemaire", "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis"]
    random_full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    # Print random Random name
    print_purple(f"Name: {random_full_name}", "bright")

    # Random Age
    # Generate a random age
    random_age = random.randint(18, 99)
    # Print random age
    print_purple(f"Age: {random_age}", "bright")

    # Random Sex
    # Generate
    Genre = ["Male", "Female", "Other"]
    random.choice(Genre)
    # Print Genre
    print_purple("Genre: " + random.choice(Genre), "bright")

    # Random SSN
    # Generate a random SSN
    random_ssn = f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
    # Print random SSN
    print_purple(f"SSN: {random_ssn}", "bright")

    # Random Credit Card
    # Generate a random credit card number
    random_credit_card = f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    # Print random credit card number
    print_purple(f"Credit Card: {random_credit_card}", "bright")
    # Credit Card Code
    # Generate a random credit card code
    random_credit_card_code = f"{random.randint(100, 999)}"
    # Print random credit card code
    print_purple(f"CVV: {random_credit_card_code}", "bright")
    # Expiration Date
    # Generate a random expiration date
    random_expiration_date = f"{random.randint(1, 12)}/{random.randint(23, 30)}"
    # Print random expiration date
    print_purple(f"Expiration Date: {random_expiration_date}", "bright")

    # Random Address
    # Generate a random address
    random_address = f"{random.randint(100, 999)} {random.choice(['Main St', 'Elm St', 'Oak St', 'Pine St'])}, {random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'])}, {random.choice(['NY', 'CA', 'IL', 'TX'])} {random.randint(10000, 99999)}"
    # Print random address
    print_purple(f"Address: {random_address}", "bright")

    # Random Phone Number
    # Generate a random phone number
    random_phone_number = f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
    # Print random phone number
    print_purple(f"Phone Number: {random_phone_number}", "bright")

    # Random Email
    # Generate a random email
    random_email = f"{random_full_name.replace(' ', '').lower()}@gmail.com"
    # Print random email
    print_purple(f"Email: {random_email}", "bright")
    # Random Password
    # Generate a random password
    random_password = f"{random.randint(10000000, 99999999)}"
    # Print random password
    print_purple(f"Password: {random_password}", "bright")

    # DISCLAIMER
    print_purple("DISCLAIMER: This is a random ID generator. Do not use it for illegal activities.", "dim")
    print_purple("These are not valid info.", "dim")

    # Save to file
    save_to_file = input("Do you want to save the ID to a file? (y/n): ")
    if save_to_file.lower() == "y":
        file_name = input("Enter the file name: ")
        with open(file_name, "w") as f:
            f.write(f"Name: {random_full_name}\n")
            f.write(f"Age: {random_age}\n")
            f.write(f"Genre: {random.choice(Genre)}\n")
            f.write(f"SSN: {random_ssn}\n")
            f.write(f"Credit Card: {random_credit_card}\n")
            f.write(f"CVV: {random_credit_card_code}\n")
            f.write(f"Expiration Date: {random_expiration_date}\n")
            f.write(f"Address: {random_address}\n")
            f.write(f"Phone Number: {random_phone_number}\n")
            f.write(f"Email: {random_email}\n")
            f.write(f"Password: {random_password}\n")
        print_purple("ID saved to file.", "bright")

    else:
        print_purple("ID not saved to file.", "dim")







