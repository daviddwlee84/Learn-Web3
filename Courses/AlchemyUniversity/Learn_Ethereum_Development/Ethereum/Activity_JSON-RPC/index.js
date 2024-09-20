const { formatEther } = require('ethers');
let axios = require('axios');

// (Optional) Use proxy behind GFW
// https://stackoverflow.com/questions/55981040/how-to-use-axios-with-a-proxy-server-to-make-an-https-call
// https://github.com/axios/axios/issues/2072
const { HttpsProxyAgent } = require("https-proxy-agent");
const httpsAgent = new HttpsProxyAgent({ host: "127.0.0.1", port: "7891" });
axios = axios.create({ httpsAgent });

// copy-paste your URL provided in your Alchemy.com dashboard
const ALCHEMY_URL = "https://eth-mainnet.g.alchemy.com/v2/4DdKxdQMB6xxPd-SjpQan_mCW7Q1zT6g/";

axios.post(ALCHEMY_URL, {
  jsonrpc: "2.0",
  id: 1,
  method: "eth_getBlockByNumber",
  params: [
    "0xb443", // block 46147
    true  // retrieve the full transaction object in transactions array
  ]
}).then((response) => {
  console.log('The block number of 0xb443 is', response.data.result);
});

const payload = {
  jsonrpc: '2.0',
  id: 1,
  method: 'eth_blockNumber',
  params: []
};

axios.post(ALCHEMY_URL, payload)
  .then(response => {
    console.log('The latest block number is', parseInt(response.data.result, 16));
  })
  .catch(error => {
    console.error(error);
  });


// https://docs.alchemy.com/reference/eth-getcode
// https://docs.chainstack.com/reference/ethereum-getcode
async function verifyContractAddress(address, addressName) {
  try {
    const response = await axios.post(ALCHEMY_URL, {
      'jsonrpc': "2.0",
      id: 1,
      method: 'eth_getCode',
      params: [
        address,
        'latest'
      ]
    });

    const bytecode = response.data.result;
    if (bytecode !== '0x') {
      console.log(`${addressName} (${address}) is a smart contract.`);
      return true;
    } else {
      console.log(`${addressName} (${address}) is not a smart contract.`);
      return false;
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
    return false;
  }
}

function verifyContractAddressPromiseWay(address, addressName) {
  return axios.post(ALCHEMY_URL, {
    'jsonrpc': "2.0",
    id: 1,
    method: 'eth_getCode',
    params: [
      address,
      'latest'
    ]
  })
    .then(response => {
      const bytecode = response.data.result;
      if (bytecode !== '0x') {
        console.log(`${addressName} (${address}) is a smart contract.`);
        return true;
      } else {
        console.log(`${addressName} (${address}) is not a smart contract.`);
        return false;
      }
    })
    .catch(error => {
      console.error(`Error: ${error.message}`);
      return false;
    });
}

verifyContractAddress("0x77777feddddffc19ff86db637967013e6c6a116c", "TORN Contract");
verifyContractAddressPromiseWay('0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045', "Vitalik's wallet");

// https://docs.alchemy.com/docs/how-to-get-eth-balance-at-a-point-in-time
// https://docs.alchemy.com/reference/eth-getbalance
// https://docs.ethers.org/v5/api/utils/display-logic/#utils-formatEther
axios.post(ALCHEMY_URL, {
  jsonrpc: "2.0",
  id: 1,
  method: "eth_getBalance",
  params: [
    "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045", // "vitalik.eth"
    "latest",
  ]
}).then((response) => {
  // return parseInt(response.data.result, 16);
  return response.data.result;
}).then((balance) => {
  const balance_eth = formatEther(balance);
  console.log(`Vitalik's balance is: ${balance_eth} ETH (original ${parseInt(balance, 16)})`);
});

// TODO: figure out how to use proxy with Alchemy SDK
