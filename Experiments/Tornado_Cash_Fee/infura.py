from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

url = f'https://mainnet.infura.io/v3/{os.getenv("INFURA_API_KEY")}'

payload = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}

headers = {"content-type": "application/json"}

response = requests.post(url, data=json.dumps(payload), headers=headers).json()

print(response)
