from dotenv import load_dotenv
import requests
import os

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
TORN_ADDRESS = os.getenv("TORN_CONTRACT_ADDRESS")
# https://etherscan.io/tx/0xdbd9ce11fd473aca558dc3ea29b5167af1ff459eddc38b5717acad97d210c234
tx_hash = "0xdbd9ce11fd473aca558dc3ea29b5167af1ff459eddc38b5717acad97d210c234"

url = f"https://api.etherscan.io/api?module=account&action=txlistinternal&txhash={tx_hash}&apikey={ETHERSCAN_API_KEY}"

response = requests.get(url)
internal_tx_data = response.json()

url = f"https://api.etherscan.io/api?module=account&action=txlist&address={TORN_ADDRESS}&sort=asc&apikey={ETHERSCAN_API_KEY}"  # &endblock={end_block}

response = requests.get(url)
contract_data = response.json()
if contract_data["status"] == "1":
    transactions = contract_data["result"]  # 10000 results
else:
    transactions = []

import ipdb

ipdb.set_trace()
