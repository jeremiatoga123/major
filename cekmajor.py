import requests
import json

def read_userids_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

userids = read_userids_from_file('userid.txt')
berear = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjc0OTc5ODE4MjEsImV4cCI6MTcyODU0NjA1OX0.xnRCRtaHanazivXV7-CkVG66BaF_1tSlYs9CzjYDHjY"  #Isi token Bearer kamu di sini
total_balance = 0
total_accounts = 0

def checkmajor(userid):
    global total_balance, total_accounts
    api = f"https://major.bot/api/users/{userid}/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {berear}",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        "Origin": "https://major.bot",
        "Referer": "https://major.bot/earn",
        "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128", "Microsoft Edge WebView2";v="128"',
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }

    response = requests.get(api, headers=headers)
    if response.status_code == 200:
        data = response.json()
        result = {
            "id": data.get("id"),
            "username": data.get("username"),
            "balance": data.get("rating"),
        }
        output = (
            f"=== User Information ===\n"
            f"ID       : {result['id']}\n"
            f"Username : {result['username']}\n"
            f"Balance Major : {result['balance']:,}\n"  
            f"========================\n"
        )
        print(output)
        total_balance += result['balance']
        total_accounts += 1
    else:
        print(f"Error for User ID {userid}: {response.status_code}")
        print(response.text)

for userid in userids:
    checkmajor(userid)
print(f"Total Accounts: {total_accounts}")
print(f"Total Balance: {total_balance:,}")