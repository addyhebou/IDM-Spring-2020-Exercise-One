import React, { Component } from 'react'

export class Click2 extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             number: Number(this.props.starterNum)
            //  name: "hey"
        };
    }

    // calc = () =>{
    //     goUp = true;
    //     if (this.state.number > 1000){
    //         goDown = false;
    //         this.divide(); 
    //     }
    //     if (this.state.number < 1000 && goUp == true){
    //         this.multiply();
    //     }
    //     else{
    //         this.divide()
    //         if (this.state.number == 1){
    //             goUp == true;
    //         }
    //     }

    // }

    multiply = () =>{
        this.setState({number: this.state.number * 2});
        console.log("muliply")
    }

    divide = () =>{
        this.setState({number: this.state.number / 2})
        console.log("divided")
    }
    
    render() {
        const num = this.state.number
        return (
            <div>
                <button onMouseOver = {this.multiply}>{num}</button>
            </div>
        )
    }
}

export default Click2;
