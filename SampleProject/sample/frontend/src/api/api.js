import { Buffer } from "buffer";

const BASE_URL = "metamask/"

async function createUserAndLogin({username}) {

    const publicAddress = await getPublicAddress()
    return fetch(BASE_URL, {
        method: "POST",
        mode: "cors",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            public_address: publicAddress,
            user: {
                username: username
            }
        })
    }).then(response => response.json()).then(
        (data) => {
            return login(data)
        })
    }

async function login({nonce, public_address}) {

    const msg = `0x${Buffer.from(nonce, 'utf8').toString('hex')}`;
    const sign = await window.ethereum.request({
        method: 'personal_sign',
        params: [msg, public_address],
    });

    return fetch(BASE_URL + "login/" + public_address, {
        method: "POST",
        mode: "cors",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            signature: sign
        })
    })
        .then(response => response.json()).then((data) => {
            return data
        })
}

async function getPublicAddress() {
    await window.ethereum.request({ method: 'eth_requestAccounts' }); // Only need to call once
    const accounts = await ethereum.request({ method: 'eth_accounts' });
    return accounts[0]
}

async function performLogin(){
    const publicAddress = await getPublicAddress()
    const URL =  BASE_URL + publicAddress
    return fetch(URL, {
        method: "GET",
        mode: "cors",
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(response => response.json()).then(
        (data) => {
            return login(data)
        })
}



export { getPublicAddress, createUserAndLogin, login, performLogin }