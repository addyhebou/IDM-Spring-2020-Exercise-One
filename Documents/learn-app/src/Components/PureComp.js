import React, { PureComponent } from 'react';

class PureComp extends React.Component {
    render() {
        console.log("pure comp render")
        return (
            <div>I"m the pure component - {this.props.name}</div>
        )
    }
}

export default PureComp;
