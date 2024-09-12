from dotenv import load_dotenv
import os
import json
from web3 import Web3
from tqdm import tqdm
from datetime import datetime
import pandas as pd

load_dotenv()


# Connect to an Ethereum node (e.g., Infura or a local node)
infura_url = f'https://mainnet.infura.io/v3/{os.getenv("INFURA_API_KEY")}'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Tornado Cash contract address and the ABI for the events (you need to get the ABI from Etherscan)
TORNADO_CASH_CONTRACT = os.getenv("TORN_CONTRACT_ADDRESS")
TORNADO_ABI = json.loads(os.getenv("TORN_ABI"))

contract = web3.eth.contract(address=TORNADO_CASH_CONTRACT, abi=TORNADO_ABI)
search_blocks = 2
end_block_number = web3.eth.get_block_number()

# debug
end_block = web3.eth.get_block(end_block_number, full_transactions=True)
print(datetime.fromtimestamp(end_block.timestamp))
print(f"https://etherscan.io/block/{end_block.number}")
print(
    f"https://etherscan.io/tx/{end_block.transactions[0].hash.hex()}",
    "(Should match number here)",
)
tx_receipt = web3.eth.get_transaction_receipt(end_block.transactions[0].hash)
print("Transaction Fee")
print(
    fee := tx_receipt.get("effectiveGasPrice", end_block.transactions[0].gasPrice)
    * tx_receipt.gasUsed,
    "Gwei",
)
print(web3.from_wei(fee, unit="ether"), "ETH")

import ipdb

ipdb.set_trace()

results = []

for block_num in tqdm(
    range(end_block_number, end_block_number - search_blocks, -1),
    desc="Blocks",
    position=0,
):
    block = web3.eth.get_block(block_num, full_transactions=True)
    timestamp = datetime.fromtimestamp(end_block.timestamp)
    for tx in tqdm(
        block.transactions, desc=f"Transactions of Block {block.number}", position=1
    ):
        if tx.to == contract.address or True:  # debug
            tx_receipt = web3.eth.get_transaction_receipt(tx.hash)

            if "effectiveGasPrice" in tx_receipt:
                # If it's an EIP-1559 transaction, use effectiveGasPrice from the receipt
                gas_price = tx_receipt.effectiveGasPrice
            else:
                # Get gasPrice from the transaction itself (tx object)
                gas_price = tx.gasPrice  # For legacy transactions

            fee = tx_receipt.gasUsed * gas_price

            results.append(
                {
                    "time": timestamp,
                    "block_num": block.number,
                    "tx_hash": tx.hash.hex(),
                    "fee": fee,
                }
            )

result_df = pd.DataFrame(results)
result_df["fee (ETH)"] = result_df["fee"].apply(web3.from_wei, unit="ether")
print(result_df)


import ipdb

ipdb.set_trace()
