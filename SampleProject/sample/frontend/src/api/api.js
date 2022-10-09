import { Buffer } from "buffer";

const BASE_URL = "metamask/"

async function createUser() {
    const publicAddress = await getPublicAddress()
    // This request is used to create the user and you will receive a nonce and public address as a result
    fetch(BASE_URL, {
        method: "POST",
        mode: "cors",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            public_address: publicAddress,
            user: {
                username: "TestUsre"
            }
        })
    })
        .then(response => response.json())
        .then(data => console.log(data))
}

async function login(){
    // retrieved from previous request
    const nonce = ""
    const from =""
    const msg = `0x${Buffer.from(nonce, 'utf8').toString('hex')}`;
    const sign = await window.ethereum.request({
      method: 'personal_sign',
      params: [msg, from],
    });
    
    fetch(BASE_URL+"login/"+from, {
        method: "POST",
        mode: "cors",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            signature : sign
        })
    })
        .then(response => response.json())
        .then(data => console.log(data))
}

async function getPublicAddress() {
    await window.ethereum.request({ method: 'eth_requestAccounts' }); // Only need to call once
    const accounts = await ethereum.request({ method: 'eth_accounts' });
    return accounts[0]
}



export { getPublicAddress, createUser, login }