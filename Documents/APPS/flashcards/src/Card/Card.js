import React from 'react';
import './Card.css';

const Card = ( props ) => {
    return (
        <div className = "card-container">
            <div className = "card">
                <div className = "front">
                    <div className = "frontContent">{props.front}</div>
                </div>
                <div className = "back">
                    <div className = "backContent">{props.back}</div>
                </div>
            </div>
        </div>
    )
}

export default Card;
