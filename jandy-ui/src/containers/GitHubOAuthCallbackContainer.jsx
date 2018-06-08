import React from 'react';
import {connect} from "react-redux";
import {bindActionCreators} from "redux";
import {fetchAccessToken} from '../actions';

class GitHubOAuthCallbackContainer extends React.Component {
    render() {
        const params = new URLSearchParams(new URL(document.location).searchParams);
        const code = params.get("code");

        this.props.fetchAccessToken(code);

        return null;
    }
}

export default connect(null, dispatch => bindActionCreators({ fetchAccessToken }, dispatch))(GitHubOAuthCallbackContainer);