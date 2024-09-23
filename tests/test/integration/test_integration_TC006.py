import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


def test_update_deleted_booking(self, create_token, get_booking_id):
    booking_id = get_booking_id
    token = create_token
    util = Util()

    # Delete the booking first
    delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
    delete_response = delete_requests(
        url=delete_url,
        headers=util.common_header_put_patch_delete_cookie(token=token),
        auth=None,
        in_json=False
    )
    verify_https_status_code(response_data=delete_response, expect_data=201)

    # Try to update the deleted booking
    put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
    response = put_requests(
        url=put_url,
        headers=util.common_header_put_patch_delete_cookie(token=token),
        payload=payload_create_booking(),
        auth=None,
        in_json=False
    )

    verify_https_status_code(response_data=response, expect_data=404)
