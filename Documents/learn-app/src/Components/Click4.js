import React, { Component } from 'react'

class Click4 extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             num: 0,
        };
    };

    incrementNum = () =>{
        this.setState({num: this.state.num + 1})
    }
    
    render() {
        return (
            <div>
                <button onClick = {this.incrementNum}>Click</button>
                <p>{this.state.num}</p>
            </div>
        )
    }
}

export default Click4
