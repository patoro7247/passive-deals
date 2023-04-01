import React, {Component, useState} from 'react';
import './SignIn.css';
import { useHistory } from 'react-router-dom';



function Register(props){
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    async function handleRegistration(){
        const response = await fetch('http://127.0.0.1:5000/api/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({
                email: email,
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
        <h1 className="grid-item">Register</h1>
        <div className="username-input-container"> 
            <label className="a-form-label">Email</label>
            <input type="text" value={email} className="user-input" onChange={(event) => setEmail(event.target.value) }/>
        </div>
        <div className="username-input-container">
            <label className="a-form-label"> Password </label>
            <input type="password" value={password} className="user-input" onChange={(event) => setPassword(event.target.value)}/>
        </div>
        <div className="register-login-container"> 
            <button className="login-button" onClick={handleRegistration}>Register</button>
        </div>

    </div>
    );


}

export default Register