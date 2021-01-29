import logo from './logo.svg';
import './App.css';
import FC from "./Components/FunctionalComp"
import {ClassComp1} from "./Components/ClassComp"
import Click from "./Components/Click"
import Click2 from "./Components/Click2"
import Click3 from "./Components/Click3"
import Click4 from "./Components/Click4"
import Counter from "./Components/Counter"
import ParentComp from "./Components/ParentComp"
import ClassProps from "./Components/ClassProps"
import FunctionalProp from "./Components/FunctionalProp"
import React, { Component } from 'react'
import ReduxComp from './Components/ReduxComp';
import FetchRandomUser from './Components/FetchRandomUser';

class App extends React.Component{

  styles={
    fontStyle: "bold",
    color: "teal"
  }

  render(){
    return (
    <div className = "App">
      <FetchRandomUser />
    </div>)
  }
}

export default App

