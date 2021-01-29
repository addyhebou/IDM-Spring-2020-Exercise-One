import React, { Component } from 'react'
import bellA from "./97600734-bell-icon-vector-alarm-handbell-yellow-isolated-sign-in-flat-style-.jpg"
import bellB from "./isolated-bell-icon-notification-symbol-calling-to-press-a-bell-sign-reminder-button-to-subscribers-of-fresh-video-content-entry-2BGK073.jpg"

export class NewComp extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             message: "Subscribe to Saint Steph",
             sub: "Subscribe",
             imageUrl: bellA
        }
    }

    styles={
        fontStyle: "italis",
        color: "purple"
    }

    buttonChange = () =>{
        this.setState({message: "Thank you for subscribing", imageUrl: bellB, sub: "Subscribed!"});
    }
    
    
    render() {
        return (
            <div className = "App">
                <h3 style = {this.styles}>{this.state.message}</h3>
                <button onClick = {this.buttonChange}>{this.state.sub}</button>
                <p/>
                <img src={this.state.imageUrl}/>
            </div>
        )
    }
}

export default NewComp
