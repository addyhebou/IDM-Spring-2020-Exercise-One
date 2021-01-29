import React, { Component } from 'react';
import UpdatedComp from "./HigherOrder"

export class Counter extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             count:0
        };
    }

    inc = () => {
        const num = this.state.count
        this.setState({count: num + 1})
    }
    
    render() {
        return (
            <div>
                <button onMouseEnter={this.inc}>
                    {this.props.name}Incremented to {this.state.count}
                </button>
            </div>
        )
    }
}

export default UpdatedComp(Counter);
