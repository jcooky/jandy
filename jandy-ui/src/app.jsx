import 'bootstrap/scss/bootstrap.scss';
import 'bootstrap';
import 'whatwg-fetch';
import 'url-search-params';
import React from 'react';
import {applyMiddleware, createStore} from "redux";
import * as ReactDOM from "react-dom";
import {Provider} from "react-redux";
import {Route, BrowserRouter as Router, Switch} from "react-router-dom";
import Index from "./components";
import reducer from './reducers';
import thunk from 'redux-thunk';
import GitHubOAuthCallbackContainer from './containers/GitHubOAuthCallbackContainer';

const store = createStore(reducer, applyMiddleware(thunk));
ReactDOM.render(
    <Provider store={store}>
        <Router>
            <Switch>
                <Route path="/github/oauth/callback" component={GitHubOAuthCallbackContainer} />
                <Route exact path="/" component={Index} />
            </Switch>
        </Router>
    </Provider>,
    document.getElementById("root")
);
