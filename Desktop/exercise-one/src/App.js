import React from 'react';
// import logo from './logo.svg';
import{
  BrowserRouter as Router,
  Switch,
  Route,
  Link
}from "react-router-dom"
import './App.css';

import ArticleListing from './pages/ArticleListing';
import Article from './pages/Article';

function App() {
  return (
      <Router>
        <Switch>
          <Route path = "/Article/:id">
            <Article />
          </Route>
          <Route path = "/">
            <ArticleListing />
          </Route>
        </Switch>
      </Router>
  );
}

export default App;
