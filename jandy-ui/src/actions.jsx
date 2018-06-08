import * as types from './constants/ActionTypes';
import user from 'User';
import axios from 'axios';

export function fetchProfile() {
    return async dispatch => {
        return dispatch({
            type: types.FETCH_PROFILE,
            text: "test"
        });
    };
}

export function fetchAccessToken(code) {
    return async dispatch => {

        const response = await axios.post(`http://localhost:3000/rest/github/oauth/access-token`, { code });
        user.accessToken = response.data['access_token'];

        return dispatch({
            type: types.FETCH_ACCESS_TOKEN,
            payload: response.data
        });
    }
}