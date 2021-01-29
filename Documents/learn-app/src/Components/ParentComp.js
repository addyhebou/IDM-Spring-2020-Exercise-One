import React, { Component } from 'react'
import PureComp from "./PureComp"
import RegComp from "./RegComp"
export class ParentComp extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             name: "PopSmoke"
        }
    }
    
    componentDidMount(){
        setInterval(()=>{
            this.setState({
                name: "PopSmoke"
            });
        }, 3000);
        
    }
    render() {
        console.log("parent render");
        return (
            <div>I'm the parent Component
                <RegComp name={this.state.name}/>
                <PureComp name = {this.state.name}/>
            </div>
        )
    }
}

export default ParentComp
