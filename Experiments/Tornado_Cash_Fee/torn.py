from dotenv import load_dotenv
import os
import json
from web3 import Web3

load_dotenv()


# Connect to an Ethereum node (e.g., Infura or a local node)
infura_url = f'https://mainnet.infura.io/v3/{os.getenv("INFURA_API_KEY")}'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Tornado Cash contract address and the ABI for the events (you need to get the ABI from Etherscan)
TORNADO_CASH_CONTRACT = os.getenv("TORN_CONTRACT_ADDRESS")
TORNADO_ABI = json.loads(os.getenv("TORN_ABI"))

contract = web3.eth.contract(address=TORNADO_CASH_CONTRACT, abi=TORNADO_ABI)

import ipdb

ipdb.set_trace()
