import React, { Component } from 'react';
import logo from './logo.svg';
import {Navigation} from './components/Navigation'
import './App.css';

class App extends Component {
  constructor(props){
    super(props)
  }


  render() {

    return (
      <div className="container">
      <Navigation/>
      </div>
    );
  }
}

export default App;
