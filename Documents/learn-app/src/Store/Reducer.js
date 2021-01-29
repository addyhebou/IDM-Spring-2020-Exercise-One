const initialState = {
    message: "Subscribe to Miina Saray"
}

const reducer = ( state = initialState, action) => {
    const newState = {...state};

    if (action.type === "Message change"){
        newState.message = 'Thank you for subscribing to Miina';
    }
    return newState;
}

export default reducer;
