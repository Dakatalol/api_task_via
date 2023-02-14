import requests


class ApiInteractions:
    """
    Helper utility for making CRUD operations on end points. Works with no auth, OAuth1 and Basic Auth.
    """

    @classmethod
    def post(cls, url: str, json: any, header_data: dict = None):
        """
        Perform a POST request

        Args:
            url: Endpoint URL
            json: Body of the request in json format
            header_data: JSON formatted Headers for the request

        Returns:
            Response data from the request
        """

        return requests.post(url, json=json, headers=header_data)
