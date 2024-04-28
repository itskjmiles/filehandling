import re

def extract_emails(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
            unique_emails = list(set(emails))
            return unique_emails
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while accessing '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")

emails = extract_emails("contacts.txt")

if emails is not None:
    print("Extracted emails:")
    for email in emails:
        print(email)
