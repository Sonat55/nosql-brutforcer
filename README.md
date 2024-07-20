# NoSQL Security Toolkit for CTFs
##Adjust to your needs

This toolkit, provides utilities for testing and ensuring the security of NoSQL databases mostly for CTFs. It includes tools for password length checking and brute force attacks, designed to help developers and security professionals assess the resilience of their NoSQL database implementations against common attack vectors.

## Features

- **NoSQL Password Length Checker**: Determines the correct password length for a given user by testing regex-based login attempts. This tool helps in identifying the password policy of the target database.
  
- **NoSQL Brute Force**: A brute force attack tool tailored for NoSQL databases. It attempts to log in with various password combinations to find the correct one.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library

### Installation

1. Clone the repository or download the toolkit to your local machine.
2. Navigate to the "Nowy folder" directory.
3. Install the required Python packages:

```sh
pip install -r requirements.txt
```

Usage
NoSQL Password Length Checker
```sh
python nosql-passwordlengthchecker.py -u <URL> -U <USER>
```
-u, --url: The URL to send the POST request to.
-U, --user: The user field value to use in the POST request.

NoSQL Brute Force
```sh
python nosql-bruteforce.py -u <URL> -U <USER> -W <length>
```
-u, --url: The URL to send the POST request to.
-U, --user: The user field value to use in the POST request.
-l, length of password
