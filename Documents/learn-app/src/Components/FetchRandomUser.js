import React, { Component } from 'react'

class FetchRandomUser extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             loading: true,
        }
    }
    
    async componentDidMount(){
        // Our commpnent loaded once
        const url = "https://api.randomuser.me/";
        const response = await fetch(url); // fetch() allows us to make HTTP request to get data
    }
    render() {
        return (
            <div>
                {this.state.loading ? <div>loading...</div> : <div>person...</div>}
            </div>
        )
    }
}

export default FetchRandomUser
