# Open-Key-Finder
Better version of bytemallet/openkeyfinder updated to work with the newest OpenAI API

## Installation
To install Open-Key-Finder, follow these steps:

1. Clone the repository:
	```shell
	git clone https://github.com/smugg99/Open-Key-Finder.git
	```

2. Navigate to the project directory:
	```shell
	cd Open-Key-Finder
	```

3. Install the required dependencies:
	```shell
	python3 -m venv venv
	```
	```shell
	source venv/bin/activate
	```
	```shell
	venv/bin/pip install -r requirements.txt
	```

4. Create venv file with your github cookie
	You can get the login cookie by going to the dev tools on your browser then
	Application>Cookies>https://github.com and search for something like "user_session"

	```shell
	touch .env
	```
	```shell
	echo 'GITHUB_COOKIE_SESSION=""' >> .env
	echo 'OUTPUT_FILE="output.json"' >> .env
	```
	
5. Run the script
	```shell
	venv/bin/python main.py
	```

## Disclaimer 
This tool is intended for educational and research purposes only. The creators of this tool are not responsible for any misuse or unauthorized to OpenAI API.