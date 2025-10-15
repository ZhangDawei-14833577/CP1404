
"""Extract a possible name from the given email address."""
def extract_name_from_email(email):
    # Remove the part before @
    prefix = email.split('@')[0]
    # Replace . or _ with a space and capitalize the first letter
    parts = prefix.replace(',', ' ').replace('_', ' ').title()
    return parts

def main():
