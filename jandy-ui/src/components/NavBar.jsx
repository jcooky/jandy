import React from 'react';

export default ({onSubmitSignIn}) => (
    <nav className="navbar navbar-fixed-top navbar-expand-lg navbar-light bg-light">
        <a className="navbar-brand" href="/">Jandy</a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#bs-navbar-collapse-1" aria-controls="bs-navbar-collapse-1" aria-expanded="false" aria-label="Toggle Navigation">
            <span className="navbar-toggler-icon"/>
        </button>
        <div className="collapse navbar-collapse" id="bs-navbar-collapse-1">
            <ul className="navbar-nav mr-auto">
                <li className="nav-item">
                    <a className="nav-link" href="#">Repositories</a>
                </li>
            </ul>
            <form className="form-inline my-2 my-lg-0" onSubmit={onSubmitSignIn}>
                <button type="submit" className="btn btn-outline-dark my-2 my-sm-0">Sign in with GitHub</button>
            </form>
        </div>
    </nav>
)