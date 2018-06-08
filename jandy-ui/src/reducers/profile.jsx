import * as types from '../constants/ActionTypes';

const initialState = {
    text: ""
};

export default function profile(state = initialState, action) {
    switch(action.type) {
        case types.FETCH_PROFILE:
            return {
                text: action.text
            };
        default:
            return state;
    }
}