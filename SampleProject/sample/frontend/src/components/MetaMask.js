import React, { Component } from "react";
import { createUserAndLogin, performLogin } from "../api/api";
import party from "party-js";
import "./style.css"

export class MetaMask extends Component {

    constructor(props) {
        super(props);
        this.state = {
            username: "",
            isRegister: false,
            isLoggedIn: true
        }
    }

    toggleHeader({ target }, isRegister) {
        const currentHeader = document.getElementsByClassName("active")[0]
        currentHeader.classList.remove("active")
        currentHeader.classList.add("inactive", "underlineHover")
        target.classList.add("active")
        target.classList.remove("inactive", "underlineHover")
        this.setState({ ...this.state, isRegister: isRegister })
    }

    setUsername({ value }) {
        this.setState({ ...this.state, username: value })
    }

    setLoggedIn(value) {
        this.setState({ ...this.state, isLoggedIn: value })
        if (value){
            alert("Logged in successfully")
        }
    }

    authenticationCard() {
        return <>
            <h2 className="active" onClick={(e) => this.toggleHeader(e, false)}> Sign In </h2>
            <h2 className="inactive underlineHover" onClick={(e) => this.toggleHeader(e, true)}>Sign Up </h2>
            <form>
                <img style={{ width: "80%" }} src="https://cdn.dribbble.com/users/2574702/screenshots/6702374/metamask.gif" />
                {this.state.isRegister ? <input type="text" className="fadeIn" placeholder="Enter username" value={this.state.username} onChange={({ target }) => this.setUsername(target)} /> : ""}
                <input type="submit" className="fadeIn fourth" value={`${this.state.isRegister ? "Register" : "SignUp"} using MetaMask`} onClick={async (e) => {
                    e.preventDefault()
                    let response;
                    if (this.state.isRegister) {
                        response = await createUserAndLogin(this.state)
                    }
                    else {

                        response = await performLogin()
                    }
                    if (response) {
                        this.setLoggedIn(true)
                    }
                    else {
                        this.setLoggedIn(false)
                    }
                }
                } />
            </form>
        </>
    }

    render() {
        return <>
            <div className="wrapper fadeInDown">
                <div id="formContent">
                    {this.authenticationCard()}
                </div>
            </div>
        </>
    }
}
