# wakapi-github
Python script that updates your GitHub Bio with your coding time of the day.

## Usage

1. Clone the repo
2. Install python and it's **requests** library
3. Get your API keys from the following links:
    - [GitHub Token](https://github.com/settings/tokens)  - Requires ```user``` scope
    - WakaPi API Key
4. Start ```py main.py```
        ``` python3 main.py```
   with the following environmental variables:
```
    "WAKAPI_API_KEY": "",
    "GITHUB_API_KEY": "",
    "WAKAPI_URL": "https://wakapi.dev" # without trailing "/"
```
