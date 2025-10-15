
"""Extract a possible name from the given email address."""
def extract_name_from_email(email):
    # Remove the part before @
    prefix = email.split('@')[0]
    # Replace . or _ with a space and capitalize the first letter
    parts = prefix.replace(',', ' ').replace('_', ' ').title()
    return parts

def main():
    """Store emails and names in a dictionary."""
    email_to_name = {}
    email = input("Emails: ")
    while email != "":
        # Automatically extract names based on email
        name = extract_name_from_email(email)
        # Ask the user if it is correct
        confirmation = input(f"Is your name {name}? (Y/n)").lower()
        if confirmation not in ("", "y", "yes"):
            name = input("Name: ")
        # Store names in a dictionary
        email_to_name[email] = name
        email = input("Email: ")

    # Print result
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()