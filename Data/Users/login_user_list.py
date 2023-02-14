from Utils.Utils import Utils

INVALID_PASSWORD_LOGIN = {
    'INPUT_REQUEST_BODY': {"username": "sss", "password": "c3Nz"},
    'EXPECTED_RESPONSE_BODY': {"errorMessage": "Wrong password."}
}
INVALID_USER_LOGIN = {
    'INPUT_REQUEST_BODY': {"username": "pesho1232323", "password": "ssss"},
    'EXPECTED_RESPONSE_BODY': {"errorMessage": "User does not exist."}
}
VALID_USER_LOGIN = {
    'INPUT_REQUEST_BODY':
        {"username": Utils.generate_random_name(), "password": Utils.encode_user_password(b'test_password')},
    'EXPECTED_RESPONSE_BODY': "Auth_token:"
}
