import PropTypes from 'prop-types';

const KEY_ACCESS_TOKEN = "commentary.user.github.access_token";

class User {
    get accessToken() {
        return window.localStorage.getItem(KEY_ACCESS_TOKEN);
    }

    set accessToken(val) {
        window.localStorage.setItem(KEY_ACCESS_TOKEN, val);
    }
}

User.propTypes = {
    accessToken: PropTypes.string
};

export default new User();