import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

def test_create_delete_booking_verify_absence(self, create_token):
    token = create_token
    util = Util()

    # Create a booking
    response = post_request(
        url=APIConstants.url_create_booking(),
        headers=util.common_headers_json(),
        auth=None,
        payload=payload_create_booking(),
        in_json=True
    )
    booking_id = response["bookingid"]
    verify_https_status_code(response_data=response, expect_data=200)

    # Delete the booking
    delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
    delete_response = delete_requests(
        url=delete_url,
        headers=util.common_header_put_patch_delete_cookie(token=token),
        auth=None,
        in_json=False
    )
    verify_https_status_code(response_data=delete_response, expect_data=201)

    # Verify booking does not exist
    get_response = get_request(url=delete_url, auth=None)
    assert get_response == {}, "Booking still exists after deletion"
