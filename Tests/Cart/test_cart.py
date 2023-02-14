import pytest

from Services.api.demoblaze_api import DemoblazeApi
from Data.Cart.add_to_cart import ADD_TO_CART_PRODUCT_7
from Data.Cart.view_cart import VIEW_CART_PRODUCT_7
from Data.Cart.delete_cart import DELETE_PRODUCT_7


@pytest.mark.smoke
def test_successful_add_to_cart_status_code():
    """
    POST /addtocart
    Validating successful add to cart
    """

    # adding product with id=7
    response = DemoblazeApi.add_to_cart(ADD_TO_CART_PRODUCT_7['INPUT_REQUEST_BODY'])

    # verifying successful response code
    assert response.status_code == 200


@pytest.mark.smoke
def test_successful_add_to_cart_and_view_cart_product():
    """
    POST /addtocart & /viewcart
    Validating that product can be added to the cart and to be viewed
    """
    # adding product with id=7
    DemoblazeApi.add_to_cart(ADD_TO_CART_PRODUCT_7['INPUT_REQUEST_BODY'])
    # hitting the view cart endpoint
    response = DemoblazeApi.view_cart(VIEW_CART_PRODUCT_7['INPUT_REQUEST_BODY'])
    result = response.json()

    # verifying that product with id=7 is in the cart
    assert VIEW_CART_PRODUCT_7['EXPECTED_RESPONSE_BODY'] in result['Items']


@pytest.mark.smoke
def test_delete_product():
    """
    POST /deleteitem
    Validation that the product is not visible in the cart after deletion
    """
    # adding product with id=7
    DemoblazeApi.add_to_cart(ADD_TO_CART_PRODUCT_7['INPUT_REQUEST_BODY'])
    # deleting the previously added product
    DemoblazeApi.delete_product(DELETE_PRODUCT_7['INPUT_REQUEST_BODY'])
    # getting the response from the cart
    response = DemoblazeApi.view_cart(VIEW_CART_PRODUCT_7['INPUT_REQUEST_BODY'])
    result = response.json()

    # verifying if the product is no longer in the cart
    assert VIEW_CART_PRODUCT_7['EXPECTED_RESPONSE_BODY'] not in result['Items']
