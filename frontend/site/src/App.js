import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import Navbar from "./components/navbar/Navbar.js";
import SignIn from "./components/SignIn.js";
import Register from "./components/Register.js";

function App() {
  return (
    <div className="App">
      <div className="navbarContainer">
        <Navbar />
        
      </div>
      <SignIn />
    </div>
  );
}

export default App;
