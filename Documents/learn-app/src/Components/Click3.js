import React, { Component } from 'react'

export class Click3 extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             num: 0
        }
    }

    increment = () =>{
        this.setState({num: this.state.num + 1})
    }
    
    render() {
        return (
            <div>
                <button onClick = {this.increment}>{this.props.name}, Click To Increment: {this.state.num}</button>
            </div>
        )
    }
}

export default Click3
