from Utils.api_utility import ApiInteractions


class DemoblazeApi:
    """
    This class allows the user to hit the various endpoints that are accessible in the demoblaze service
    and returns the response back to be used to validate the responses.
    """
    base_url = 'https://api.demoblaze.com/'
    auth = None
    headers = {'Content-Type': 'application/json'}

    # POST Requests
    @classmethod
    def login_user(cls, json):
        return ApiInteractions.post(cls.base_url + 'login', header_data=cls.headers, json=json)

    @classmethod
    def signup_user(cls, json):
        return ApiInteractions.post(cls.base_url + 'signup', header_data=cls.headers, json=json)

    @classmethod
    def add_to_cart(cls, json):
        return ApiInteractions.post(cls.base_url + 'addtocart', header_data=cls.headers, json=json)

    @classmethod
    def view_cart(cls, json):
        return ApiInteractions.post(cls.base_url + 'viewcart', header_data=cls.headers, json=json)

    @classmethod
    def delete_product(cls, json):
        return ApiInteractions.post(cls.base_url + 'deleteitem', header_data=cls.headers, json=json)
