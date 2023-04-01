import React, {Component, useState} from 'react';
import './SignIn.css';
import { useHistory } from 'react-router-dom';



function SignIn(props){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    async function handleLogin(){
        const response = await fetch('http://127.0.0.1:5000/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        if(response.ok){
            //sign into the account
            console.log('lmaooo')


        } else{
            //redirect back to page/tell user that
            //their account info is wrong
        }

    }

    return (
        <div className="grid-container">
        <h1 className="grid-item"> Sign In</h1>
        <div className="username-input-container"> 
            <label className="a-form-label"> Email or Username</label>
            <input type="text" value={username} className="user-input" onChange={(event) => setUsername(event.target.value) }/>
        </div>
        <div className="username-input-container">
            <label className="a-form-label"> Password </label>
            <input type="password" value={password} className="user-input" onChange={(event) => setPassword(event.target.value)}/>
        </div>
        <div className="register-login-container"> 
            <a className="register-button" href="https://www.paethos.me/passive-deals/register">Register</a>
            <button className="login-button" onClick={handleLogin}>Log In</button>
        </div>

    </div>
    );


}

export default SignIn