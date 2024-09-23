import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


def test_get_booking_ids_update_and_verify(self, create_token):
    token = create_token
    util = Util()

    # Get all booking IDs
    get_all_ids_url = APIConstants.url_create_booking()
    all_bookings = get_request(url=get_all_ids_url, auth=None)

    # Assuming we take the first booking
    booking_id = all_bookings[0]["bookingid"]

    # Update booking
    update_payload = payload_create_booking_dynamic()
    update_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
    update_response = put_requests(
        url=update_url,
        headers=util.common_header_put_patch_delete_cookie(token=token),
        payload=update_payload,
        auth=None,
        in_json=True
    )
    verify_https_status_code(response_data=update_response, expect_data=200)

    # Verify the updated booking
    get_booking_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
    get_response = get_request(url=get_booking_url, auth=None)

    assert get_response["firstname"] == update_payload["firstname"], "Update failed"
