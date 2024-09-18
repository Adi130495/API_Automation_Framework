# Create Token
# Create Booking ID
# Update the Booking (PUT) - BookingID, Token
# Delete the Booking

# Verify that created booking id when we update we are able to update it and delete it

import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

class TestCRUDBooking(object):

    @pytest.fixture()
    def create_token(self):
        util = Util()  # Instantiate Util
        response = post_request(
            url=APIConstants.url_create_token(),
            headers=util.common_headers_json(),  # Use instance of Util
            auth=None,
            payload=payload_create_token(),
            in_json=False
        )
        verify_https_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null_token(response.json()["token"])
        return response.json()["token"]

    @pytest.fixture()
    def get_booking_id(self):
        util = Util()  # Instantiate Util
        response = post_request(
            url=APIConstants.url_create_booking(),
            auth=None,
            headers=util.common_headers_json(),  # Use instance of Util
            payload=payload_create_booking(),
            in_json=False
        )

        booking_id = response.json()["bookingid"]

        verify_https_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id

    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        util = Util()  # Instantiate Util
        response = put_requests(
            url=put_url,
            headers=util.common_header_put_patch_delete_cookie(token=token),  # Use instance of Util
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        verify_https_status_code(response_data=response, expect_data=200)

    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        util = Util()  # Instantiate Util
        response = delete_requests(
            url=delete_url,
            headers=util.common_header_put_patch_delete_cookie(token=token),  # Use instance of Util
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_https_status_code(response_data=response, expect_data=201)
