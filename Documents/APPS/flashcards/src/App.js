import React, { Component } from 'react';
import './App.css';
import Card from './Card/Card.js';
import DrawButton from './DrawButton/DrawButton.js';
import firebase from 'firebase/app';
import 'firebase/database';

import { DB_CONFIG } from './Config/Firebase/db_config';

class App extends Component{ 

  constructor(props) {
    super(props);

    if (!firebase.apps.length) {
      this.app = firebase.initializeApp(DB_CONFIG);
    } else {
      this.app = firebase.app(); // if already initialized, use that one
    }
    this.database = this.app.database().ref().child('cards');
    this.updateCard = this.updateCard.bind(this);


    this.state = {
      cards: [],
      currentCard: {}
    }
  }

  componentWillMount(){
    // Gets called immediately after the constructor and before component is rendered
    const currentCards = this.state.cards;
    this.database.on('child_added', snap => {
      currentCards.push({
        id: snap.key,
        front: snap.val().front,
        back: snap.val().back,
      })

      this.setState({
        cards: currentCards,
        currentCard: this.getRandomCard(currentCards)
      })
    })
  }
  // componentDidMount gets called after the component is rendered

  getRandomCard(currentCards){
    var card = currentCards[Math.floor(Math.random() * currentCards.length)];
    return card;
  }

  updateCard(){
    console.log('New card!');
    this.setState({
      currentCard: this.getRandomCard(this.state.cards),
    })
  }


  render() {
    return (
      <div className="App">
        <div className = "Header">Positive Affirmations</div>
        <div className = "background">
          <div>
            <div className = "cardRow" style = {{backgroundColor: 'non'}}>
              <div className = "behind"></div>
              <div className = "middle"></div>
              <div className = "top">
                <Card front = {this.state.currentCard.front} back = {this.state.currentCard.back}/>
              </div>
            </div>
            <div className = "drawRow" style = {{backgroundColor: 'none'}}>
              <DrawButton drawCard = {this.updateCard} />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
