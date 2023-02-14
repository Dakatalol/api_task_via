import pytest

from Services.api.demoblaze_api import DemoblazeApi
from Data.Users.login_user_list import INVALID_PASSWORD_LOGIN, VALID_USER_LOGIN, INVALID_USER_LOGIN


@pytest.mark.smoke
def test_valid_user_login():
    """
    POST /login
    Validation for successful user login
    """
    # registering user with valid data
    DemoblazeApi.signup_user(VALID_USER_LOGIN['INPUT_REQUEST_BODY'])
    # logging the user
    response = DemoblazeApi.login_user(VALID_USER_LOGIN['INPUT_REQUEST_BODY'])
    result = response.json()

    # verifying that the login is successful by receiving auth_token and status code 200
    assert VALID_USER_LOGIN['EXPECTED_RESPONSE_BODY'] in result and response.status_code == 200


@pytest.mark.regression
def test_invalid_password_login():
    """
    POST /login
    Validation for incorrect password
    """
    # hitting the endpoint with valid username and invalid password
    response = DemoblazeApi.login_user(INVALID_PASSWORD_LOGIN['INPUT_REQUEST_BODY'])
    result = response.json()

    # verifying by response message-> "errorMessage": "Wrong password."
    assert result == INVALID_PASSWORD_LOGIN['EXPECTED_RESPONSE_BODY']


@pytest.mark.regression
def test_invalid_user_login():
    """
    POST /login
    Validation for incorrect username
    """
    # hitting the endpoint with invalid username
    response = DemoblazeApi.login_user(INVALID_USER_LOGIN['INPUT_REQUEST_BODY'])
    result = response.json()

    # verifying by response message-> "errorMessage": "User does not exist."
    assert result == INVALID_USER_LOGIN['EXPECTED_RESPONSE_BODY']
