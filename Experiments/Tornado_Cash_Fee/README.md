# Analysis Tornado Cash Fees From Blockchain

- [Tornado Cash project | Token Terminal](https://tokenterminal.com/terminal/projects/tornado-cash)
- [Tornado Cash](https://github.com/tornadocash)
- [$2.38 | TORN Token (TORN) Token Tracker | Etherscan](https://etherscan.io/token/0x77777feddddffc19ff86db637967013e6c6a116c): Tornado Cash (TORN) Governance Token Contract Address `0x77777feddddffc19ff86db637967013e6c6a116c`

---

- [Web3 Development Platform | IPFS API & Gateway | Blockchain Node Service](https://www.infura.io/)
  - [Ethereum API | IPFS API & Gateway | ETH Nodes as a Service | Infura](https://app.infura.io/)
  - [Ethereum | INFURA](https://docs.infura.io/api/networks/ethereum)
- [【Ethereum 智能合約開發筆記】不用自己跑節點，使用 Infura 和 web3.js 呼叫合約.md](https://gist.github.com/Ankarrr/b33d388aa4c4411559f74d9814447ff3)
- [How to access real-time smart contract data from Python code (using Lido contract as an example) | by Kirill Balakhonov | Chainstack | Medium](https://medium.com/@balakhonoff_47314/how-to-access-real-time-smart-contract-data-from-python-code-using-lido-as-an-example-38738ff077c5)
- [Getting Started | Metadata API](https://metadata.etherscan.io/)
  - [Etherscan APIs- Ethereum (ETH) API Provider](https://etherscan.io/apis)
- [Consensys/mythril: Security analysis tool for EVM bytecode. Supports smart contracts built for Ethereum, Hedera, Quorum, Vechain, Rootstock, Tron and other EVM-compatible blockchains.](https://github.com/Consensys/mythril)
  - [How to perform dynamic analysis of a smart contract with Myth | by bugbountydegen | Medium](https://medium.com/@bugbountydegen/how-to-perform-dynamic-analysis-of-a-smart-contract-with-myth-e80fb9351c85)
  - [What is Mythril? — Mythril v0.23.9 documentation](https://mythril-classic.readthedocs.io/en/master/about.html)

> - `myth analyze -a 0x77777FeDdddFfC19Ff86DB637967013e6C6A116C --infura-id YOUR_INFURA_ID`
>   - `mythril.interfaces.cli [ERROR]: Could not connect to RPC server. Make sure that your node is running and that RPC parameters are set correctly.`
> - `docker run -it mythril/myth /bin/bash`
>
> ```
> mythril.mythril.mythril_analyzer [CRITICAL]: Exception occurred, aborting analysis. Please report this issue to the Mythril GitHub page.
> Traceback (most recent call last):
>   File "/usr/local/lib/python3.10/site-packages/mythril/mythril/mythril_analyzer.py", line 153, in fire_lasers
>     sym = SymExecWrapper(
>   File "/usr/local/lib/python3.10/site-packages/mythril/analysis/symbolic.py", line 242, in __init__
>     self.laser.sym_exec(world_state=world_state, target_address=address.value)
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/svm.py", line 185, in sym_exec
>     self.execute_transactions(symbol_factory.BitVecVal(target_address, 256))
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/svm.py", line 232, in execute_transactions
>     self._execute_transactions_incremental(
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/svm.py", line 302, in _execute_transactions_incremental
>     execute_message_call(self, address, func_hashes=func_hashes)
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/transaction/symbolic.py", line 151, in execute_message_call
>     laser_evm.exec()
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/svm.py", line 344, in exec
>     new_states, op_code = self.execute_state(global_state)
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/svm.py", line 445, in execute_state
>     ).evaluate(global_state)
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/instructions.py", line 265, in evaluate
>     result = instruction_mutator(global_state)
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/instructions.py", line 196, in wrapper
>     new_global_states = self.call_on_state_copy(func, func_obj, global_state)
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/instructions.py", line 131, in call_on_state_copy
>     return func(func_obj, global_state_copy)
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/instructions.py", line 794, in calldataload_
>     value = environment.calldata.get_word_at(op0)
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/ethereum/state/calldata.py", line 55, in get_word_at
>     return simplify(Concat(parts))
>   File "/usr/local/lib/python3.10/site-packages/mythril/laser/smt/bitvec_helper.py", line 137, in Concat
>     nraw = z3.Concat([a.raw for a in bvs])
>   File "/usr/local/lib/python3.10/site-packages/z3/z3.py", line 4142, in Concat
>     _z3_assert(sz >= 2, "At least two arguments expected.")
>   File "/usr/local/lib/python3.10/site-packages/z3/z3.py", line 107, in _z3_assert
>     raise Z3Exception(msg)
> z3.z3types.Z3Exception: At least two arguments expected.
> 
> ==== Integer Arithmetic Bugs ====
> SWC ID: 101
> Severity: High
> Contract: 0x77777feddddffc19ff86db637967013e6c6a116c
> Function name: name()
> PC address: 960
> Estimated Gas Usage: 1422 - 2269
> The arithmetic operator can overflow.
> It is possible to cause an integer overflow or underflow in the arithmetic operation.
> --------------------
> Initial State:
> 
> Account: [ATTACKER], balance: 0x0, nonce:0, storage:{}
> Account: [SOMEGUY], balance: 0x0, nonce:0, storage:{}
> 
> Transaction Sequence:
> 
> Caller: [SOMEGUY], function: name(), txdata: 0x06fdde03, value: 0x0
> 
> ==== Integer Arithmetic Bugs ====
> SWC ID: 101
> Severity: High
> Contract: 0x77777feddddffc19ff86db637967013e6c6a116c
> Function name: link_classic_internal(uint64,int64) or symbol()
> PC address: 2636
> Estimated Gas Usage: 1465 - 2312
> The arithmetic operator can overflow.
> It is possible to cause an integer overflow or underflow in the arithmetic operation.
> --------------------
> Initial State:
> 
> Account: [ATTACKER], balance: 0x0, nonce:0, storage:{}
> Account: [SOMEGUY], balance: 0x0, nonce:0, storage:{}
> 
> Transaction Sequence:
> 
> Caller: [SOMEGUY], function: link_classic_internal(uint64,int64), txdata: 0x95d89b41, value: 0x0
> 
> ==== Dependence on predictable environment variable ====
> SWC ID: 116
> Severity: Low
> Contract: 0x77777feddddffc19ff86db637967013e6c6a116c
> Function name: _function_0xd505accf
> PC address: 3299
> Estimated Gas Usage: 616 - 711
> A control flow decision is made based on The block.timestamp environment variable.
> The block.timestamp environment variable is used to determine a control flow decision. Note that the values of variables like coinbase, gaslimit, block number and timestamp are predictable and can be manipulated by a malicious miner. Also keep in mind that attackers know hashes of earlier blocks. Don't use any of those environment variables as sources of randomness and be aware that use of these variables introduces a certain level of trust into miners.
> --------------------
> Initial State:
> 
> Account: [ATTACKER], balance: 0x0, nonce:0, storage:{}
> Account: [SOMEGUY], balance: 0x0, nonce:0, storage:{}
> 
> Transaction Sequence:
> 
> Caller: [SOMEGUY], function: unknown, txdata: 0xd505accf000000000000000000000000aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, decoded_data: , value: 0x0
> ```

---

What is Fees

- [Token Terminal | Fundamentals for crypto](https://tokenterminal.com/terminal/metrics/fees)
- [Fees – Weekly fundamentals #59 | Token Terminal](https://tokenterminal.com/resources/weekly-fundamentals/59#product-tip-of-the-week)

---

Method ID

- [Etherscan Information Center | Method ID](https://info.etherscan.com/what-is-method-id/)
- [Ethereum Signature Database](https://www.4byte.directory/)

---

Mempool

- [How to access Ethereum Mempool | QuickNode](https://www.quicknode.com/guides/ethereum-development/transactions/how-to-access-ethereum-mempool)
- [Geth API — web3.py 7.2.0 documentation](https://web3py.readthedocs.io/en/latest/web3.geth.html#web3.geth.txpool.TxPool.content)

---

Internal Transaction

- [web3js - How to get contract internal transactions - Ethereum Stack Exchange](https://ethereum.stackexchange.com/questions/3417/how-to-get-contract-internal-transactions)
  - Instrumented EVM
    - [ethereumjs/ethereumjs-monorepo: Monorepo for the Ethereum VM TypeScript Implementation](https://github.com/ethereumjs/ethereumjs-monorepo)
  - Others' API (e.g. Etherscan)
- [Internal Transaction Monitoring Is The Missing Puzzle Piece To Understanding Your Smart Contract Activity](https://www.blocknative.com/blog/eth-internal-transactions)
- [Internal Transactions FAQs | Moralis Web3 Documentation](https://docs.moralis.io/web3-data-api/evm/internal-transactions)
