# Learn Solidity Syntax

## Resources

- [alchemyplatform/learn-solidity-presentations: All of the presentations in the Learn Solidity course](https://github.com/alchemyplatform/learn-solidity-presentations)
- [foundry - Ethereum Development Framework](https://getfoundry.sh/) - Use to run unit test, ...
- [Marp: Markdown Presentation Ecosystem](https://marp.app/) [presentation](./presentations/)

---

- [EVM Codes - An Ethereum Virtual Machine Opcodes Interactive Reference](https://www.evm.codes/)
- [Opcodes for the EVM | ethereum.org](https://ethereum.org/developers/docs/evm/opcodes/)

---

- [Foundry forge in monorepo](https://chatgpt.com/g/g-p-68ef9e5c2b7481919480de565ea6aac1-web3-crypto/shared/c/690abebb-c8dc-8323-bb55-d3214b87bce4?owner_user_id=user-B4WgHPeH6xDhpfy8YNMr7nRy)
  - [foundry/crates/config at master · foundry-rs/foundry](https://github.com/foundry-rs/foundry/tree/master/crates/config)

```bash
cd ./presentations/1a-value-types/examples/0-example-value-types
forge compile
forge test

cd ./examples/0-example-value-types
forge init --no-git .
# copied Example.sol & delete scripts
forge compile
forge test
# show logs
forge test -vv
```
