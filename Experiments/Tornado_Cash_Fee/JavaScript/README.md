- [Node.js includes built-in support for .env files](https://philna.sh/blog/2023/09/05/nodejs-supports-dotenv/)
- [motdotla/dotenv: Loads environment variables from .env for nodejs projects.](https://github.com/motdotla/dotenv)

TODO:

```js
const { ethers } = require('ethers');

// Connect to an Ethereum node (e.g., Infura)
const provider = new ethers.providers.JsonRpcProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID");

// Tornado Cash contract address and ABI for the events (you need to get the ABI from Etherscan)
const tornadoCashAddress = "0xYourTornadoCashContractAddress";
const tornadoAbi = [...]  // replace with the actual ABI

const tornadoCashContract = new ethers.Contract(tornadoCashAddress, tornadoAbi, provider);

async function fetchDailyFees() {
    const startBlock = 13000000; // starting block number
    const endBlock = await provider.getBlockNumber(); // current block number
    
    // Fetch logs of fee events (assuming the event name is "YourFeeEvent")
    const filter = tornadoCashContract.filters.YourFeeEvent();
    const events = await tornadoCashContract.queryFilter(filter, startBlock, endBlock);
    
    const feeData = [];

    for (const event of events) {
        const block = await provider.getBlock(event.blockNumber);
        const timestamp = block.timestamp;
        const date = new Date(timestamp * 1000).toISOString().slice(0, 10); // Get the date part
        const fee = ethers.utils.formatEther(event.args.fee);
        feeData.push({ date, fee: parseFloat(fee) });
    }

    // Aggregate fees by day
    const dailyFees = feeData.reduce((acc, { date, fee }) => {
        acc[date] = (acc[date] || 0) + fee;
        return acc;
    }, {});

    console.log(dailyFees);
}

fetchDailyFees();
```
