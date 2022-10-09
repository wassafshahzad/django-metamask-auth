import React, { Component } from "react";
import { createUser, login } from "../api/api";

export  class MetaMask extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return (
        <div className="container">
            <div className="logo-contianer">
                <img src="https://cdn.dribbble.com/users/2574702/screenshots/6702374/metamask.gif"/>
            </div>
            <div className="form-container">
                <button onClick={() => login() }>Login process</button>
            </div>
        </div>)
    }
}

// {
//     "public_address": "0x18420dbf3fd84400ebdc5f18caa54b99796ecebb",
//     "nonce": "GQ9FNOYR0VXIYZJ6UEHGQ74A",
//     "user": {
//         "email": "",
//         "username": "TestUsre"
//     }
// }