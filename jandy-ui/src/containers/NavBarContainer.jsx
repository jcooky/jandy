import React from 'react';
import {connect} from "react-redux";
import {fetchProfile} from '../actions';
import {bindActionCreators} from "redux";
import NavBar from "../components/NavBar";

class NavBarContainer extends React.Component {
    handleSubmitSignIn(e) {
        e.preventDefault();
        e.stopPropagation();

        const clientId = "5b6118bdbd4066c1ea7a";

        window.location.href = `https://github.com/login/oauth/authorize?client_id=${clientId}&scope=user,repo`
    }

    render() {
        return (
            <NavBar onSubmitSignIn={::this.handleSubmitSignIn} />
        );
    }
}

export default connect(null, dispatch => bindActionCreators({ fetchProfile }, dispatch))(NavBarContainer);

