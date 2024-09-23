# Integration Scenarios :-

# Verify that Create Booking -> PATCH request -> Verify that firstname is updated
# Create a Booking, Delete the Booking with ID and verify using GET request that it should not exist
# Get an Existing Booking ID from GET all Booking ID's, Update a Booking and verify using GET by ID
# Create a Booking, DELETE it
# Invalid creation -> enter a wrong payload or wrong JSON
# Try to update on a Delete ID -> 404

# Test for the Single Request :-
# Response
# Status code
# Headers

import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

def test_patch_update_booking_firstname(create_token, get_booking_id):
    booking_id = get_booking_id
    token = create_token
    patch_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
    util = Util()

    # Updating only the firstname
    updated_payload = {
        "firstname": "UpdatedName"
    }

    response = patch_requests(
        url=patch_url,
        headers=util.common_header_put_patch_delete_cookie(token=token),
        payload=updated_payload,
        auth=None,
        in_json=True
    )

    verify_https_status_code(response_data=response, expect_data=200)

    # Verify the updated firstname
    get_booking_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
    get_response = get_request(url=get_booking_url, auth=None)

    assert get_response["firstname"] == "UpdatedName", "Failed to update firstname"


