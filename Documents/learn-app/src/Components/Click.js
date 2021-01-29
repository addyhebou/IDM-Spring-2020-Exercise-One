import React, { Component } from 'react';
import UpdatedComp from "./HigherOrder"

export class Click extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             num: 0
        }
    }

    inc = ()=>{
        const numVal = this.state.num;
        this.setState({num: numVal + 1})
    }
    
    render() {
        const bob = this.state.num
        return (
            <div>
                <h1>Below is a button:</h1>
                <button onClick = {this.inc}>{this.props.name}{bob}</button>
            </div>
        )
    }
}

export default UpdatedComp(Click);
